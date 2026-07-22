from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_compiler():
    path = ROOT / 'scripts/compilar_tema.py'
    spec = importlib.util.spec_from_file_location('compilar_tema', path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_all_semantic_types_are_allowed():
    module = load_compiler()
    expected = {'hablemos-claro', 'en-la-calle', 'lo-que-cae', 'perla-vigor', 'trampa', 'ha-caido', 'visual'}
    assert module.VIGOR_BLOCKS == expected


def test_tema_01_semantic_blocks_are_balanced():
    module = load_compiler()
    path = ROOT / 'conocimiento/policia-nacional/tema-01/master.md'
    module.validate_vigor_blocks(path.read_text(encoding='utf-8'), str(path.relative_to(ROOT)))


def test_compiled_views_preserve_semantic_blocks():
    for relative in [
        'temas/policia-nacional/parte/tema-01-el-derecho-la-persona-y-la-nacionalidad.md',
        'temas/policia-nacional/atestado/tema-01-el-derecho-la-persona-y-la-nacionalidad.md',
    ]:
        text = (ROOT / relative).read_text(encoding='utf-8')
        assert ':::lo-que-cae' in text
        assert ':::visual' in text


def test_explorer_supports_filters_and_auto_images():
    text = (ROOT / 'explorador.html').read_text(encoding='utf-8')
    assert 'function filtrar' in text
    assert 'function resolverVisuales' in text
    assert "'hablemos-claro'" in text
    assert "'lo-que-cae'" in text
