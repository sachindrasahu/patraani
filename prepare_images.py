"""Converts source dress PNGs to web JPEGs. Usage: python prepare_images.py "<path to Dresses folder>" """
import os, sys, hashlib, json
from PIL import Image
SRC = sys.argv[1]; ROOT = os.path.dirname(os.path.abspath(__file__))
manifest = {}
for d in sorted(os.listdir(SRC), key=int):
    seen, out = set(), []
    for f in sorted(os.listdir(f'{SRC}/{d}')):
        h = hashlib.md5(open(f'{SRC}/{d}/{f}', 'rb').read()).hexdigest()
        if h in seen: continue
        seen.add(h)
        i = len(out) + 1
        im = Image.open(f'{SRC}/{d}/{f}').convert('RGB')
        big = im.copy(); big.thumbnail((1400, 1400)); big.save(f'{ROOT}/img/dresses/{d}-{i}.jpg', quality=82, optimize=True, progressive=True)
        th = im.copy(); th.thumbnail((640, 640)); th.save(f'{ROOT}/img/thumbs/{d}-{i}.jpg', quality=80, optimize=True)
        out.append(f'{d}-{i}.jpg')
    manifest[d] = out
json.dump(manifest, open(f'{ROOT}/img/manifest.json', 'w'), indent=1)
print({k: len(v) for k, v in manifest.items()})
