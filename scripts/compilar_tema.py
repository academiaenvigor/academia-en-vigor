#!/usr/bin/env python3
from pathlib import Path
import argparse, json, re
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'conocimiento/policia-nacional/tema-03/manifest.json'
BLOCK_RE=re.compile(
 r'<!-- BLOCK (\d{2}) START -->\n## \d+\. (.*?)\n\*\*Fuente principal:\*\* `([^`]+)`\n'
 r'<!-- PARTE START -->\n(.*?)\n<!-- PARTE END -->\n'
 r'<!-- ATESTADO START -->\n(.*?)\n<!-- ATESTADO END -->\n<!-- BLOCK \1 END -->',re.S)
LAYERS=['MAPA','CONTENIDO','HABLEMOS_CLARO','EN_LA_CALLE','LO_QUE_CAE','HA_CAIDO']
def load():
 m=json.loads(MANIFEST.read_text(encoding='utf-8'))
 text=(ROOT/m['source_file']).read_text(encoding='utf-8')
 blocks=[{'number':n,'title':t,'source':s,'parte':p.strip(),'atestado':a.strip()} for n,t,s,p,a in BLOCK_RE.findall(text)]
 layers={}
 for key in LAYERS:
  mm=re.search(rf'<!-- LAYER:{key} -->\n# ([^\n]+)\n(.*?)(?=\n<!-- LAYER:|\Z)',text,re.S)
  if not mm: raise ValueError(f'Falta capa {key}')
  layers[key]=(mm.group(1),mm.group(2).strip())
 return m,blocks,layers
def render(kind,m,blocks,layers):
 out=[f"# TEMA 3 · LA CONSTITUCIÓN ESPAÑOLA (II)\n\n**Policía Nacional · Método VIGOR · {kind.upper()}**\n**Versión de contenido:** {m['content_version']}\n**Estado editorial:** {m['editorial_status']} · **Publicación:** {m['publication_status']}\n"]
 out.append(f"# {layers['MAPA'][0]}\n\n{layers['MAPA'][1]}\n")
 out.append('# Contenido\n')
 for b in blocks:
  out.append(f"## {b['number']}. {b['title']}\n\n{b[kind]}\n\n*Referencia principal: `{b['source']}`.*\n")
 for key in LAYERS[2:]:
  title,body=layers[key]; out.append(f"# {title}\n\n{body}\n")
 out.append(f"---\n\n*Academia En Vigor · El temario que nunca duerme · Tema 3 · v{m['content_version']} · Documento interno no publicado.*\n")
 return '\n'.join(out)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--write',action='store_true'); ap.add_argument('--check',action='store_true'); args=ap.parse_args()
 m,b,l=load()
 if len(b)!=m['semantic_blocks']: raise SystemExit(f"Bloques incoherentes: {len(b)}")
 bad=[]
 for kind,path in m['outputs'].items():
  target=ROOT/path; expected=render(kind,m,b,l)
  if args.write: target.parent.mkdir(parents=True,exist_ok=True); target.write_text(expected,encoding='utf-8')
  if args.check and (not target.exists() or target.read_text(encoding='utf-8')!=expected): bad.append(path)
 if bad:
  print('Derivados desactualizados:',*bad,sep='\n- '); return 1
 print(f"OK: {len(b)} bloques; derivados {'escritos' if args.write else 'verificados' if args.check else 'calculados'}")
 return 0
if __name__=='__main__': raise SystemExit(main())
