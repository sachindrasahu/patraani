# Patraani — exhibition website

Static site, hosted on GitHub Pages.

## Adding a dress
1. Put the photos in a numbered folder under the source `Dresses/` folder (e.g. `Dresses/26/`).
2. Run the image step in `prepare_images.py` (writes `img/dresses`, `img/thumbs`, `img/manifest.json`).
3. Add a line to `dresses.json` with `id`, one-word `name`, and a one-line description.
4. `python build.py`, then commit and push.

Team photos live in `img/team/` (800×800 squares).
