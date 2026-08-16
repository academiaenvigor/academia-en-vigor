# TEMA 38 · FUNDAMENTOS DE SISTEMAS OPERATIVOS: FUNCIONES DE UN SISTEMA OPERATIVO. TIPOLOGÍAS: MS-DOS, UNIX, LINUX, WINDOWS Y MACOS. SISTEMAS OPERATIVOS MÓVILES: IOS Y ANDROID. SISTEMAS DE ALMACENAMIENTO. SISTEMAS DE ARCHIVOS.

**Policía Nacional · Método VIGOR · PARTE**
**Versión de contenido:** 1.0.0
**Estado editorial:** approved_internal · **Publicación:** not_published

# Mapa del tema

El Tema 38 se estudia en diez partes: fundamentos; funciones; MS-DOS; UNIX/POSIX; Linux; Windows; macOS; iOS y Android; sistemas de almacenamiento; y sistemas de archivos.

# Contenido

## 01. Alcance oficial del Tema 38

**Idea de control:** El programa exige fundamentos y funciones de los sistemas operativos.

- El programa exige fundamentos y funciones de los sistemas operativos.
- Las tipologías expresamente citadas son MS-DOS, UNIX, Linux, Windows y macOS.
- El epígrafe incorpora los sistemas operativos móviles iOS y Android.
- El programa se completa con sistemas de almacenamiento y sistemas de archivos.

<!-- VISUAL:t38-01-alcance-oficial-del-tema-38.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-01-alcance-oficial-del-tema-38.webp" alt="Alcance oficial del Tema 38" width="820">
</p>
<p align="center"><em>Infografía: Alcance oficial del Tema 38.</em></p>

<!-- FUENTE: CONVOCATORIA-PN-2026-T38 -->

## 02. Hardware, software y firmware

**Idea de control:** El hardware reúne los componentes físicos que ejecutan, almacenan o transfieren información.

- El hardware reúne los componentes físicos que ejecutan, almacenan o transfieren información.
- El software es el conjunto de instrucciones y datos que se ejecutan sobre el hardware.
- El firmware es software estrechamente ligado a un dispositivo y almacenado normalmente en memoria no volátil.
- El sistema operativo coordina hardware, aplicaciones, datos y usuarios sin confundirse con ninguno de ellos.

<!-- VISUAL:t38-02-hardware-software-y-firmware.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-02-hardware-software-y-firmware.webp" alt="Hardware, software y firmware" width="820">
</p>
<p align="center"><em>Infografía: Hardware, software y firmware.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 03. Arquitectura de programa almacenado

**Idea de control:** En una arquitectura de programa almacenado, instrucciones y datos se conservan en memoria accesible al procesador.

- En una arquitectura de programa almacenado, instrucciones y datos se conservan en memoria accesible al procesador.
- La unidad de control obtiene y decodifica instrucciones, y coordina su ejecución.
- La ALU realiza operaciones aritméticas y lógicas requeridas por las instrucciones.
- Los buses y controladores permiten intercambiar direcciones, datos y señales de control entre componentes.

<!-- VISUAL:t38-03-arquitectura-de-programa-almacenado.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-03-arquitectura-de-programa-almacenado.webp" alt="Arquitectura de programa almacenado" width="820">
</p>
<p align="center"><em>Infografía: Arquitectura de programa almacenado.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 04. CPU, núcleos, hilos y caché

**Idea de control:** La CPU ejecuta instrucciones y puede integrar uno o varios núcleos de procesamiento.

- La CPU ejecuta instrucciones y puede integrar uno o varios núcleos de procesamiento.
- Un núcleo físico no es idéntico a un hilo lógico ofrecido por el hardware.
- Los registros guardan operandos, direcciones y estado inmediato de la ejecución.
- La memoria caché reduce la latencia media al conservar datos e instrucciones próximos al procesador.

<!-- VISUAL:t38-il-04-cpu-nucleos-hilos-y-cache.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-04-cpu-nucleos-hilos-y-cache.webp" alt="CPU, núcleos, hilos y caché" width="820">
</p>
<p align="center"><em>Infografía: CPU, núcleos, hilos y caché.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 05. Jerarquía de memoria

**Idea de control:** Registros y cachés son muy rápidos y de capacidad limitada frente a la memoria principal.

- Registros y cachés son muy rápidos y de capacidad limitada frente a la memoria principal.
- La RAM mantiene temporalmente código y datos en uso y pierde normalmente su contenido sin alimentación.
- El almacenamiento secundario conserva información de forma no volátil.
- La memoria virtual no convierte el almacenamiento en RAM física ni elimina su diferencia de velocidad.

<!-- VISUAL:t38-il-05-jerarquia-de-memoria.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-05-jerarquia-de-memoria.webp" alt="Jerarquía de memoria" width="820">
</p>
<p align="center"><em>Infografía: Jerarquía de memoria.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 06. Bit, byte y prefijos de capacidad

**Idea de control:** El bit es una unidad binaria y el byte agrupa ocho bits.

- El bit es una unidad binaria y el byte agrupa ocho bits.
- La b minúscula suele representar bits y la B mayúscula bytes.
- Los prefijos SI kB, MB y GB usan potencias de mil.
- Los prefijos binarios KiB, MiB y GiB usan potencias de 1024 y no deben confundirse con los prefijos SI.

<!-- VISUAL:t38-06-bit-byte-y-prefijos-de-capacidad.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-06-bit-byte-y-prefijos-de-capacidad.webp" alt="Bit, byte y prefijos de capacidad" width="820">
</p>
<p align="center"><em>Infografía: Bit, byte y prefijos de capacidad.</em></p>

<!-- FUENTE: NVME-SPEC-T38 -->

## 07. Entrada, salida y periféricos

**Idea de control:** Un dispositivo de entrada aporta datos o señales al sistema.

- Un dispositivo de entrada aporta datos o señales al sistema.
- Un dispositivo de salida presenta o transmite resultados del sistema.
- Un mismo dispositivo puede realizar funciones de entrada y salida.
- El sistema operativo accede a los periféricos mediante controladores y mecanismos de entrada/salida.

<!-- VISUAL:t38-07-entrada-salida-y-perifericos.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-07-entrada-salida-y-perifericos.webp" alt="Entrada, salida y periféricos" width="820">
</p>
<p align="center"><em>Infografía: Entrada, salida y periféricos.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 08. Arranque: firmware, cargador y núcleo

**Idea de control:** El firmware inicializa componentes básicos y localiza un mecanismo de arranque.

- El firmware inicializa componentes básicos y localiza un mecanismo de arranque.
- El cargador de arranque prepara el entorno y transfiere el control al núcleo del sistema operativo.
- El núcleo inicializa subsistemas como memoria, planificación, dispositivos y sistema de archivos raíz.
- El arranque seguro añade verificaciones de integridad o autenticidad, pero no es sinónimo de cifrado de todos los datos.

<!-- VISUAL:t38-08-arranque-firmware-cargador-y-nucleo.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-08-arranque-firmware-cargador-y-nucleo.webp" alt="Arranque: firmware, cargador y núcleo" width="820">
</p>
<p align="center"><em>Infografía: Arranque: firmware, cargador y núcleo.</em></p>

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 09. Sistema operativo como gestor de recursos

**Idea de control:** El sistema operativo administra procesador, memoria, dispositivos y almacenamiento.

- El sistema operativo administra procesador, memoria, dispositivos y almacenamiento.
- Proporciona abstracciones que evitan que cada aplicación gestione directamente el hardware.
- Arbitra recursos compartidos para reducir conflictos entre programas y usuarios.
- Ofrece servicios comunes para ejecutar aplicaciones y conservar información.

<!-- VISUAL:t38-09-sistema-operativo-como-gestor-de-recursos.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-09-sistema-operativo-como-gestor-de-recursos.webp" alt="Sistema operativo como gestor de recursos" width="820">
</p>
<p align="center"><em>Infografía: Sistema operativo como gestor de recursos.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 10. Núcleo, modo usuario y llamadas al sistema

**Idea de control:** El núcleo ejecuta funciones privilegiadas y mantiene el control de recursos críticos.

- El núcleo ejecuta funciones privilegiadas y mantiene el control de recursos críticos.
- Las aplicaciones ordinarias se ejecutan normalmente con privilegios restringidos en modo usuario.
- Una llamada al sistema solicita al núcleo un servicio mediante una interfaz definida.
- Separar privilegios limita el daño directo que puede causar un proceso de usuario defectuoso.

<!-- VISUAL:t38-il-10-nucleo-modo-usuario-y-llamadas-al-sistema.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-10-nucleo-modo-usuario-y-llamadas-al-sistema.webp" alt="Núcleo, modo usuario y llamadas al sistema" width="820">
</p>
<p align="center"><em>Infografía: Núcleo, modo usuario y llamadas al sistema.</em></p>

<!-- FUENTE: MS-WINDOWS-INTERNALS-T38 -->

## 11. Programa, proceso e imagen ejecutable

**Idea de control:** Un programa es código y datos preparados para ejecutarse.

- Un programa es código y datos preparados para ejecutarse.
- Un proceso es una instancia en ejecución con estado y recursos asociados.
- Varias instancias del mismo programa pueden originar procesos distintos.
- El sistema identifica y administra procesos sin confundirlos con el archivo ejecutable que los inició.

<!-- VISUAL:t38-11-programa-proceso-e-imagen-ejecutable.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-11-programa-proceso-e-imagen-ejecutable.webp" alt="Programa, proceso e imagen ejecutable" width="820">
</p>
<p align="center"><em>Infografía: Programa, proceso e imagen ejecutable.</em></p>

<!-- FUENTE: POSIX-2024-T38 -->

## 12. Estados y ciclo de vida de un proceso

**Idea de control:** Un proceso listo puede ejecutar cuando el planificador le asigne procesador.

- Un proceso listo puede ejecutar cuando el planificador le asigne procesador.
- Un proceso en ejecución está usando una CPU o núcleo lógico en ese instante.
- Un proceso bloqueado o en espera aguarda un evento o recurso antes de continuar.
- La terminación libera o transfiere los recursos conforme a las reglas del sistema.

<!-- VISUAL:t38-il-12-estados-y-ciclo-de-vida-de-un-proceso.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-12-estados-y-ciclo-de-vida-de-un-proceso.webp" alt="Estados y ciclo de vida de un proceso" width="820">
</p>
<p align="center"><em>Infografía: Estados y ciclo de vida de un proceso.</em></p>

<!-- FUENTE: POSIX-2024-T38 -->

## 13. Hilos y recursos compartidos

**Idea de control:** Un hilo es una secuencia de ejecución planificable dentro de un proceso.

- Un hilo es una secuencia de ejecución planificable dentro de un proceso.
- Los hilos de un proceso comparten habitualmente el espacio de direcciones y otros recursos.
- Cada hilo conserva contexto propio, como registros y pila de ejecución.
- Compartir memoria facilita cooperación, pero exige sincronización frente a accesos concurrentes.

<!-- VISUAL:t38-13-hilos-y-recursos-compartidos.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-13-hilos-y-recursos-compartidos.webp" alt="Hilos y recursos compartidos" width="820">
</p>
<p align="center"><em>Infografía: Hilos y recursos compartidos.</em></p>

<!-- FUENTE: MS-WINDOWS-INTERNALS-T38 -->

## 14. Planificación de CPU

**Idea de control:** El planificador decide qué tarea ejecutable utiliza la CPU en cada momento.

- El planificador decide qué tarea ejecutable utiliza la CPU en cada momento.
- La política puede considerar prioridad, equidad, latencia, plazos o consumo energético.
- El cambio de contexto sustituye el estado de ejecución de una tarea por el de otra.
- Una mayor prioridad no implica necesariamente monopolio ilimitado del procesador.

<!-- VISUAL:t38-14-planificacion-de-cpu.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-14-planificacion-de-cpu.webp" alt="Planificación de CPU" width="820">
</p>
<p align="center"><em>Infografía: Planificación de CPU.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 15. Multiprogramación, multitarea y multiprocesamiento

**Idea de control:** La multiprogramación mantiene varios trabajos preparados para aprovechar mejor la CPU.

- La multiprogramación mantiene varios trabajos preparados para aprovechar mejor la CPU.
- La multitarea alterna o distribuye la ejecución de varias tareas de forma gestionada.
- El multiprocesamiento utiliza más de una unidad de procesamiento.
- La concurrencia permite progresos solapados; el paralelismo implica ejecución simultánea real.

<!-- VISUAL:t38-15-multiprogramacion-multitarea-y-multiprocesamiento.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-15-multiprogramacion-multitarea-y-multiprocesamiento.webp" alt="Multiprogramación, multitarea y multiprocesamiento" width="820">
</p>
<p align="center"><em>Infografía: Multiprogramación, multitarea y multiprocesamiento.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 16. Sincronización y condiciones de carrera

**Idea de control:** Existe condición de carrera cuando el resultado depende de un orden no controlado entre ejecuciones concurrentes.

- Existe condición de carrera cuando el resultado depende de un orden no controlado entre ejecuciones concurrentes.
- La exclusión mutua protege secciones críticas frente a accesos simultáneos incompatibles.
- Semáforos, mutex y otros mecanismos coordinan tareas con propiedades diferentes.
- Un interbloqueo puede surgir cuando varias tareas esperan recursos retenidos entre sí.

<!-- VISUAL:t38-il-16-sincronizacion-y-condiciones-de-carrera.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-16-sincronizacion-y-condiciones-de-carrera.webp" alt="Sincronización y condiciones de carrera" width="820">
</p>
<p align="center"><em>Infografía: Sincronización y condiciones de carrera.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 17. Comunicación entre procesos

**Idea de control:** La comunicación entre procesos permite intercambiar datos o señales entre ejecuciones separadas.

- La comunicación entre procesos permite intercambiar datos o señales entre ejecuciones separadas.
- Tuberías, colas, memoria compartida, señales y sockets son mecanismos de IPC.
- La memoria compartida puede ser eficiente, pero requiere coordinación de acceso.
- Un socket puede comunicar procesos del mismo equipo o de equipos distintos según su dominio y protocolo.

<!-- VISUAL:t38-17-comunicacion-entre-procesos.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-17-comunicacion-entre-procesos.webp" alt="Comunicación entre procesos" width="820">
</p>
<p align="center"><em>Infografía: Comunicación entre procesos.</em></p>

<!-- FUENTE: POSIX-2024-T38 -->

## 18. Gestión de memoria

**Idea de control:** El sistema operativo asigna memoria a procesos y recupera regiones cuando dejan de utilizarse.

- El sistema operativo asigna memoria a procesos y recupera regiones cuando dejan de utilizarse.
- La protección de memoria evita accesos no autorizados entre espacios de direcciones.
- La traducción de direcciones permite separar la visión virtual del proceso de la ubicación física.
- La fragmentación puede ser interna o externa y no describe necesariamente archivos del disco.

<!-- VISUAL:t38-18-gestion-de-memoria.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-18-gestion-de-memoria.webp" alt="Gestión de memoria" width="820">
</p>
<p align="center"><em>Infografía: Gestión de memoria.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 19. Memoria virtual y paginación

**Idea de control:** La memoria virtual proporciona a cada proceso un espacio de direcciones abstracto.

- La memoria virtual proporciona a cada proceso un espacio de direcciones abstracto.
- La paginación divide el espacio virtual y la memoria física en unidades gestionables.
- Una falta de página ocurre cuando la traducción o el contenido requerido no está disponible como necesita la CPU.
- El intercambio con almacenamiento es mucho más lento que acceder a RAM y su uso excesivo degrada el rendimiento.

<!-- VISUAL:t38-il-19-memoria-virtual-y-paginacion.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-19-memoria-virtual-y-paginacion.webp" alt="Memoria virtual y paginación" width="820">
</p>
<p align="center"><em>Infografía: Memoria virtual y paginación.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 20. Gestión de archivos y directorios

**Idea de control:** El sistema operativo ofrece operaciones para crear, abrir, leer, escribir, renombrar y eliminar archivos.

- El sistema operativo ofrece operaciones para crear, abrir, leer, escribir, renombrar y eliminar archivos.
- Los directorios organizan nombres y referencias dentro de una jerarquía.
- Los metadatos describen propiedades como tipo, tamaño, marcas temporales, propietario o permisos.
- Eliminar una referencia de directorio no equivale necesariamente a sobrescribir de inmediato los datos físicos.

<!-- VISUAL:t38-20-gestion-de-archivos-y-directorios.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-20-gestion-de-archivos-y-directorios.webp" alt="Gestión de archivos y directorios" width="820">
</p>
<p align="center"><em>Infografía: Gestión de archivos y directorios.</em></p>

<!-- FUENTE: POSIX-2024-T38 -->

## 21. Dispositivos, controladores y entrada/salida

**Idea de control:** Un controlador traduce operaciones del sistema a interacciones adecuadas con un dispositivo.

- Un controlador traduce operaciones del sistema a interacciones adecuadas con un dispositivo.
- Las interrupciones permiten notificar eventos sin sondear continuamente todos los dispositivos.
- El almacenamiento en búfer suaviza diferencias de velocidad entre productores y consumidores.
- La cola de entrada/salida permite ordenar y combinar peticiones según la política del sistema.

<!-- VISUAL:t38-21-dispositivos-controladores-y-entrada-salida.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-21-dispositivos-controladores-y-entrada-salida.webp" alt="Dispositivos, controladores y entrada/salida" width="820">
</p>
<p align="center"><em>Infografía: Dispositivos, controladores y entrada/salida.</em></p>

<!-- FUENTE: MS-WINDOWS-INTERNALS-T38 -->

## 22. Interfaz de línea de comandos, shell y GUI

**Idea de control:** Una interfaz de línea de comandos recibe instrucciones textuales.

- Una interfaz de línea de comandos recibe instrucciones textuales.
- Una shell interpreta órdenes y puede combinar programas mediante redirecciones y tuberías.
- Una interfaz gráfica utiliza ventanas, iconos, menús y otros controles visuales.
- CLI y GUI pueden coexistir y utilizar los mismos servicios del sistema operativo.

<!-- VISUAL:t38-il-22-interfaz-de-linea-de-comandos-shell-y-gui.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-22-interfaz-de-linea-de-comandos-shell-y-gui.webp" alt="Interfaz de línea de comandos, shell y GUI" width="820">
</p>
<p align="center"><em>Infografía: Interfaz de línea de comandos, shell y GUI.</em></p>

<!-- FUENTE: POSIX-2024-T38 -->

## 23. Usuarios, autenticación y autorización

**Idea de control:** La autenticación comprueba una identidad declarada.

- La autenticación comprueba una identidad declarada.
- La autorización decide qué acciones puede realizar una identidad autenticada.
- Las cuentas, grupos y roles permiten asignar privilegios sin concederlos de forma indiscriminada.
- El principio de mínimo privilegio limita cada usuario o proceso a los permisos necesarios.

<!-- VISUAL:t38-23-usuarios-autenticacion-y-autorizacion.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-23-usuarios-autenticacion-y-autorizacion.webp" alt="Usuarios, autenticación y autorización" width="820">
</p>
<p align="center"><em>Infografía: Usuarios, autenticación y autorización.</em></p>

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 24. Protección, aislamiento y auditoría

**Idea de control:** El aislamiento de procesos reduce accesos directos entre aplicaciones.

- El aislamiento de procesos reduce accesos directos entre aplicaciones.
- Los permisos y controles de acceso protegen objetos según identidad y política.
- El registro de eventos permite reconstruir actividad, aunque no evita por sí solo un incidente.
- Actualizaciones, firma de código, cifrado y copias de seguridad resuelven riesgos distintos y se complementan.

<!-- VISUAL:t38-24-proteccion-aislamiento-y-auditoria.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-24-proteccion-aislamiento-y-auditoria.webp" alt="Protección, aislamiento y auditoría" width="820">
</p>
<p align="center"><em>Infografía: Protección, aislamiento y auditoría.</em></p>

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 25. Errores, excepciones y recuperación

**Idea de control:** El sistema operativo gestiona excepciones del procesador y errores comunicados por hardware o software.

- El sistema operativo gestiona excepciones del procesador y errores comunicados por hardware o software.
- Un fallo de una aplicación no debería comprometer por diseño todo el sistema.
- La recuperación puede incluir reintentos, terminación controlada, reparación del sistema de archivos o restauración.
- La tolerancia a fallos reduce impacto, pero no convierte ningún sistema en infalible.

<!-- VISUAL:t38-25-errores-excepciones-y-recuperacion.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-25-errores-excepciones-y-recuperacion.webp" alt="Errores, excepciones y recuperación" width="820">
</p>
<p align="center"><em>Infografía: Errores, excepciones y recuperación.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 26. MS-DOS: naturaleza y contexto histórico

**Idea de control:** MS-DOS es una familia histórica de sistemas operativos de disco desarrollada para ordenadores personales compatibles.

- MS-DOS es una familia histórica de sistemas operativos de disco desarrollada para ordenadores personales compatibles.
- Su interacción característica es textual mediante un intérprete de comandos.
- Las versiones clásicas fueron diseñadas para entornos de recursos muy limitados frente a sistemas actuales.
- Estudiar MS-DOS sirve para comprender rutas, unidades, comandos y FAT, no para presentarlo como plataforma moderna segura.

<!-- VISUAL:t38-26-ms-dos-naturaleza-y-contexto-historico.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-26-ms-dos-naturaleza-y-contexto-historico.webp" alt="MS-DOS: naturaleza y contexto histórico" width="820">
</p>
<p align="center"><em>Infografía: MS-DOS: naturaleza y contexto histórico.</em></p>

<!-- FUENTE: MS-DOS-SOURCE-T38 -->

## 27. Arquitectura y límites clásicos de MS-DOS

**Idea de control:** El MS-DOS clásico trabajaba sobre la arquitectura x86 en modo real de sus primeras generaciones.

- El MS-DOS clásico trabajaba sobre la arquitectura x86 en modo real de sus primeras generaciones.
- Carecía del aislamiento y la protección de memoria propios de sistemas modernos.
- Su modelo habitual era monousuario y de una tarea principal, aunque existieron técnicas y extensiones residentes.
- Los programas accedían al sistema mediante servicios de DOS, BIOS y, en ciertos casos, acceso directo al hardware.

<!-- VISUAL:t38-27-arquitectura-y-limites-clasicos-de-ms-dos.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-27-arquitectura-y-limites-clasicos-de-ms-dos.webp" alt="Arquitectura y límites clásicos de MS-DOS" width="820">
</p>
<p align="center"><em>Infografía: Arquitectura y límites clásicos de MS-DOS.</em></p>

<!-- FUENTE: MS-DOS-SOURCE-T38 -->

## 28. Intérprete y comandos de MS-DOS

**Idea de control:** COMMAND.COM actuaba como intérprete de comandos en versiones clásicas de MS-DOS.

- COMMAND.COM actuaba como intérprete de comandos en versiones clásicas de MS-DOS.
- Los comandos internos formaban parte del intérprete y los externos residían en archivos ejecutables separados.
- DIR, CD, COPY, DEL y REN representan operaciones habituales sobre archivos y directorios.
- La existencia histórica de un comando no garantiza idéntica sintaxis o comportamiento en la consola de Windows actual.

<!-- VISUAL:t38-28-interprete-y-comandos-de-ms-dos.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-28-interprete-y-comandos-de-ms-dos.webp" alt="Intérprete y comandos de MS-DOS" width="820">
</p>
<p align="center"><em>Infografía: Intérprete y comandos de MS-DOS.</em></p>

<!-- FUENTE: MS-DOS-SOURCE-T38 -->

## 29. Unidades, rutas y nombres en MS-DOS

**Idea de control:** MS-DOS identifica habitualmente volúmenes mediante letras seguidas de dos puntos.

- MS-DOS identifica habitualmente volúmenes mediante letras seguidas de dos puntos.
- La barra inversa separa componentes de ruta y la raíz se representa desde la unidad activa.
- El directorio actual puede ser distinto en cada unidad según el entorno DOS.
- Las primeras convenciones FAT usaron nombres cortos 8.3; las extensiones posteriores no deben proyectarse sin fecha sobre todas las versiones.

<!-- VISUAL:t38-29-unidades-rutas-y-nombres-en-ms-dos.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-29-unidades-rutas-y-nombres-en-ms-dos.webp" alt="Unidades, rutas y nombres en MS-DOS" width="820">
</p>
<p align="center"><em>Infografía: Unidades, rutas y nombres en MS-DOS.</em></p>

<!-- FUENTE: MS-DOS-SOURCE-T38 -->

## 30. MS-DOS, FAT y arranque

**Idea de control:** MS-DOS utilizó variantes de FAT para organizar archivos en volúmenes.

- MS-DOS utilizó variantes de FAT para organizar archivos en volúmenes.
- El sector de arranque y los archivos del sistema participaban en la carga de versiones clásicas.
- La tabla FAT registra cadenas de clústeres y estado de asignación.
- FAT aporta compatibilidad y sencillez, pero no ofrece el modelo de permisos y diario de NTFS o ext4.

<!-- VISUAL:t38-il-30-ms-dos-fat-y-arranque.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-30-ms-dos-fat-y-arranque.webp" alt="MS-DOS, FAT y arranque" width="820">
</p>
<p align="center"><em>Infografía: MS-DOS, FAT y arranque.</em></p>

<!-- FUENTE: MS-DOS-SOURCE-T38 -->

## 31. UNIX: origen y principios

**Idea de control:** UNIX nació como una familia de sistemas multiusuario y multitarea.

- UNIX nació como una familia de sistemas multiusuario y multitarea.
- Su diseño favorece herramientas pequeñas que pueden combinarse mediante interfaces comunes.
- La jerarquía de archivos parte de una raíz única.
- El término UNIX no debe usarse como sinónimo automático de cualquier sistema parecido a Unix.

<!-- VISUAL:t38-31-unix-origen-y-principios.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-31-unix-origen-y-principios.webp" alt="UNIX: origen y principios" width="820">
</p>
<p align="center"><em>Infografía: UNIX: origen y principios.</em></p>

<!-- FUENTE: POSIX-2024-T38 -->

## 32. Núcleo, shell y utilidades UNIX

**Idea de control:** El núcleo gestiona procesos, memoria, dispositivos y sistemas de archivos.

- El núcleo gestiona procesos, memoria, dispositivos y sistemas de archivos.
- La shell interpreta el lenguaje de órdenes y lanza programas.
- Las utilidades realizan tareas concretas y se coordinan mediante archivos, argumentos, tuberías y redirecciones.
- La shell es un programa de usuario y no debe confundirse con el núcleo.

<!-- VISUAL:t38-32-nucleo-shell-y-utilidades-unix.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-32-nucleo-shell-y-utilidades-unix.webp" alt="Núcleo, shell y utilidades UNIX" width="820">
</p>
<p align="center"><em>Infografía: Núcleo, shell y utilidades UNIX.</em></p>

<!-- FUENTE: POSIX-2024-T38 -->

## 33. Jerarquía, raíz y montaje en UNIX

**Idea de control:** La barra inclinada representa la raíz y separa componentes de una ruta POSIX.

- La barra inclinada representa la raíz y separa componentes de una ruta POSIX.
- Una ruta absoluta parte de la raíz y una relativa se interpreta desde el directorio de trabajo.
- Montar incorpora un sistema de archivos en un punto de la jerarquía.
- Los dispositivos pueden exponerse mediante archivos especiales sin que dispositivo y archivo ordinario sean idénticos.

<!-- VISUAL:t38-33-jerarquia-raiz-y-montaje-en-unix.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-33-jerarquia-raiz-y-montaje-en-unix.webp" alt="Jerarquía, raíz y montaje en UNIX" width="820">
</p>
<p align="center"><em>Infografía: Jerarquía, raíz y montaje en UNIX.</em></p>

<!-- FUENTE: POSIX-2024-T38 -->

## 34. Procesos UNIX: fork, exec y wait

**Idea de control:** fork crea un nuevo proceso a partir del contexto del proceso llamante.

- fork crea un nuevo proceso a partir del contexto del proceso llamante.
- exec sustituye la imagen del proceso por un nuevo programa sin crear por sí solo otro proceso.
- wait permite recoger el estado de terminación de procesos hijos.
- La combinación fork y exec explica un patrón clásico de lanzamiento de programas en sistemas UNIX.

<!-- VISUAL:t38-34-procesos-unix-fork-exec-y-wait.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-34-procesos-unix-fork-exec-y-wait.webp" alt="Procesos UNIX: fork, exec y wait" width="820">
</p>
<p align="center"><em>Infografía: Procesos UNIX: fork, exec y wait.</em></p>

<!-- FUENTE: POSIX-2024-T38 -->

## 35. Usuarios, grupos y permisos POSIX

**Idea de control:** Los permisos clásicos distinguen lectura, escritura y ejecución.

- Los permisos clásicos distinguen lectura, escritura y ejecución.
- Las clases tradicionales son propietario, grupo y otros.
- En un directorio, lectura, escritura y ejecución tienen efectos diferentes de los que tienen sobre un archivo ordinario.
- El usuario con privilegios administrativos no elimina la necesidad de aplicar mínimo privilegio.

<!-- VISUAL:t38-il-35-usuarios-grupos-y-permisos-posix.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-35-usuarios-grupos-y-permisos-posix.webp" alt="Usuarios, grupos y permisos POSIX" width="820">
</p>
<p align="center"><em>Infografía: Usuarios, grupos y permisos POSIX.</em></p>

<!-- FUENTE: POSIX-2024-T38 -->

## 36. Tuberías, redirecciones y descriptores

**Idea de control:** La entrada estándar, la salida estándar y el error estándar son flujos diferenciados.

- La entrada estándar, la salida estándar y el error estándar son flujos diferenciados.
- Una tubería conecta normalmente la salida de un proceso con la entrada de otro.
- La redirección cambia el origen o destino de un flujo sin modificar necesariamente el programa.
- Un descriptor de archivo es un identificador de proceso para un archivo abierto u otro objeto de entrada/salida.

<!-- VISUAL:t38-il-36-tuberias-redirecciones-y-descriptores.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-36-tuberias-redirecciones-y-descriptores.webp" alt="Tuberías, redirecciones y descriptores" width="820">
</p>
<p align="center"><em>Infografía: Tuberías, redirecciones y descriptores.</em></p>

<!-- FUENTE: POSIX-2024-T38 -->

## 37. POSIX, UNIX y sistemas tipo Unix

**Idea de control:** POSIX define interfaces y comportamientos portables para sistemas compatibles.

- POSIX define interfaces y comportamientos portables para sistemas compatibles.
- UNIX es también una marca y una especificación de conformidad gestionada por The Open Group.
- Un sistema tipo Unix puede compartir diseño e interfaces sin estar certificado como UNIX.
- IBM AIX es un sistema operativo UNIX orientado principalmente a servidores y entornos empresariales.

<!-- VISUAL:t38-37-posix-unix-y-sistemas-tipo-unix.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-37-posix-unix-y-sistemas-tipo-unix.webp" alt="POSIX, UNIX y sistemas tipo Unix" width="820">
</p>
<p align="center"><em>Infografía: POSIX, UNIX y sistemas tipo Unix.</em></p>

<!-- FUENTE: POSIX-2024-T38 -->

## 38. Linux: núcleo y distribuciones

**Idea de control:** Linux designa estrictamente el núcleo iniciado por el proyecto de Linus Torvalds.

- Linux designa estrictamente el núcleo iniciado por el proyecto de Linus Torvalds.
- Una distribución combina el núcleo con bibliotecas, herramientas, instalador, repositorios y políticas propias.
- Distintas distribuciones pueden usar el mismo núcleo con componentes y ciclos de soporte diferentes.
- GNU/Linux es una denominación usada cuando se destaca la combinación del núcleo Linux con herramientas GNU.

<!-- VISUAL:t38-38-linux-nucleo-y-distribuciones.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-38-linux-nucleo-y-distribuciones.webp" alt="Linux: núcleo y distribuciones" width="820">
</p>
<p align="center"><em>Infografía: Linux: núcleo y distribuciones.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 39. Arquitectura del núcleo Linux

**Idea de control:** Linux se describe habitualmente como un núcleo monolítico con capacidad modular.

- Linux se describe habitualmente como un núcleo monolítico con capacidad modular.
- Servicios fundamentales como planificación, memoria y VFS se ejecutan en espacio de núcleo.
- Los módulos permiten incorporar funcionalidad al núcleo sin recompilarlo íntegramente en muchos casos.
- Monolítico no significa que todo el software del sistema se ejecute en modo núcleo.

<!-- VISUAL:t38-39-arquitectura-del-nucleo-linux.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-39-arquitectura-del-nucleo-linux.webp" alt="Arquitectura del núcleo Linux" width="820">
</p>
<p align="center"><em>Infografía: Arquitectura del núcleo Linux.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 40. VFS y jerarquía Linux

**Idea de control:** VFS proporciona una interfaz común para que coexistan distintos sistemas de archivos.

- VFS proporciona una interfaz común para que coexistan distintos sistemas de archivos.
- La jerarquía Linux integra volúmenes y sistemas virtuales bajo una raíz.
- Los inodos representan objetos y metadatos en sistemas que usan ese modelo.
- Una entrada de directorio relaciona un nombre con un objeto; nombre e inodo no son la misma cosa.

<!-- VISUAL:t38-40-vfs-y-jerarquia-linux.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-40-vfs-y-jerarquia-linux.webp" alt="VFS y jerarquía Linux" width="820">
</p>
<p align="center"><em>Infografía: VFS y jerarquía Linux.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 41. Procesos y pseudo-sistema /proc

**Idea de control:** /proc expone información de procesos y estructuras internas mediante una interfaz de sistema de archivos.

- /proc expone información de procesos y estructuras internas mediante una interfaz de sistema de archivos.
- Muchas entradas de /proc se generan dinámicamente y no son archivos persistentes en disco.
- Los identificadores numéricos de proceso aparecen como directorios bajo /proc cuando procede.
- Modificar parámetros mediante interfaces de /proc o sysctl exige conocer permisos, alcance y riesgo.

<!-- VISUAL:t38-il-41-procesos-y-pseudo-sistema-proc.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-41-procesos-y-pseudo-sistema-proc.webp" alt="Procesos y pseudo-sistema /proc" width="820">
</p>
<p align="center"><em>Infografía: Procesos y pseudo-sistema /proc.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 42. Propiedad, permisos y privilegios en Linux

**Idea de control:** Los procesos actúan con identidades y grupos que condicionan sus permisos.

- Los procesos actúan con identidades y grupos que condicionan sus permisos.
- root es la cuenta administrativa tradicional, pero los sistemas pueden delegar privilegios de forma controlada.
- sudo ejecuta una orden conforme a una política; no convierte toda la sesión en root necesariamente.
- Las capacidades de Linux pueden dividir privilegios tradicionalmente concentrados en root.

<!-- VISUAL:t38-42-propiedad-permisos-y-privilegios-en-linux.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-42-propiedad-permisos-y-privilegios-en-linux.webp" alt="Propiedad, permisos y privilegios en Linux" width="820">
</p>
<p align="center"><em>Infografía: Propiedad, permisos y privilegios en Linux.</em></p>

<!-- FUENTE: POSIX-2024-T38 -->

## 43. Servicios, demonios y arranque en Linux

**Idea de control:** Un demonio es un proceso que presta servicios en segundo plano.

- Un demonio es un proceso que presta servicios en segundo plano.
- El sistema de inicio y gestor de servicios arranca, supervisa y detiene unidades según configuración.
- systemd es común en muchas distribuciones, pero no define por sí solo a Linux.
- El núcleo inicia el primer proceso de espacio de usuario conforme al sistema configurado.

<!-- VISUAL:t38-43-servicios-demonios-y-arranque-en-linux.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-43-servicios-demonios-y-arranque-en-linux.webp" alt="Servicios, demonios y arranque en Linux" width="820">
</p>
<p align="center"><em>Infografía: Servicios, demonios y arranque en Linux.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 44. Software libre, código abierto y licencias

**Idea de control:** El código del núcleo Linux se distribuye principalmente bajo GPLv2.

- El código del núcleo Linux se distribuye principalmente bajo GPLv2.
- Código abierto describe disponibilidad del código bajo una licencia, no ausencia de derechos de autor.
- Software libre se refiere a libertades de uso, estudio, modificación y redistribución conforme a la licencia.
- Gratuidad, código abierto y software libre son conceptos relacionados, pero no equivalentes.

<!-- VISUAL:t38-44-software-libre-codigo-abierto-y-licencias.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-44-software-libre-codigo-abierto-y-licencias.webp" alt="Software libre, código abierto y licencias" width="820">
</p>
<p align="center"><em>Infografía: Software libre, código abierto y licencias.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 45. Windows y la familia Windows NT

**Idea de control:** Las versiones modernas de escritorio y servidor de Windows pertenecen a la familia Windows NT.

- Las versiones modernas de escritorio y servidor de Windows pertenecen a la familia Windows NT.
- Windows separa componentes de modo usuario y modo núcleo.
- El ejecutivo y el núcleo cooperan con controladores y la capa de abstracción de hardware.
- La compatibilidad con aplicaciones históricas no convierte Windows actual en MS-DOS.

<!-- VISUAL:t38-45-windows-y-la-familia-windows-nt.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-45-windows-y-la-familia-windows-nt.webp" alt="Windows y la familia Windows NT" width="820">
</p>
<p align="center"><em>Infografía: Windows y la familia Windows NT.</em></p>

<!-- FUENTE: MS-WINDOWS-INTERNALS-T38 -->

## 46. Procesos, hilos y servicios en Windows

**Idea de control:** Windows planifica hilos dentro del contexto de procesos.

- Windows planifica hilos dentro del contexto de procesos.
- Un servicio es un programa administrado por el Service Control Manager y puede ejecutarse sin sesión interactiva.
- El Administrador de tareas permite observar aplicaciones, procesos y consumo, pero no sustituye al planificador.
- Finalizar un proceso puede perder trabajo o afectar servicios dependientes.

<!-- VISUAL:t38-46-procesos-hilos-y-servicios-en-windows.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-46-procesos-hilos-y-servicios-en-windows.webp" alt="Procesos, hilos y servicios en Windows" width="820">
</p>
<p align="center"><em>Infografía: Procesos, hilos y servicios en Windows.</em></p>

<!-- FUENTE: MS-WINDOWS-INTERNALS-T38 -->

## 47. Registro de Windows

**Idea de control:** El Registro almacena configuración estructurada del sistema, usuarios y aplicaciones.

- El Registro almacena configuración estructurada del sistema, usuarios y aplicaciones.
- Claves y valores forman una jerarquía lógica distinta de la jerarquía ordinaria de archivos.
- Editar el Registro puede afectar al funcionamiento y requiere copia o procedimiento de recuperación adecuado.
- No toda configuración de Windows vive en el Registro: también existen archivos, bases y servicios de configuración.

<!-- VISUAL:t38-il-47-registro-de-windows.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-47-registro-de-windows.webp" alt="Registro de Windows" width="820">
</p>
<p align="center"><em>Infografía: Registro de Windows.</em></p>

<!-- FUENTE: MS-WINDOWS-INTERNALS-T38 -->

## 48. Explorer, CMD y PowerShell

**Idea de control:** El Explorador de archivos es una interfaz gráfica para navegar y gestionar objetos del sistema de archivos.

- El Explorador de archivos es una interfaz gráfica para navegar y gestionar objetos del sistema de archivos.
- CMD interpreta el lenguaje de comandos tradicional de Windows.
- PowerShell trabaja con comandos y objetos y no es una simple copia de COMMAND.COM.
- Las tres interfaces pueden realizar operaciones semejantes mediante modelos y sintaxis diferentes.

<!-- VISUAL:t38-il-48-explorer-cmd-y-powershell.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-48-explorer-cmd-y-powershell.webp" alt="Explorer, CMD y PowerShell" width="820">
</p>
<p align="center"><em>Infografía: Explorer, CMD y PowerShell.</em></p>

<!-- FUENTE: MS-WINDOWS-INTERNALS-T38 -->

## 49. Cuentas, UAC y controles de acceso

**Idea de control:** Windows asocia procesos a tokens que recogen identidad, grupos y privilegios.

- Windows asocia procesos a tokens que recogen identidad, grupos y privilegios.
- Las ACL especifican qué identidades pueden realizar determinadas operaciones sobre un objeto.
- UAC ayuda a separar el uso ordinario de las operaciones que requieren elevación.
- Aceptar una elevación no concede permisos permanentes e ilimitados a todos los procesos.

<!-- VISUAL:t38-49-cuentas-uac-y-controles-de-acceso.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-49-cuentas-uac-y-controles-de-acceso.webp" alt="Cuentas, UAC y controles de acceso" width="820">
</p>
<p align="center"><em>Infografía: Cuentas, UAC y controles de acceso.</em></p>

<!-- FUENTE: MS-WINDOWS-INTERNALS-T38 -->

## 50. Unidades, rutas y atributos en Windows

**Idea de control:** Windows representa habitualmente volúmenes mediante letras, aunque también admite puntos de montaje en carpetas.

- Windows representa habitualmente volúmenes mediante letras, aunque también admite puntos de montaje en carpetas.
- La barra inversa separa componentes en rutas Win32 habituales.
- Oculto, sistema y solo lectura son atributos; no equivalen por sí solos a permisos de acceso.
- Mostrar archivos ocultos es una opción de visualización y no elimina automáticamente sus restricciones de acceso.

<!-- VISUAL:t38-50-unidades-rutas-y-atributos-en-windows.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-50-unidades-rutas-y-atributos-en-windows.webp" alt="Unidades, rutas y atributos en Windows" width="820">
</p>
<p align="center"><em>Infografía: Unidades, rutas y atributos en Windows.</em></p>

<!-- FUENTE: MS-NTFS-T38 -->

## 51. Actualización, cifrado y recuperación en Windows

**Idea de control:** Windows Update distribuye correcciones y cambios, pero exige gestión de reinicios y compatibilidad.

- Windows Update distribuye correcciones y cambios, pero exige gestión de reinicios y compatibilidad.
- BitLocker cifra volúmenes y protege datos en reposo conforme a su configuración.
- EFS cifra archivos compatibles en NTFS y no es lo mismo que cifrar todo el volumen.
- Los puntos de restauración, copias de seguridad y recuperación de archivos cubren supuestos diferentes.

<!-- VISUAL:t38-51-actualizacion-cifrado-y-recuperacion-en-windows.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-51-actualizacion-cifrado-y-recuperacion-en-windows.webp" alt="Actualización, cifrado y recuperación en Windows" width="820">
</p>
<p align="center"><em>Infografía: Actualización, cifrado y recuperación en Windows.</em></p>

<!-- FUENTE: MS-NTFS-T38 -->

## 52. macOS, Darwin y XNU

**Idea de control:** macOS es el sistema operativo de escritorio de Apple y se apoya en Darwin.

- macOS es el sistema operativo de escritorio de Apple y se apoya en Darwin.
- XNU es el núcleo utilizado por macOS y combina componentes Mach con elementos BSD y controladores I/O Kit.
- macOS ofrece interfaces UNIX y una interfaz gráfica propia.
- Compartir componentes con iOS no convierte ambos sistemas en productos idénticos.

<!-- VISUAL:t38-52-macos-darwin-y-xnu.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-52-macos-darwin-y-xnu.webp" alt="macOS, Darwin y XNU" width="820">
</p>
<p align="center"><em>Infografía: macOS, Darwin y XNU.</em></p>

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 53. Aqua, Finder y Terminal

**Idea de control:** Aqua designa el entorno gráfico característico de macOS.

- Aqua designa el entorno gráfico característico de macOS.
- Finder permite navegar y gestionar archivos, aplicaciones y volúmenes.
- Terminal proporciona acceso a una shell y utilidades de línea de comandos.
- Usar Finder o Terminal no cambia por sí solo los permisos efectivos del usuario.

<!-- VISUAL:t38-il-53-aqua-finder-y-terminal.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-53-aqua-finder-y-terminal.webp" alt="Aqua, Finder y Terminal" width="820">
</p>
<p align="center"><em>Infografía: Aqua, Finder y Terminal.</em></p>

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 54. Aplicaciones, paquetes y sandbox en macOS

**Idea de control:** Una aplicación macOS puede presentarse como un paquete que Finder muestra como una unidad lógica.

- Una aplicación macOS puede presentarse como un paquete que Finder muestra como una unidad lógica.
- El paquete contiene ejecutables y recursos organizados conforme a convenciones de la plataforma.
- El sandbox restringe recursos accesibles a una aplicación según sus permisos y entitlements.
- La firma de código aporta autenticidad e integridad, pero no demuestra que una aplicación sea segura en cualquier circunstancia.

<!-- VISUAL:t38-54-aplicaciones-paquetes-y-sandbox-en-macos.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-54-aplicaciones-paquetes-y-sandbox-en-macos.webp" alt="Aplicaciones, paquetes y sandbox en macOS" width="820">
</p>
<p align="center"><em>Infografía: Aplicaciones, paquetes y sandbox en macOS.</em></p>

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 55. APFS en macOS

**Idea de control:** APFS es el sistema de archivos predeterminado en macOS moderno y en otras plataformas Apple.

- APFS es el sistema de archivos predeterminado en macOS moderno y en otras plataformas Apple.
- APFS fue diseñado con especial atención a almacenamiento Flash y SSD.
- Sus contenedores permiten compartir espacio entre varios volúmenes.
- Copy-on-write, clonación y snapshots son funciones distintas aunque relacionadas.

<!-- VISUAL:t38-55-apfs-en-macos.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-55-apfs-en-macos.webp" alt="APFS en macOS" width="820">
</p>
<p align="center"><em>Infografía: APFS en macOS.</em></p>

<!-- FUENTE: APPLE-APFS-T38 -->

## 56. Rutas, volúmenes y sensibilidad a mayúsculas

**Idea de control:** macOS usa una jerarquía de rutas con barra inclinada y una raíz única.

- macOS usa una jerarquía de rutas con barra inclinada y una raíz única.
- Los volúmenes se montan dentro de esa jerarquía y Finder puede presentarlos con nombres amigables.
- APFS admite variantes sensibles y no sensibles a mayúsculas según el formato elegido.
- No debe suponerse una misma sensibilidad a mayúsculas para todos los volúmenes macOS.

<!-- VISUAL:t38-56-rutas-volumenes-y-sensibilidad-a-mayusculas.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-56-rutas-volumenes-y-sensibilidad-a-mayusculas.webp" alt="Rutas, volúmenes y sensibilidad a mayúsculas" width="820">
</p>
<p align="center"><em>Infografía: Rutas, volúmenes y sensibilidad a mayúsculas.</em></p>

<!-- FUENTE: APPLE-APFS-T38 -->

## 57. FileVault y volumen de sistema firmado

**Idea de control:** FileVault protege datos en reposo mediante cifrado de volumen conforme a la plataforma.

- FileVault protege datos en reposo mediante cifrado de volumen conforme a la plataforma.
- El volumen de sistema firmado protege la integridad del contenido del sistema mediante una cadena verificable.
- Cifrado e integridad responden a amenazas diferentes.
- Perder una clave o credencial de recuperación puede impedir acceder a datos cifrados.

<!-- VISUAL:t38-57-filevault-y-volumen-de-sistema-firmado.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-57-filevault-y-volumen-de-sistema-firmado.webp" alt="FileVault y volumen de sistema firmado" width="820">
</p>
<p align="center"><em>Infografía: FileVault y volumen de sistema firmado.</em></p>

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 58. Rasgos de los sistemas operativos móviles

**Idea de control:** Un sistema móvil gestiona recursos limitados, batería, conectividad radio, sensores y ciclo de vida de aplicaciones.

- Un sistema móvil gestiona recursos limitados, batería, conectividad radio, sensores y ciclo de vida de aplicaciones.
- La interfaz táctil es habitual, pero no define por sí sola la arquitectura del sistema.
- Las aplicaciones se aíslan y reciben permisos conforme al modelo de la plataforma.
- Suspender o terminar procesos en segundo plano permite gestionar energía y memoria.

<!-- VISUAL:t38-58-rasgos-de-los-sistemas-operativos-moviles.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-58-rasgos-de-los-sistemas-operativos-moviles.webp" alt="Rasgos de los sistemas operativos móviles" width="820">
</p>
<p align="center"><em>Infografía: Rasgos de los sistemas operativos móviles.</em></p>

<!-- FUENTE: ANDROID-ARCH-T38 -->

## 59. iOS: arquitectura y ecosistema

**Idea de control:** iOS es el sistema operativo de Apple para iPhone.

- iOS es el sistema operativo de Apple para iPhone.
- Comparte bases tecnológicas con otras plataformas Apple, incluido XNU y APFS.
- El sistema integra frameworks de alto nivel sobre servicios y núcleo protegidos.
- El ecosistema controla instalación, firma y ejecución de aplicaciones mediante políticas de plataforma.

<!-- VISUAL:t38-59-ios-arquitectura-y-ecosistema.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-59-ios-arquitectura-y-ecosistema.webp" alt="iOS: arquitectura y ecosistema" width="820">
</p>
<p align="center"><em>Infografía: iOS: arquitectura y ecosistema.</em></p>

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 60. Sandbox, entitlements y permisos en iOS

**Idea de control:** Las aplicaciones de terceros se ejecutan en sandbox con un contenedor propio.

- Las aplicaciones de terceros se ejecutan en sandbox con un contenedor propio.
- Los entitlements declaran capacidades autorizadas para un binario firmado.
- El acceso a datos sensibles se media mediante servicios y permisos del sistema.
- Conceder un permiso concreto no elimina el resto de límites del sandbox.

<!-- VISUAL:t38-60-sandbox-entitlements-y-permisos-en-ios.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-60-sandbox-entitlements-y-permisos-en-ios.webp" alt="Sandbox, entitlements y permisos en iOS" width="820">
</p>
<p align="center"><em>Infografía: Sandbox, entitlements y permisos en iOS.</em></p>

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 61. iOS, APFS y Data Protection

**Idea de control:** iOS utiliza APFS y mecanismos de Data Protection para proteger datos.

- iOS utiliza APFS y mecanismos de Data Protection para proteger datos.
- Los archivos pueden asociarse a clases que condicionan cuándo son accesibles.
- Las claves por archivo o extensión se integran con la jerarquía criptográfica del dispositivo.
- El estado bloqueado del dispositivo y la disponibilidad de credenciales influyen en el acceso según la clase.

<!-- VISUAL:t38-61-ios-apfs-y-data-protection.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-61-ios-apfs-y-data-protection.webp" alt="iOS, APFS y Data Protection" width="820">
</p>
<p align="center"><em>Infografía: iOS, APFS y Data Protection.</em></p>

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 62. Android: capas de arquitectura

**Idea de control:** Android se apoya en un kernel Linux adaptado a las necesidades de la plataforma.

- Android se apoya en un kernel Linux adaptado a las necesidades de la plataforma.
- La HAL ofrece interfaces normalizadas entre componentes superiores e implementaciones de hardware.
- El runtime y las bibliotecas nativas prestan servicios de ejecución y funciones básicas.
- El framework de aplicaciones expone servicios de alto nivel a las aplicaciones.

<!-- VISUAL:t38-62-android-capas-de-arquitectura.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-62-android-capas-de-arquitectura.webp" alt="Android: capas de arquitectura" width="820">
</p>
<p align="center"><em>Infografía: Android: capas de arquitectura.</em></p>

<!-- FUENTE: ANDROID-ARCH-T38 -->

## 63. Android Runtime y Binder

**Idea de control:** Android Runtime ejecuta código de aplicaciones y gestiona aspectos de su entorno.

- Android Runtime ejecuta código de aplicaciones y gestiona aspectos de su entorno.
- Binder es el mecanismo principal de comunicación entre procesos en Android.
- Los servicios del sistema exponen operaciones a procesos clientes mediante interfaces controladas.
- IPC no significa que todas las aplicaciones compartan el mismo proceso o memoria.

<!-- VISUAL:t38-63-android-runtime-y-binder.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-63-android-runtime-y-binder.webp" alt="Android Runtime y Binder" width="820">
</p>
<p align="center"><em>Infografía: Android Runtime y Binder.</em></p>

<!-- FUENTE: ANDROID-ARCH-T38 -->

## 64. Aislamiento y permisos en Android

**Idea de control:** Android asigna identidades y aislamientos a las aplicaciones para separar sus datos y procesos.

- Android asigna identidades y aislamientos a las aplicaciones para separar sus datos y procesos.
- Los permisos controlan el acceso a funciones o datos protegidos.
- SELinux refuerza el control de acceso obligatorio en la plataforma.
- Instalar una aplicación no concede necesariamente todos los permisos sensibles solicitados.

<!-- VISUAL:t38-64-aislamiento-y-permisos-en-android.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-64-aislamiento-y-permisos-en-android.webp" alt="Aislamiento y permisos en Android" width="820">
</p>
<p align="center"><em>Infografía: Aislamiento y permisos en Android.</em></p>

<!-- FUENTE: ANDROID-ARCH-T38 -->

## 65. Almacenamiento y cifrado en Android

**Idea de control:** El cifrado basado en archivos permite proteger archivos con claves que pueden desbloquearse de forma independiente.

- El cifrado basado en archivos permite proteger archivos con claves que pueden desbloquearse de forma independiente.
- Direct Boot distingue almacenamiento disponible antes y después de desbloquear credenciales.
- El almacenamiento interno privado de una aplicación no equivale al almacenamiento compartido.
- El acceso al almacenamiento compartido está condicionado por versión, permisos y políticas como scoped storage.

<!-- VISUAL:t38-65-almacenamiento-y-cifrado-en-android.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-65-almacenamiento-y-cifrado-en-android.webp" alt="Almacenamiento y cifrado en Android" width="820">
</p>
<p align="center"><em>Infografía: Almacenamiento y cifrado en Android.</em></p>

<!-- FUENTE: ANDROID-STORAGE-T38 -->

## 66. Comparación entre iOS y Android

**Idea de control:** iOS y Android gestionan aplicaciones, memoria, dispositivos, energía, permisos y almacenamiento.

- iOS y Android gestionan aplicaciones, memoria, dispositivos, energía, permisos y almacenamiento.
- iOS utiliza tecnologías Apple como XNU y APFS; Android utiliza un kernel Linux y la arquitectura AOSP.
- Ambos aíslan aplicaciones, aunque sus mecanismos, distribución y políticas no son idénticos.
- Las diferencias de versión y fabricante impiden convertir una observación concreta en regla universal de Android.

<!-- VISUAL:t38-il-66-comparacion-entre-ios-y-android.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-66-comparacion-entre-ios-y-android.webp" alt="Comparación entre iOS y Android" width="820">
</p>
<p align="center"><em>Infografía: Comparación entre iOS y Android.</em></p>

<!-- FUENTE: APPLE-PLATFORM-SECURITY-T38 -->

## 67. Memoria y almacenamiento: clasificación

**Idea de control:** La memoria de trabajo y el almacenamiento persistente cumplen funciones diferentes.

- La memoria de trabajo y el almacenamiento persistente cumplen funciones diferentes.
- Un medio volátil pierde normalmente su contenido al faltar alimentación; uno no volátil lo conserva.
- Almacenamiento local, extraíble y remoto describen ubicación o conexión, no un único tipo físico.
- Capacidad, latencia, rendimiento, durabilidad, coste y disponibilidad son compromisos distintos.

<!-- VISUAL:t38-67-memoria-y-almacenamiento-clasificacion.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-67-memoria-y-almacenamiento-clasificacion.webp" alt="Memoria y almacenamiento: clasificación" width="820">
</p>
<p align="center"><em>Infografía: Memoria y almacenamiento: clasificación.</em></p>

<!-- FUENTE: NVME-SPEC-T38 -->

## 68. Discos magnéticos HDD

**Idea de control:** Un HDD almacena datos mediante dominios magnéticos en platos giratorios.

- Un HDD almacena datos mediante dominios magnéticos en platos giratorios.
- El posicionamiento mecánico introduce latencia de búsqueda y rotación.
- El acceso secuencial suele resultar menos costoso que muchos accesos aleatorios dispersos.
- Golpes, vibración y desgaste mecánico son riesgos relevantes, aunque no los únicos.

<!-- VISUAL:t38-il-68-discos-magneticos-hdd.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-68-discos-magneticos-hdd.webp" alt="Discos magnéticos HDD" width="820">
</p>
<p align="center"><em>Infografía: Discos magnéticos HDD.</em></p>

<!-- FUENTE: MS-STORAGE-T38 -->

## 69. Unidades de estado sólido SSD

**Idea de control:** Un SSD almacena datos normalmente en memoria flash no volátil y carece de platos y cabezales.

- Un SSD almacena datos normalmente en memoria flash no volátil y carece de platos y cabezales.
- El controlador gestiona traducción de direcciones, corrección de errores y distribución de escrituras.
- La amplificación de escritura y el desgaste condicionan la vida útil de la flash.
- TRIM permite al sistema informar de bloques que ya no contienen datos útiles, si toda la cadena lo admite.

<!-- VISUAL:t38-69-unidades-de-estado-solido-ssd.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-69-unidades-de-estado-solido-ssd.webp" alt="Unidades de estado sólido SSD" width="820">
</p>
<p align="center"><em>Infografía: Unidades de estado sólido SSD.</em></p>

<!-- FUENTE: NVME-SPEC-T38 -->

## 70. SATA, NVMe y factores de forma

**Idea de control:** SATA es una interfaz y protocolo de almacenamiento usado por HDD y SSD.

- SATA es una interfaz y protocolo de almacenamiento usado por HDD y SSD.
- NVMe define comunicación del host con almacenamiento no volátil mediante transportes compatibles.
- M.2 describe un factor de forma y conector; una unidad M.2 puede usar protocolos diferentes.
- Un SSD no es automáticamente NVMe y una unidad NVMe no se define únicamente por su forma física.

<!-- VISUAL:t38-70-sata-nvme-y-factores-de-forma.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-70-sata-nvme-y-factores-de-forma.webp" alt="SATA, NVMe y factores de forma" width="820">
</p>
<p align="center"><em>Infografía: SATA, NVMe y factores de forma.</em></p>

<!-- FUENTE: NVME-SPEC-T38 -->

## 71. Medios ópticos y extraíbles

**Idea de control:** CD, DVD y Blu-ray almacenan información mediante estructuras ópticas leídas por una unidad compatible.

- CD, DVD y Blu-ray almacenan información mediante estructuras ópticas leídas por una unidad compatible.
- Los formatos pueden ser de solo lectura, grabables una vez o regrabables.
- Una memoria USB integra almacenamiento flash y un controlador mediante una interfaz USB.
- Extraíble no significa inmune a corrupción, pérdida física o malware.

<!-- VISUAL:t38-71-medios-opticos-y-extraibles.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-71-medios-opticos-y-extraibles.webp" alt="Medios ópticos y extraíbles" width="820">
</p>
<p align="center"><em>Infografía: Medios ópticos y extraíbles.</em></p>

<!-- FUENTE: MS-STORAGE-T38 -->

## 72. Sectores, bloques y clústeres

**Idea de control:** Un sector es una unidad direccionable del dispositivo o de su interfaz lógica.

- Un sector es una unidad direccionable del dispositivo o de su interfaz lógica.
- Un bloque es una unidad utilizada por capas del sistema o del sistema de archivos.
- Un clúster o unidad de asignación agrupa sectores para asignar espacio a archivos en determinados sistemas.
- Sector, bloque, página y clúster no deben usarse como sinónimos universales.

<!-- VISUAL:t38-72-sectores-bloques-y-clusteres.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-72-sectores-bloques-y-clusteres.webp" alt="Sectores, bloques y clústeres" width="820">
</p>
<p align="center"><em>Infografía: Sectores, bloques y clústeres.</em></p>

<!-- FUENTE: LINUX-EXT4-T38 -->

## 73. Particiones, volúmenes, MBR y GPT

**Idea de control:** Una partición divide lógicamente el espacio de un dispositivo conforme a una tabla.

- Una partición divide lógicamente el espacio de un dispositivo conforme a una tabla.
- Un volumen es una unidad lógica que el sistema puede formatear y montar, y no siempre coincide uno a uno con una partición.
- MBR es un esquema histórico con limitaciones de tamaño y número de particiones primarias.
- GPT usa identificadores GUID, admite más particiones y se asocia habitualmente con UEFI.

<!-- VISUAL:t38-73-particiones-volumenes-mbr-y-gpt.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-73-particiones-volumenes-mbr-y-gpt.webp" alt="Particiones, volúmenes, MBR y GPT" width="820">
</p>
<p align="center"><em>Infografía: Particiones, volúmenes, MBR y GPT.</em></p>

<!-- FUENTE: MS-STORAGE-T38 -->

## 74. RAID, redundancia y copia de seguridad

**Idea de control:** RAID combina unidades para obtener rendimiento, capacidad o redundancia según el nivel.

- RAID combina unidades para obtener rendimiento, capacidad o redundancia según el nivel.
- RAID 0 distribuye datos sin redundancia y aumenta el impacto del fallo de una unidad.
- RAID 1 mantiene copias espejo y sacrifica capacidad útil.
- RAID no sustituye una copia de seguridad independiente frente a borrado, corrupción o ataque.

<!-- VISUAL:t38-il-74-raid-redundancia-y-copia-de-seguridad.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-74-raid-redundancia-y-copia-de-seguridad.webp" alt="RAID, redundancia y copia de seguridad" width="820">
</p>
<p align="center"><em>Infografía: RAID, redundancia y copia de seguridad.</em></p>

<!-- FUENTE: MS-STORAGE-T38 -->

## 75. Concepto y funciones del sistema de archivos

**Idea de control:** Un sistema de archivos define cómo se organizan, nombran y localizan datos y metadatos en un soporte o espacio lógico.

- Un sistema de archivos define cómo se organizan, nombran y localizan datos y metadatos en un soporte o espacio lógico.
- Gestiona asignación de espacio, directorios y operaciones sobre archivos.
- Puede incorporar permisos, diario, compresión, cifrado, cuotas o instantáneas según su diseño.
- El sistema de archivos no es el dispositivo físico ni la tabla de particiones.

<!-- VISUAL:t38-75-concepto-y-funciones-del-sistema-de-archivos.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-75-concepto-y-funciones-del-sistema-de-archivos.webp" alt="Concepto y funciones del sistema de archivos" width="820">
</p>
<p align="center"><em>Infografía: Concepto y funciones del sistema de archivos.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 76. Archivos, directorios y metadatos

**Idea de control:** El contenido de un archivo se distingue de los metadatos que lo describen.

- El contenido de un archivo se distingue de los metadatos que lo describen.
- Un directorio asocia nombres con objetos del sistema de archivos.
- Las marcas temporales pueden registrar distintos eventos y su significado depende del sistema.
- Extensión, tipo real y aplicación asociada son conceptos relacionados, pero no idénticos.

<!-- VISUAL:t38-76-archivos-directorios-y-metadatos.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-76-archivos-directorios-y-metadatos.webp" alt="Archivos, directorios y metadatos" width="820">
</p>
<p align="center"><em>Infografía: Archivos, directorios y metadatos.</em></p>

<!-- FUENTE: LINUX-KERNEL-T38 -->

## 77. Rutas absolutas, relativas y resolución de nombres

**Idea de control:** Una ruta absoluta se resuelve desde una raíz o designador completo del sistema.

- Una ruta absoluta se resuelve desde una raíz o designador completo del sistema.
- Una ruta relativa se interpreta desde el directorio de trabajo u otro contexto definido.
- Los componentes especiales punto y doble punto representan respectivamente el directorio actual y su padre en entornos compatibles.
- Los separadores, nombres reservados y sensibilidad a mayúsculas dependen del sistema y de su configuración.

<!-- VISUAL:t38-77-rutas-absolutas-relativas-y-resolucion-de-nombres.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-77-rutas-absolutas-relativas-y-resolucion-de-nombres.webp" alt="Rutas absolutas, relativas y resolución de nombres" width="820">
</p>
<p align="center"><em>Infografía: Rutas absolutas, relativas y resolución de nombres.</em></p>

<!-- FUENTE: POSIX-2024-T38 -->

## 78. Asignación de espacio y fragmentación interna

**Idea de control:** El sistema de archivos asigna espacio en unidades que pueden ser mayores que los datos finales de un archivo.

- El sistema de archivos asigna espacio en unidades que pueden ser mayores que los datos finales de un archivo.
- El espacio no aprovechado dentro de la última unidad asignada es fragmentación interna.
- Unidades mayores reducen ciertas estructuras de gestión, pero pueden desperdiciar más espacio con archivos pequeños.
- La elección de tamaño de unidad depende del sistema, volumen y carga de trabajo.

<!-- VISUAL:t38-78-asignacion-de-espacio-y-fragmentacion-interna.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-78-asignacion-de-espacio-y-fragmentacion-interna.webp" alt="Asignación de espacio y fragmentación interna" width="820">
</p>
<p align="center"><em>Infografía: Asignación de espacio y fragmentación interna.</em></p>

<!-- FUENTE: LINUX-EXT4-T38 -->

## 79. Montaje, letras y puntos de montaje

**Idea de control:** Montar conecta un sistema de archivos con un punto accesible de la jerarquía.

- Montar conecta un sistema de archivos con un punto accesible de la jerarquía.
- Los sistemas tipo Unix usan puntos de montaje dentro de un árbol único.
- Windows usa habitualmente letras, pero también puede montar volúmenes en carpetas.
- Desmontar de forma segura permite completar escrituras pendientes antes de retirar un medio.

<!-- VISUAL:t38-79-montaje-letras-y-puntos-de-montaje.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-79-montaje-letras-y-puntos-de-montaje.webp" alt="Montaje, letras y puntos de montaje" width="820">
</p>
<p align="center"><em>Infografía: Montaje, letras y puntos de montaje.</em></p>

<!-- FUENTE: POSIX-2024-T38 -->

## 80. Formateo, borrado y recuperación

**Idea de control:** Formatear crea o renueva estructuras de un sistema de archivos en un volumen.

- Formatear crea o renueva estructuras de un sistema de archivos en un volumen.
- El formato rápido suele reconstruir metadatos esenciales sin verificar ni sobrescribir todo el soporte.
- Eliminar o formatear no garantiza por sí solo un borrado irrecuperable.
- El borrado seguro depende del medio, cifrado, controlador y procedimiento de sanitización.

<!-- VISUAL:t38-80-formateo-borrado-y-recuperacion.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-80-formateo-borrado-y-recuperacion.webp" alt="Formateo, borrado y recuperación" width="820">
</p>
<p align="center"><em>Infografía: Formateo, borrado y recuperación.</em></p>

<!-- FUENTE: MS-STORAGE-T38 -->

## 81. Diario, copy-on-write y comprobaciones

**Idea de control:** El journaling registra información de cambios para facilitar recuperación tras una interrupción.

- El journaling registra información de cambios para facilitar recuperación tras una interrupción.
- Copy-on-write escribe cambios en nuevas ubicaciones antes de actualizar referencias.
- Los checksums detectan determinadas alteraciones, pero no reparan cualquier daño por sí solos.
- Ninguno de estos mecanismos sustituye una copia de seguridad independiente.

<!-- VISUAL:t38-81-diario-copy-on-write-y-comprobaciones.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-81-diario-copy-on-write-y-comprobaciones.webp" alt="Diario, copy-on-write y comprobaciones" width="820">
</p>
<p align="center"><em>Infografía: Diario, copy-on-write y comprobaciones.</em></p>

<!-- FUENTE: LINUX-EXT4-T38 -->

## 82. FAT12, FAT16 y FAT32

**Idea de control:** Las variantes FAT se diferencian principalmente por el tamaño de sus entradas y la cantidad de clústeres direccionables.

- Las variantes FAT se diferencian principalmente por el tamaño de sus entradas y la cantidad de clústeres direccionables.
- FAT32 mantiene amplia compatibilidad, pero carece de permisos ACL y diario nativos comparables a NTFS.
- FAT32 no admite archivos de tamaño igual o superior a 4 GiB por el campo de tamaño de 32 bits.
- El límite práctico de creación de volúmenes puede depender de la herramienta y no solo del formato FAT32.

<!-- VISUAL:t38-82-fat12-fat16-y-fat32.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-82-fat12-fat16-y-fat32.webp" alt="FAT12, FAT16 y FAT32" width="820">
</p>
<p align="center"><em>Infografía: FAT12, FAT16 y FAT32.</em></p>

<!-- FUENTE: MS-EXFAT-T38 -->

## 83. exFAT

**Idea de control:** exFAT es sucesor de FAT32 dentro de la familia FAT.

- exFAT es sucesor de FAT32 dentro de la familia FAT.
- Utiliza campos de 64 bits para tamaño de archivo y fue diseñado para archivos y dispositivos grandes.
- Mantiene una estructura relativamente simple y orientada a medios extraíbles y flash.
- La compatibilidad real depende de la versión del sistema y del dispositivo, no solo del nombre exFAT.

<!-- VISUAL:t38-83-exfat.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-83-exfat.webp" alt="exFAT" width="820">
</p>
<p align="center"><em>Infografía: exFAT.</em></p>

<!-- FUENTE: MS-EXFAT-T38 -->

## 84. NTFS

**Idea de control:** NTFS es el sistema de archivos predeterminado de Windows moderno para volúmenes del sistema.

- NTFS es el sistema de archivos predeterminado de Windows moderno para volúmenes del sistema.
- Admite descriptores de seguridad y listas de control de acceso.
- Incluye diario de metadatos y funciones como compresión, cuotas y cifrado EFS.
- La compatibilidad de escritura desde otros sistemas debe comprobarse por versión y software; no es universal por definición.

<!-- VISUAL:t38-84-ntfs.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-84-ntfs.webp" alt="NTFS" width="820">
</p>
<p align="center"><em>Infografía: NTFS.</em></p>

<!-- FUENTE: MS-NTFS-T38 -->

## 85. ReFS y alcance comparado

**Idea de control:** ReFS es un sistema de archivos de Microsoft orientado a resiliencia, integridad y escenarios de almacenamiento determinados.

- ReFS es un sistema de archivos de Microsoft orientado a resiliencia, integridad y escenarios de almacenamiento determinados.
- ReFS y NTFS comparten algunas funciones, pero no son intercambiables en todos los escenarios.
- La disponibilidad de ReFS depende de la edición, versión y tipo de volumen de Windows.
- Que ReFS sea más reciente no lo convierte automáticamente en la mejor elección para cualquier equipo.

<!-- VISUAL:t38-85-refs-y-alcance-comparado.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-85-refs-y-alcance-comparado.webp" alt="ReFS y alcance comparado" width="820">
</p>
<p align="center"><em>Infografía: ReFS y alcance comparado.</em></p>

<!-- FUENTE: MS-NTFS-T38 -->

## 86. ext2, ext3 y ext4

**Idea de control:** ext2 no incorpora el diario que caracteriza a ext3.

- ext2 no incorpora el diario que caracteriza a ext3.
- ext3 añadió journaling manteniendo continuidad con ext2.
- ext4 amplió capacidad y rendimiento mediante extents, asignación diferida y otras mejoras.
- ext4 utiliza inodos, grupos de bloques y un diario gestionado con JBD2 cuando está habilitado.

<!-- VISUAL:t38-86-ext2-ext3-y-ext4.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-86-ext2-ext3-y-ext4.webp" alt="ext2, ext3 y ext4" width="820">
</p>
<p align="center"><em>Infografía: ext2, ext3 y ext4.</em></p>

<!-- FUENTE: LINUX-EXT4-T38 -->

## 87. APFS y HFS+

**Idea de control:** HFS+ fue el sistema principal de macOS antes de APFS.

- HFS+ fue el sistema principal de macOS antes de APFS.
- APFS se convirtió en el sistema predeterminado de las plataformas Apple modernas.
- APFS ofrece cifrado, snapshots, clonación y espacio compartido entre volúmenes.
- La transición no significa que todos los soportes antiguos o externos se conviertan automáticamente a APFS.

<!-- VISUAL:t38-87-apfs-y-hfs.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-87-apfs-y-hfs.webp" alt="APFS y HFS+" width="820">
</p>
<p align="center"><em>Infografía: APFS y HFS+.</em></p>

<!-- FUENTE: APPLE-APFS-T38 -->

## 88. ISO 9660 y UDF

**Idea de control:** ISO 9660 se diseñó para el intercambio de datos en medios ópticos de solo lectura.

- ISO 9660 se diseñó para el intercambio de datos en medios ópticos de solo lectura.
- UDF se utiliza en distintos medios ópticos y soporta casos más amplios y archivos mayores según versión.
- Las extensiones de ISO 9660 pueden ampliar nombres y metadatos para plataformas concretas.
- El sistema de archivos del medio y el tipo físico de disco son capas distintas.

<!-- VISUAL:t38-88-iso-9660-y-udf.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-88-iso-9660-y-udf.webp" alt="ISO 9660 y UDF" width="820">
</p>
<p align="center"><em>Infografía: ISO 9660 y UDF.</em></p>

<!-- FUENTE: MS-STORAGE-T38 -->

## 89. Enlaces, permisos y sensibilidad a mayúsculas

**Idea de control:** Un enlace duro añade otra referencia al mismo objeto dentro de las restricciones del sistema de archivos.

- Un enlace duro añade otra referencia al mismo objeto dentro de las restricciones del sistema de archivos.
- Un enlace simbólico contiene una referencia de ruta y puede quedar roto si cambia su destino.
- Los permisos pueden expresarse mediante bits clásicos, ACL u otros modelos.
- La distinción entre mayúsculas y minúsculas depende del sistema de archivos, su formato y la capa que resuelve nombres.

<!-- VISUAL:t38-89-enlaces-permisos-y-sensibilidad-a-mayusculas.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-89-enlaces-permisos-y-sensibilidad-a-mayusculas.webp" alt="Enlaces, permisos y sensibilidad a mayúsculas" width="820">
</p>
<p align="center"><em>Infografía: Enlaces, permisos y sensibilidad a mayúsculas.</em></p>

<!-- FUENTE: POSIX-2024-T38 -->

## 90. Elección del sistema de archivos

**Idea de control:** La elección debe considerar sistema operativo, tamaño de archivos, permisos, resiliencia, rendimiento y dispositivos de destino.

- La elección debe considerar sistema operativo, tamaño de archivos, permisos, resiliencia, rendimiento y dispositivos de destino.
- FAT32 prioriza compatibilidad amplia con límites relevantes; exFAT amplía tamaños para medios compartidos.
- NTFS y FAT, ext4 y APFS son ejemplos reales de sistemas de archivos de los ecosistemas Windows, Linux y Apple.
- Ninguna tabla de compatibilidad es eterna: debe fecharse y comprobarse en las versiones concretas implicadas.

<!-- VISUAL:t38-il-90-eleccion-del-sistema-de-archivos.webp -->
<p align="center">
  <img src="../../../assets/policia-nacional/tema-38/t38-il-90-eleccion-del-sistema-de-archivos.webp" alt="Elección del sistema de archivos" width="820">
</p>
<p align="center"><em>Infografía: Elección del sistema de archivos.</em></p>

<!-- FUENTE: CONVOCATORIA-PN-2026-T38 -->

# Hablemos claro

:::hablemos-claro
Este tema tiene cuatro trampas maestras: confundir hardware con software; programa con proceso; dispositivo, partición, volumen y sistema de archivos; y producto histórico con versión actual. Antes de responder identifica la capa, la plataforma y si la afirmación depende de versión.
:::

# En la calle

:::en-la-calle
En una intervención, distinguir un archivo oculto de uno inaccesible, un volumen cifrado de una copia de seguridad o una unidad M.2 de un protocolo NVMe evita diagnósticos falsos y preserva mejor la evidencia.
:::

# Lo que cae

:::lo-que-cae
Prioriza funciones del sistema operativo; proceso, hilo y planificación; memoria virtual; kernel, shell y GUI; diferencias entre MS-DOS, UNIX, Linux, Windows, macOS, iOS y Android; HDD/SSD, SATA/NVMe, MBR/GPT; y FAT32, exFAT, NTFS, ext4 y APFS.
:::

# Ha caído

:::ha-caido
Se han localizado 9 referencias históricas del Tema 38. Permanecen ocultas y en cuarentena porque no existe plantilla oficial final verificable en el repositorio.
:::

## Fuentes legales, institucionales y primarias

- `CONVOCATORIA-PN-2026-T38`
- `MS-WINDOWS-INTERNALS-T38`
- `MS-NTFS-T38`
- `MS-EXFAT-T38`
- `MS-STORAGE-T38`
- `MS-DOS-SOURCE-T38`
- `POSIX-2024-T38`
- `LINUX-KERNEL-T38`
- `LINUX-EXT4-T38`
- `APPLE-PLATFORM-SECURITY-T38`
- `APPLE-APFS-T38`
- `ANDROID-ARCH-T38`
- `ANDROID-STORAGE-T38`
- `NVME-SPEC-T38`

---

*Academia En Vigor · El temario que nunca duerme · Tema 38 · v1.0.0 · Documento interno no publicado.*
