"""Convert source dress photos into web JPEGs and merge them into img/manifest.json.

Usage:  python prepare_images.py "<path to a folder of numbered dress folders>"

Only numerically-named subfolders are read, so a source folder may hold other
directories (e.g. "New Ones") without upsetting the run. Existing manifest
entries for folders not present in this source are left alone, so each batch of
new dresses can be added without re-processing the whole collection.
"""
import os, sys, hashlib, json
from PIL import Image, ImageOps

SRC = sys.argv[1]
ROOT = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(ROOT, 'img', 'manifest.json')

manifest = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}

folders = sorted((d for d in os.listdir(SRC) if d.isdigit() and os.path.isdir(f'{SRC}/{d}')), key=int)
if not folders:
    sys.exit(f'No numbered dress folders found in {SRC}')

for d in folders:
    seen, out = set(), []
    for f in sorted(os.listdir(f'{SRC}/{d}')):
        path = f'{SRC}/{d}/{f}'
        h = hashlib.md5(open(path, 'rb').read()).hexdigest()
        if h in seen:
            continue
        seen.add(h)
        i = len(out) + 1
        im = ImageOps.exif_transpose(Image.open(path)).convert('RGB')
        big = im.copy(); big.thumbnail((1400, 1400))
        big.save(f'{ROOT}/img/dresses/{d}-{i}.jpg', quality=82, optimize=True, progressive=True)
        th = im.copy(); th.thumbnail((640, 640))
        th.save(f'{ROOT}/img/thumbs/{d}-{i}.jpg', quality=80, optimize=True)
        out.append(f'{d}-{i}.jpg')
    manifest[d] = out
    print(f'  #{d}: {len(out)} images')

json.dump(manifest, open(MANIFEST, 'w'), indent=1)
print(f'manifest now holds {len(manifest)} dresses')
