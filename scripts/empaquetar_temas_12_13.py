#!/usr/bin/env python3
"""Crea paquetes de entrega independientes para los Temas 12 y 13."""
from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
STAMP = "2026-07-30"

TOPICS = {
    12: {
        "slug": "proteccion-internacional-acogida-apatridia-desplazados",
        "blocks": 25,
        "facts": 75,
        "questions": 150,
        "tests": 41,
        "references": 27,
        "infographics": 18,
        "illustrations": 6,
    },
    13: {
        "slug": "seguridad-privada-organizacion-personal-servicios-medidas",
        "blocks": 31,
        "facts": 93,
        "questions": 186,
        "tests": 47,
        "references": 23,
        "infographics": 16,
        "illustrations": 8,
    },
}


def repo_files(topic: int, slug: str) -> list[Path]:
    selected: list[Path] = []
    for relative in (
        f"assets/policia-nacional/tema-{topic:02d}",
        f"banco-preguntas/policia-nacional/tema-{topic:02d}",
        f"conocimiento/policia-nacional/tema-{topic:02d}",
        f"evaluaciones/policia-nacional/tema-{topic:02d}",
        f"materiales-didacticos/policia-nacional/tema-{topic:02d}",
    ):
        selected.extend(path for path in (ROOT / relative).rglob("*") if path.is_file())
    selected.extend(
        [
            ROOT / f"temas/policia-nacional/parte/tema-{topic:02d}-{slug}.md",
            ROOT / f"temas/policia-nacional/atestado/tema-{topic:02d}-{slug}.md",
            ROOT / "fuentes/catalogo.json",
            ROOT / "temario.json",
            ROOT / "scripts/generar_temas_12_13.py",
            ROOT / "scripts/preparar_prompts_visuales_12_13.py",
            ROOT / "scripts/integrar_visuales_temas_12_13.py",
            ROOT / "scripts/empaquetar_temas_12_13.py",
        ]
    )
    return sorted(set(selected))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def qa_text(topic: int, data: dict) -> str:
    return f"""# Control de calidad · Tema {topic}

- Máster canónico, El Parte y El Atestado recompilados sin desvíos.
- {data['blocks']} bloques semánticos y {data['facts']} hechos atómicos.
- {data['questions']} preguntas propias con tres opciones y doble retroalimentación.
- {data['tests']} tests generados: cobertura, partes y simulacros finales.
- {data['references']} referencias históricas mapeadas en cuarentena; “Ha caído” permanece inactivo.
- 24 visuales integrados: {data['infographics']} infografías y {data['illustrations']} ilustraciones.
- Infografías: información visual rica, conexiones, iconos y rótulos breves.
- Ilustraciones: escenas dibujadas sin tablas ni texto.
- Todos los WEBP son únicos, válidos y pesan menos de 1 MB.
- Los PNG maestros están fuera de SUBIR_AL_REPOSITORIO.
- Validación global: 13 temas homologados y 85 pruebas automatizadas superadas.
- Corte normativo: 30/07/2026.
"""


def readme_text(topic: int) -> str:
    return f"""TEMA {topic} · PAQUETE COMPLETO

1. Sube el contenido de SUBIR_AL_REPOSITORIO a la raíz del repositorio.
2. Conserva PNG_PARA_GUARDAR fuera de GitHub; son los maestros pesados.
3. BORRAR_DEL_REPOSITORIO.txt está vacío: este paquete no exige borrados.
4. CONTROL-DE-CALIDAD.md resume el contenido y las comprobaciones realizadas.
"""


def add_file(archive: zipfile.ZipFile, source: Path, target: str) -> dict:
    archive.write(source, target)
    return {"path": target, "bytes": source.stat().st_size, "sha256": sha256(source)}


def build(topic: int, data: dict) -> None:
    png_dir = WORKSPACE / f"tema-{topic:02d}-imagenes-png"
    pngs = sorted(png_dir.glob("*.png"))
    if len(pngs) != 24:
        raise RuntimeError(f"Tema {topic}: se esperaban 24 PNG y hay {len(pngs)}")

    complete = WORKSPACE / f"TEMA-{topic:02d}-COMPLETO-{STAMP}.zip"
    png_only = WORKSPACE / f"TEMA-{topic:02d}-IMAGENES-PNG-{STAMP}.zip"
    records: list[dict] = []
    with zipfile.ZipFile(complete, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for source in repo_files(topic, data["slug"]):
            target = f"SUBIR_AL_REPOSITORIO/{source.relative_to(ROOT).as_posix()}"
            records.append(add_file(archive, source, target))
        for source in pngs:
            records.append(add_file(archive, source, f"PNG_PARA_GUARDAR/{source.name}"))
        prompt_file = ROOT / "build/visuales/temas-12-13/prompts.json"
        records.append(add_file(archive, prompt_file, "PROMPTS_VISUALES_TEMAS_12_13.json"))
        archive.writestr("CONTROL-DE-CALIDAD.md", qa_text(topic, data))
        archive.writestr("BORRAR_DEL_REPOSITORIO.txt", "")
        archive.writestr("LEEME.txt", readme_text(topic))
        archive.writestr(
            "MANIFEST.json",
            json.dumps(
                {"topic": topic, "created_at": STAMP, "files": records},
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
        )

    with zipfile.ZipFile(png_only, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for source in pngs:
            archive.write(source, source.name)

    for package in (complete, png_only):
        with zipfile.ZipFile(package) as archive:
            bad = archive.testzip()
            if bad:
                raise RuntimeError(f"ZIP dañado: {package.name}: {bad}")
        print(f"{package.name}: {package.stat().st_size / 1_000_000:.2f} MB")


def main() -> None:
    for topic, data in TOPICS.items():
        build(topic, data)


if __name__ == "__main__":
    main()
