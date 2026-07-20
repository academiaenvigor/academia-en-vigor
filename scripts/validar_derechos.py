
#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_EXTENSIONS = {
    '.pdf', '.doc', '.docx', '.odt', '.rtf', '.ppt', '.pptx', '.key',
    '.mp3', '.wav', '.m4a', '.aac', '.flac', '.mp4', '.mov', '.avi', '.mkv',
    '.zip', '.rar', '.7z',
}
FORBIDDEN_DIR_NAMES = {'fuentes-privadas', 'originales', 'escaneos', 'descargas'}
ALLOWED_IMAGE_ROOT = ROOT / 'assets'
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.webp', '.svg'}


def main() -> int:
    errors = []
    for path in ROOT.rglob('*'):
        if '.git' in path.parts or 'build' in path.parts or '__pycache__' in path.parts:
            continue
        if path.is_dir() and path.name.lower() in FORBIDDEN_DIR_NAMES:
            errors.append(f'Directorio privado no permitido: {path.relative_to(ROOT)}')
            continue
        if not path.is_file():
            continue
        suffix = path.suffix.lower()
        if suffix in FORBIDDEN_EXTENSIONS:
            errors.append(f'Archivo binario o comprimido no permitido: {path.relative_to(ROOT)}')
        if suffix in IMAGE_EXTENSIONS and ALLOWED_IMAGE_ROOT not in path.parents:
            errors.append(f'Imagen fuera de assets/: {path.relative_to(ROOT)}')
        lowered = path.name.lower()
        if any(marker in lowered for marker in ('marca-de-agua', 'watermark', 'soluciones-y-retroalimentacion')):
            errors.append(f'Nombre sospechoso de material ajeno: {path.relative_to(ROOT)}')
    if errors:
        print('\n'.join(f'ERROR: {error}' for error in errors))
        return 1
    print('OK derechos: no hay documentos de terceros ni binarios pesados versionados')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
