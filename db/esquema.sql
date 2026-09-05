-- ============================================================================
-- ACADEMIA EN VIGOR · Esquema completo de la base de datos
-- Proyecto Supabase: academia-en-vigor-dev (bcdivukgxtjkpedntumc, Frankfurt)
-- Versión 1.0 · 20 de agosto de 2026
--
-- Este archivo es LA FOTO COMPLETA de la base de datos. Todo lo que existe en
-- Supabase está aquí, y nada de lo que hay en Supabase falta aquí.
--
-- Se puede ejecutar TANTAS VECES COMO QUIERAS sobre la base de datos actual:
-- no borra datos, crea lo que falta y deja como estaba lo que ya existe.
--
-- Guárdalo en el repositorio como  db/esquema.sql
-- ============================================================================


-- ----------------------------------------------------------------------------
-- BORRADO TOTAL · descomentar SOLO si quieres empezar de cero de verdad.
-- Ojo: esto borra el contenido, no las cuentas de usuario (esas viven en auth).
-- ----------------------------------------------------------------------------
-- drop table if exists public.progreso     cascade;
-- drop table if exists public.imagenes     cascade;
-- drop table if exists public.preguntas    cascade;
-- drop table if exists public.contenidos   cascade;
-- drop table if exists public.entitlements cascade;
-- drop table if exists public.planes       cascade;
-- drop table if exists public.convocatorias cascade;
-- drop table if exists public.temas        cascade;
-- drop table if exists public.alumnos      cascade;
-- drop table if exists public.oposiciones  cascade;
-- drop function if exists public.tiene_acceso_tema(uuid) cascade;
-- drop function if exists public.handle_new_user() cascade;
-- drop function if exists public.marcar_actualizacion() cascade;


-- ============================================================================
-- 1 · CATÁLOGO
-- ============================================================================

create table if not exists public.oposiciones (
  id            text primary key,                    -- 'policia-nacional'
  display_name  text not null,
  activa        boolean not null default true,
  orden         integer not null default 0,
  created_at    timestamptz not null default now()
);

create table if not exists public.convocatorias (
  id            uuid primary key default gen_random_uuid(),
  oposicion_id  text not null references public.oposiciones(id) on delete cascade,
  nombre        text not null,
  fecha_examen  date,
  orden         integer not null default 0,
  created_at    timestamptz not null default now()
);

create table if not exists public.temas (
  id              uuid primary key default gen_random_uuid(),
  oposicion_id    text not null references public.oposiciones(id) on delete cascade,
  numero          integer not null,
  slug            text not null,
  titulo          text not null,
  orden           integer not null,
  es_gratuito     boolean not null default false,    -- decisión editorial: NUNCA la toca publicar.py
  content_version text not null default '0.1.0',
  visual_version  text not null default '0.1.0',
  publicado       boolean not null default false,    -- decisión editorial: NUNCA la toca publicar.py
  created_at      timestamptz not null default now(),
  updated_at      timestamptz not null default now()
);

-- Claves de conflicto que necesita publicar.py para hacer upsert
create unique index if not exists temas_oposicion_numero_key
  on public.temas (oposicion_id, numero);


-- ============================================================================
-- 2 · ALUMNOS Y DERECHOS DE ACCESO
-- ============================================================================

create table if not exists public.alumnos (
  id             uuid primary key references auth.users(id) on delete cascade,
  email          text not null,
  nombre         text,
  acepta_ofertas boolean not null default true,
  created_at     timestamptz not null default now(),
  updated_at     timestamptz not null default now()
);

create table if not exists public.planes (
  id                      text primary key,          -- 'pn-mensual'
  oposicion_id            text not null references public.oposiciones(id) on delete cascade,
  nombre                  text not null,
  tipo                    text not null,             -- free | mensual | trimestral | completa
  temas_por_mes           integer,                   -- null = sin goteo, todo abierto
  convocatorias_incluidas integer,                   -- para la COMPLETA (2x1)
  precio_centimos         integer not null,
  activo                  boolean not null default true,
  created_at              timestamptz not null default now()
);

create table if not exists public.entitlements (
  id                       uuid primary key default gen_random_uuid(),
  alumno_id                uuid not null references auth.users(id) on delete cascade,
  plan_id                  text not null references public.planes(id),
  oposicion_id             text not null references public.oposiciones(id) on delete cascade,
  fecha_alta               timestamptz not null default now(),   -- origen del goteo
  convocatoria_inicio_id   uuid references public.convocatorias(id),
  convocatorias_consumidas integer not null default 0,
  estado                   text not null default 'activo',       -- activo | cancelado | caducado
  stripe_subscription_id   text,
  created_at               timestamptz not null default now()
);

create index if not exists entitlements_alumno_idx
  on public.entitlements (alumno_id, oposicion_id, estado);


-- ============================================================================
-- 3 · CONTENIDO
-- ============================================================================

create table if not exists public.contenidos (
  id         uuid primary key default gen_random_uuid(),
  tema_id    uuid not null references public.temas(id) on delete cascade,
  tipo       text not null,                          -- parte | atestado
  markdown   text not null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create unique index if not exists contenidos_tema_tipo_key
  on public.contenidos (tema_id, tipo);

create table if not exists public.preguntas (
  id                 text primary key,               -- 'PN-T01-Q001'
  tema_id            uuid references public.temas(id) on delete cascade,  -- null en oficiales
  oposicion_id       text not null references public.oposiciones(id) on delete cascade,
  origen             text not null,                  -- propia | oficial
  bloque             integer,
  enunciado          text not null,
  opciones           jsonb not null,
  respuesta_correcta text not null,
  explicacion        text,
  retroalimentacion  jsonb,
  norma              text,
  articulo           text,
  created_at         timestamptz not null default now()
);

create index if not exists preguntas_tema_idx on public.preguntas (tema_id);
create index if not exists preguntas_oposicion_origen_idx on public.preguntas (oposicion_id, origen);

create table if not exists public.imagenes (
  id         uuid primary key default gen_random_uuid(),
  tema_id    uuid not null references public.temas(id) on delete cascade,
  fichero    text not null,
  titulo     text,
  alt        text,
  bloque     integer,
  orden      integer not null default 0,
  created_at timestamptz not null default now()
);

create unique index if not exists imagenes_tema_fichero_key
  on public.imagenes (tema_id, fichero);


-- ============================================================================
-- 4 · PROGRESO DEL ALUMNO
-- Una fila por alumno y pregunta, con contadores. No guarda un histórico de
-- cada intento: con 40.080 preguntas y varios repasos, eso se dispara.
-- ============================================================================

create table if not exists public.progreso (
  alumno_id        uuid not null references auth.users(id) on delete cascade,
  pregunta_id      text not null references public.preguntas(id) on delete cascade,
  tema_id          uuid references public.temas(id) on delete cascade,
  aciertos         integer not null default 0,
  fallos           integer not null default 0,
  ultimo_acierto   boolean,
  ultima_respuesta text,
  actualizado_en   timestamptz not null default now(),
  primary key (alumno_id, pregunta_id)
);

create index if not exists progreso_alumno_tema_idx
  on public.progreso (alumno_id, tema_id);


-- ============================================================================
-- 5 · FUNCIONES
-- ============================================================================

-- Marca updated_at en cada modificación
create or replace function public.marcar_actualizacion()
returns trigger
language plpgsql
as $$
begin
  new.updated_at := now();
  return new;
end;
$$;

do $$
declare t text;
begin
  foreach t in array array['alumnos','temas','contenidos'] loop
    execute format('drop trigger if exists %I on public.%I', 'set_updated_at_'||t, t);
    execute format(
      'create trigger %I before update on public.%I
       for each row execute function public.marcar_actualizacion()',
      'set_updated_at_'||t, t);
  end loop;
end $$;


-- ¿Puede este alumno ver este tema?
-- El goteo NO se almacena: se calcula desde fecha_alta cada vez que se pregunta.
-- Así no hay tareas mensuales que mantener ni desbloqueos que falsificar.
create or replace function public.tiene_acceso_tema(p_tema_id uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1
    from public.temas t
    where t.id = p_tema_id
      and t.publicado
      and (
        t.es_gratuito
        or exists (
          select 1
          from public.entitlements e
          join public.planes p on p.id = e.plan_id
          where e.alumno_id = auth.uid()
            and e.oposicion_id = t.oposicion_id
            and e.estado = 'activo'
            and (
              p.temas_por_mes is null            -- plan sin goteo: todo abierto
              or t.orden <= p.temas_por_mes * (
                   1 + extract(year  from age(now(), e.fecha_alta)) * 12
                     + extract(month from age(now(), e.fecha_alta))
                 )
            )
        )
      )
  );
$$;


-- ¿Tiene el alumno algún derecho activo sobre esta oposición?
-- Se usa para los exámenes oficiales, que no cuelgan de ningún tema.
create or replace function public.tiene_acceso_oposicion(p_oposicion_id text)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1 from public.entitlements e
    where e.alumno_id = auth.uid()
      and e.oposicion_id = p_oposicion_id
      and e.estado = 'activo'
  );
$$;


-- Al registrarse un usuario, se le crea su ficha de alumno
create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  insert into public.alumnos (id, email, nombre)
  values (
    new.id,
    new.email,
    coalesce(new.raw_user_meta_data ->> 'full_name', new.raw_user_meta_data ->> 'name')
  )
  on conflict (id) do nothing;
  return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();


-- ============================================================================
-- 6 · SEGURIDAD (RLS)
-- Se borran todas las políticas anteriores de estas tablas y se recrean, para
-- que este archivo sea la única verdad y no queden políticas sueltas de
-- sesiones anteriores.
-- ============================================================================

do $$
declare r record;
begin
  for r in
    select schemaname, tablename, policyname
    from pg_policies
    where schemaname = 'public'
      and tablename in ('oposiciones','convocatorias','temas','alumnos','planes',
                        'entitlements','contenidos','preguntas','imagenes','progreso')
  loop
    execute format('drop policy %I on %I.%I', r.policyname, r.schemaname, r.tablename);
  end loop;
end $$;

alter table public.oposiciones   enable row level security;
alter table public.convocatorias enable row level security;
alter table public.temas         enable row level security;
alter table public.alumnos       enable row level security;
alter table public.planes        enable row level security;
alter table public.entitlements  enable row level security;
alter table public.contenidos    enable row level security;
alter table public.preguntas     enable row level security;
alter table public.imagenes      enable row level security;
alter table public.progreso      enable row level security;

-- --- Catálogo: visible para cualquiera, también sin registrarse -------------
create policy "catalogo de oposiciones visible"
  on public.oposiciones for select to anon, authenticated
  using (activa);

create policy "convocatorias visibles"
  on public.convocatorias for select to anon, authenticated
  using (true);

create policy "planes visibles"
  on public.planes for select to anon, authenticated
  using (activo);

-- El índice del temario se ve entero (títulos), el contenido no.
create policy "indice de temas visible"
  on public.temas for select to anon, authenticated
  using (publicado);

-- --- Datos del propio alumno -----------------------------------------------
create policy "el alumno ve su ficha"
  on public.alumnos for select to authenticated
  using (id = auth.uid());

create policy "el alumno edita su ficha"
  on public.alumnos for update to authenticated
  using (id = auth.uid()) with check (id = auth.uid());

-- Sin política de INSERT ni de UPDATE: los derechos de acceso solo los concede
-- el service_role desde el webhook de Stripe. Un alumno no puede regalarse nada.
create policy "el alumno ve sus derechos"
  on public.entitlements for select to authenticated
  using (alumno_id = auth.uid());

-- --- Contenido: solo si se tiene acceso al tema -----------------------------
create policy "contenido solo con acceso"
  on public.contenidos for select to authenticated
  using (public.tiene_acceso_tema(tema_id));

create policy "imagenes solo con acceso"
  on public.imagenes for select to authenticated
  using (public.tiene_acceso_tema(tema_id));

create policy "preguntas solo con acceso"
  on public.preguntas for select to authenticated
  using (
    case
      when tema_id is not null then public.tiene_acceso_tema(tema_id)
      else public.tiene_acceso_oposicion(oposicion_id)   -- exámenes oficiales
    end
  );

-- --- Progreso: cada alumno, el suyo ----------------------------------------
create policy "el alumno ve su progreso"
  on public.progreso for select to authenticated
  using (alumno_id = auth.uid());

create policy "el alumno anota su progreso"
  on public.progreso for insert to authenticated
  with check (alumno_id = auth.uid());

create policy "el alumno actualiza su progreso"
  on public.progreso for update to authenticated
  using (alumno_id = auth.uid()) with check (alumno_id = auth.uid());

create policy "el alumno borra su progreso"
  on public.progreso for delete to authenticated
  using (alumno_id = auth.uid());


-- ============================================================================
-- 6 bis · PERMISOS
-- El RLS decide QUÉ filas ve cada uno, pero antes hay que dar permiso sobre la
-- tabla. Supabase suele hacerlo solo al crear tablas desde su panel; si la
-- opción "exponer tablas nuevas automáticamente" está desactivada, o si la
-- tabla se creó por SQL, hay que concederlo a mano. Sin esto, la aplicación
-- responde "permission denied" aunque las políticas sean correctas.
-- ============================================================================

grant usage on schema public to anon, authenticated, service_role;

grant select on public.oposiciones, public.convocatorias, public.planes, public.temas
  to anon, authenticated;

grant select on public.contenidos, public.preguntas, public.imagenes, public.entitlements
  to authenticated;

grant select, update on public.alumnos to authenticated;

grant select, insert, update, delete on public.progreso to authenticated;

grant all on all tables in schema public to service_role;

grant execute on function public.tiene_acceso_tema(uuid)      to anon, authenticated;
grant execute on function public.tiene_acceso_oposicion(text) to anon, authenticated;


-- ============================================================================
-- 7 · DATOS DE CATÁLOGO
-- ============================================================================

insert into public.oposiciones (id, display_name, orden) values
  ('policia-nacional', 'Policía Nacional · Escala Básica', 1),
  ('guardia-civil',    'Guardia Civil · Cabos y Guardias', 2)
on conflict (id) do update
  set display_name = excluded.display_name,
      orden        = excluded.orden;

-- Los planes se insertan cuando estén decididos los precios.
-- Plantilla, con los importes a cero para que no se publique nada por error:
--
-- insert into public.planes (id, oposicion_id, nombre, tipo, temas_por_mes,
--                            convocatorias_incluidas, precio_centimos, activo)
-- values
--   ('pn-free',       'policia-nacional', 'Gratuito',   'free',       null, null,    0, true),
--   ('pn-mensual',    'policia-nacional', 'Mensual',    'mensual',       4, null,    0, false),
--   ('pn-trimestral', 'policia-nacional', 'Trimestral', 'trimestral',    4, null,    0, false),
--   ('pn-completa',   'policia-nacional', 'Completa',   'completa',   null,    2,    0, false)
-- on conflict (id) do nothing;


-- ============================================================================
-- 8 · COMPROBACIÓN
-- ============================================================================

select
  (select count(*) from public.oposiciones) as oposiciones,
  (select count(*) from public.temas)       as temas,
  (select count(*) from public.contenidos)  as contenidos,
  (select count(*) from public.preguntas)   as preguntas,
  (select count(*) from public.imagenes)    as imagenes,
  (select count(*) from pg_policies where schemaname = 'public') as politicas;
