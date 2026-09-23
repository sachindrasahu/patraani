"""Builds index.html, stuti.html and dresses/<name>.html from dresses.json + img/manifest.json.

Run `python build.py` after adding dresses (see README.md).
"""
import json, os, html
from urllib.parse import quote

ROOT = os.path.dirname(os.path.abspath(__file__))
DRESSES = json.load(open(os.path.join(ROOT, 'dresses.json'), encoding='utf-8'))
MANIFEST = json.load(open(os.path.join(ROOT, 'img', 'manifest.json')))
SIZES = json.load(open(os.path.join(ROOT, 'sizes.json'), encoding='utf-8'))

IG = 'https://www.instagram.com/rinestuofficial/'
WA_STUTI = '919312255642'
WA_NEENA = '919873416631'
ADDRESS_Q = '62+B.D.+Estate,+Civil+Lines,+Delhi+110054'

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">')

IG_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true">'
          '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>')


def head(title, desc, base='', extra_class=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<link rel="icon" href="{base}favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="{base}css/style.css">
</head>
<body class="{extra_class}">'''


def header(base='', solid=False):
    cls = ' always-solid' if solid else ''
    return f'''<header class="site-header{cls}">
  <a class="brand" href="{base}index.html">Patraani<small>Est. 1995 · Delhi</small></a>
  <button class="nav-toggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
  <nav class="nav">
    <a href="{base}index.html#story">Our Story</a>
    <a href="{base}index.html#collection">The Collection</a>
    <a href="{base}index.html#rinestu">Rinestu</a>
    <a href="{base}index.html#women">The Women</a>
    <a href="{base}index.html#visit">Visit</a>
  </nav>
</header>'''


def footer(base='', floating=True):
    return f'''<footer>
  <div class="wrap">
    <div>
      <div class="brand">Patraani</div>
      <div class="fine">62, B.D. Estate, Civil Lines, Delhi 110054 · Since 1995</div>
    </div>
    <div class="links">
      <a href="{IG}" target="_blank" rel="noopener">Instagram</a>
      <a href="https://wa.me/{WA_STUTI}" target="_blank" rel="noopener">WhatsApp</a>
      <a href="#size-guide" data-size-guide>Size Guide</a>
      <a href="{base}index.html#collection">Collection</a>
    </div>
  </div>
</footer>
{size_modal()}
{float_wa(base) if floating else ''}
<script src="{base}js/main.js"></script>
</body>
</html>'''


def size_modal():
    cols = ''.join(f'<th>{html.escape(c)}</th>' for c in SIZES['columns'])
    rows = ''.join('<tr>' + ''.join(f'<td>{html.escape(c)}</td>' for c in r) + '</tr>' for r in SIZES['rows'])
    howto = ''.join(f'<div><dt>{html.escape(a)}</dt><dd>{html.escape(b)}</dd></div>' for a, b in SIZES['howto'])
    return f'''<div class="size-modal" id="size-guide" role="dialog" aria-modal="true" aria-label="Size guide" hidden>
  <div class="size-panel">
    <button class="size-close" aria-label="Close">&#10005;</button>
    <div class="eyebrow">Size guide</div>
    <h2>Finding <em>your size</em></h2>
    <p class="size-intro">All measurements are body measurements, in inches. Every garment is cut with comfortable ease over these. If you are between sizes, or would like a piece made to your own measurements, simply tell us on WhatsApp &mdash; almost everything we make can be altered or made to order at no extra cost.</p>
    <div class="size-table-wrap">
      <table class="size-table"><thead><tr>{cols}</tr></thead><tbody>{rows}</tbody></table>
    </div>
    <h3>How to measure</h3>
    <dl class="size-howto">{howto}</dl>
    <p class="size-foot">Still unsure? Send us your usual size in any brand you wear often, and we will match it.</p>
  </div>
</div>'''


def float_wa(base=''):
    msg = 'Hello! I would like to order from the Patraani collection.'
    return (f'<a class="wa-float" href="https://wa.me/{WA_STUTI}?text=' + quote(msg) +
            '" target="_blank" rel="noopener" aria-label="Order on WhatsApp">'
            '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.2-1.7-.9-2-1-.3-.1-.5-.2-.7.1s-.8 1-.9 1.2c-.2.2-.3.2-.6.1a8 8 0 0 1-2.4-1.5 9 9 0 0 1-1.6-2c-.2-.3 0-.5.1-.6l.5-.6.3-.5v-.5l-1-2.3c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.2.2 2.2 3.3 5.2 4.6.7.3 1.3.5 1.8.6.7.2 1.4.2 1.9.1.6-.1 1.7-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3z"/><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3.1.8.8-3-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></svg>'
            '<span>Order on WhatsApp</span></a>')


def imgs(d):
    return MANIFEST[str(d['id'])]


def slug(d):
    return d['name'].lower()


# ---------------------------------------------------------------- index.html
def build_index():
    cards = []
    for i, d in enumerate(DRESSES):
        im = imgs(d)
        alt = f'<img class="alt" src="img/thumbs/{im[1]}" alt="" loading="lazy">' if len(im) > 1 else ''
        cards.append(f'''
      <a class="card reveal" data-delay="{i % 4}" href="dresses/{slug(d)}.html">
        <div class="frame">
          <img class="main" src="img/thumbs/{im[0]}" alt="{html.escape(d['name'])} — {html.escape(d['line'])}" loading="lazy">
          {alt}
        </div>
        <div class="meta"><h3>{html.escape(d['name'])}</h3><span>View →</span></div>
      </a>''')

    ticker = ''.join('<span>Hand Embroidery<i>✦</i></span><span>Est. 1995<i>✦</i></span><span>Civil Lines, Delhi<i>✦</i></span><span>Limited Edition<i>✦</i></span><span>Three Women, One Thread<i>✦</i></span>' for _ in range(2))

    page = head('Patraani — Indian Wear, Made by Hand Since 1995',
                'Patraani: fashion in its most cultivated form. Limited-edition Indian and Western wear with fine hand embroidery, from Civil Lines, Delhi. Home of Rinestu.') + header() + f'''

<section class="hero" id="top">
  <div class="hero-media"><img src="img/dresses/17-1.jpg" alt="" fetchpriority="high"></div>
  <div class="hero-content">
    <div class="eyebrow">Indian wear · Made by hand · Since 1995</div>
    <h1>Patraani</h1>
    <p class="lede">Fashion in its most cultivated form. A limited-edition assortment of Indian and Western wear, embroidered by hand in Civil Lines, Delhi — by three women and the karigars who have grown old with them.</p>
    <div class="hero-actions">
      <a class="btn" href="#collection">View the collection</a>
      <a class="btn" href="#story" style="border-color:transparent;padding-left:0">Our story →</a>
    </div>
  </div>
  <div class="scroll-cue">Scroll</div>
</section>

<div class="ticker" aria-hidden="true"><div class="ticker-track">{ticker}</div></div>

<section class="story" id="story">
  <div class="wrap story-grid">
    <figure class="story-media reveal">
      <img src="img/dresses/20-1.jpg" alt="A Patraani kurta in blush linen with an ivory jacquard panel">
      <div class="stamp"><div><b>30</b>years of<br>needle &amp; thread</div></div>
      <figcaption>Lullaby</figcaption>
    </figure>
    <div class="story-text">
      <div class="eyebrow reveal">Our story</div>
      <h2 class="reveal" data-delay="1">It began in 1995, in a year that also gave the family <em>a daughter.</em></h2>
      <p class="first reveal" data-delay="1">Ritu Gupta had just graduated from NIFT Delhi, from a batch that would go on to shape Indian fashion for the next thirty years. While her classmates chased the runways, she chose the slower, quieter craft: Indian wear, made by hand, made to last. She set up a workshop, found her karigars, and called it Patraani.</p>
      <p class="reveal" data-delay="2">When Ritu married and relocated, her sister Neena picked up the needle. For the better part of three decades she has held the label steady — through changing fashions and faithful customers — with the same stubborn devotion to detail: embroidery so fine you have to lean in to see it, fabrics chosen like heirlooms, and prices that never forgot the women who wore them.</p>
      <div class="pull reveal" data-delay="2">“They come back because our garments are evergreen. A Patraani piece is not for a season. It is for a life.”<small>A customer of thirty years</small></div>
      <p class="reveal" data-delay="2">And then there was the daughter. Stuti was born the same year Patraani was, and she grew up on its floor — among bolts of fabric, trays of sequins, and the low hum of karigars at work. Fashion was never a career she chose; it was the house she grew up in. After graduating in Fashion Design she came home to her mother's table, and later built her own sub-label under the same roof.</p>
      <p class="reveal" data-delay="3">Today the three names are stitched into one. <span class="serif-i">Ri</span>tu. <span class="serif-i">Ne</span>ena. <span class="serif-i">Stu</span>ti.</p>
      <div class="ri-ne-stu reveal" data-delay="3"><b>Ri</b><span>·</span><b>Ne</b><span>·</span><b>Stu</b></div>
    </div>
  </div>
</section>

<section class="values">
  <div class="wrap values-grid">
    <div class="value reveal"><div class="num">I</div><h3>Hand <em>embroidery</em></h3><p>Extremely delicate, intricate Indian embroidery, done by hand by karigars who have been with us for decades.</p></div>
    <div class="value reveal" data-delay="1"><div class="num">II</div><h3>Fabrics like <em>heirlooms</em></h3><p>Only the finest linens, cottons and silks — chosen to be worn for years, washed for years, loved for years.</p></div>
    <div class="value reveal" data-delay="2"><div class="num">III</div><h3>Original <em>design</em></h3><p>Traditional cuts with fine ornate embroidery; Western silhouettes with delicate, atypical detail. Nothing copied.</p></div>
    <div class="value reveal" data-delay="3"><div class="num">IV</div><h3>Honest <em>pricing</em></h3><p>Finer workmanship than the market, at a price that has always stayed nominal. That is how you keep a customer for thirty years.</p></div>
  </div>
</section>

<section class="collection" id="collection">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow reveal">The exhibition</div>
      <h2 class="reveal" data-delay="1">The <em>Collection</em></h2>
      <p class="reveal" data-delay="2">A limited edition. Every garment is embroidered by hand and made in small numbers — when it's gone, it's gone. Click any piece to see it from every angle.</p>
    </div>
    <div class="grid">{''.join(cards)}
    </div>
  </div>
</section>

<section class="rinestu" id="rinestu">
  <div class="wrap">
    <div>
      <div class="eyebrow reveal">The sub-label</div>
      <h2 class="reveal" data-delay="1">Rinestu — a younger hand, <em>the same old heart.</em></h2>
      <p class="reveal" data-delay="2">Founded by Stuti under the Patraani roof, Rinestu brings the label's eye for detail to intricate machine embroidery — executed by our own karigars, with the same fabrics, the same finish and the same refusal to compromise.</p>
      <p class="reveal" data-delay="2">The name is an acronym, and a tribute: the first letters of the three women who built this house. Ritu, the founder. Neena, who carried it. Stuti, who grew up in it.</p>
      <div class="letters reveal" data-delay="3">
        <div><b>Ri</b><span>Ritu</span></div>
        <div><b>Ne</b><span>Neena</span></div>
        <div><b>Stu</b><span>Stuti</span></div>
      </div>
      <div style="margin-top:34px" class="reveal" data-delay="3"><a class="btn" href="{IG}" target="_blank" rel="noopener">@rinestuofficial on Instagram</a></div>
    </div>
    <figure class="reveal"><img src="img/dresses/12-5.jpg" alt="Close-up of Rinestu embroidery on peach linen" loading="lazy"></figure>
  </div>
</section>

<section class="women" id="women">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow reveal">The women</div>
      <h2 class="reveal" data-delay="1">Three names. <em>One thread.</em></h2>
    </div>
    <div class="women-grid">
      <div class="person reveal">
        <div class="photo"><img src="img/team/ritu.jpg" alt="Ritu Gupta" loading="lazy"></div>
        <h3>Ritu Gupta</h3>
        <div class="role">Founder · 1995</div>
        <p>NIFT Delhi. Began Patraani with a needle, a few metres of fabric and an unfashionable belief in things that last.</p>
      </div>
      <div class="person reveal" data-delay="1">
        <div class="photo"><img src="img/team/neena.jpg" alt="Neena Gupta" loading="lazy"></div>
        <h3>Neena Gupta</h3>
        <div class="role">Designer &amp; Proprietor · Patraani</div>
        <p>The hand that has guided Patraani for the better part of three decades. Took over from her sister and has led every collection since — knows every karigar by name, every customer by their wardrobe, and every stitch before it is made.</p>
      </div>
      <a class="person reveal" data-delay="2" href="stuti.html">
        <div class="photo"><img src="img/team/stuti.jpg" alt="Stuti Gupta" loading="lazy"></div>
        <h3>Stuti Gupta</h3>
        <div class="role">Designer · Founder, Rinestu</div>
        <p>Born the year Patraani was. Grew up on its floor. Now designs for it — and for a label of her own.</p>
        <span class="cta">Read her story</span>
      </a>
    </div>
  </div>
</section>

<section class="visit" id="visit">
  <div class="wrap">
    <div>
      <div class="eyebrow reveal">Visit us</div>
      <h2 class="reveal" data-delay="1">Come, <em>lean in.</em></h2>
      <p class="reveal" data-delay="1" style="margin:18px 0 34px;color:var(--ink-soft);max-width:48ch">The embroidery is best seen up close. Write to us, call, or come by the studio in Civil Lines.</p>
      <dl class="reveal" data-delay="2">
        <div><dt>Studio</dt><dd><a href="https://www.google.com/maps/search/?api=1&query={ADDRESS_Q}" target="_blank" rel="noopener">62, B.D. Estate, Civil Lines,<br>Delhi 110054</a></dd></div>
        <div><dt>Call or WhatsApp</dt>
          <dd><a href="https://wa.me/{WA_STUTI}" target="_blank" rel="noopener">+91 93122 55642</a><small>Stuti Gupta</small></dd>
          <dd style="margin-top:14px"><a href="https://wa.me/{WA_NEENA}" target="_blank" rel="noopener">+91 98734 16631</a><small>Neena Gupta</small></dd>
        </div>
        <div><dt>Instagram</dt><dd><a class="ig" href="{IG}" target="_blank" rel="noopener">{IG_SVG}@rinestuofficial</a></dd></div>
      </dl>
    </div>
    <div class="map reveal" data-delay="2">
      <iframe title="Map — 62 B.D. Estate, Civil Lines, Delhi" src="https://www.google.com/maps?q={ADDRESS_Q}&z=16&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
  </div>
</section>
''' + footer()
    open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(page)


# ---------------------------------------------------------------- dress pages
def build_dresses():
    os.makedirs(os.path.join(ROOT, 'dresses'), exist_ok=True)
    n = len(DRESSES)
    for i, d in enumerate(DRESSES):
        prev_d, next_d = DRESSES[(i - 1) % n], DRESSES[(i + 1) % n]
        im = imgs(d)
        figs = ''.join(
            f'<figure><img src="../img/dresses/{f}" alt="{html.escape(d["name"])} — view {k + 1}"{" loading=\"lazy\"" if k else ""}></figure>'
            for k, f in enumerate(im))
        size_buttons = ''.join(
            f'<button type="button" class="size-opt" data-size="{r[0]}">{r[0]}</button>'
            for r in SIZES['rows']) + '<button type="button" class="size-opt" data-size="Made to measure">Made to measure</button>'
        wa_text = f"Hello! I would like to order '{d['name']}' from the Patraani collection."
        wa = f'https://wa.me/{WA_STUTI}?text=' + quote(wa_text)
        page = head(f'{d["name"]} · Patraani', d['line'], base='../') + header(base='../', solid=True) + f'''
<main class="dress-page">
  <div class="wrap">
    <div class="crumbs"><a href="../index.html">Patraani</a> / <a href="../index.html#collection">The Collection</a> / <span>{html.escape(d['name'])}</span></div>
    <div class="dress-layout">
      <div class="dress-gallery">{figs}</div>
      <aside class="dress-info">
        <div class="num">Patraani · The Collection</div>
        <h1>{html.escape(d['name'])}</h1>
        <p class="line">{html.escape(d['line'])}</p>
        <div class="facts">
          <div><span>Edition</span><span>Limited · made to order</span></div>
          <div><span>Embroidery</span><span>By hand, in-house</span></div>
          <div><span>Studio</span><span>Civil Lines, Delhi</span></div>
        </div>
        <div class="order" data-dress="{html.escape(d['name'])}" data-wa="{WA_STUTI}">
          <div class="order-head">
            <span class="order-label">Select a size</span>
            <a href="#size-guide" data-size-guide class="size-link">Size guide</a>
          </div>
          <div class="size-picker" role="group" aria-label="Select a size">{size_buttons}</div>
          <div class="actions">
            <a class="btn solid order-btn" href="{wa}" target="_blank" rel="noopener">Order on WhatsApp</a>
            <a class="btn dark" href="{IG}" target="_blank" rel="noopener">See more on Instagram</a>
          </div>
          <p class="order-note">Orders and enquiries are answered personally by Stuti. Alterations and made-to-measure are available on every piece.</p>
        </div>
        <nav class="dress-nav">
          <a class="prev" href="{slug(prev_d)}.html"><span>← Previous</span><b>{html.escape(prev_d['name'])}</b></a>
          <a class="next" href="{slug(next_d)}.html"><span>Next →</span><b>{html.escape(next_d['name'])}</b></a>
        </nav>
      </aside>
    </div>
  </div>
</main>
<div class="lightbox" role="dialog" aria-label="Image viewer">
  <button class="close">Close ✕</button>
  <button class="prev" aria-label="Previous">‹</button>
  <img src="" alt="">
  <button class="next" aria-label="Next">›</button>
  <div class="count"></div>
</div>
''' + footer(base='../', floating=False)
        open(os.path.join(ROOT, 'dresses', slug(d) + '.html'), 'w', encoding='utf-8').write(page)


# ---------------------------------------------------------------- stuti.html
def build_stuti():
    page = head('Stuti Gupta — Designer · Patraani & Rinestu',
                'Born the year Patraani was founded, Stuti Gupta grew up among fabric and embroidery. She now designs for Patraani and leads her own sub-label, Rinestu.') + header(solid=True) + f'''
<main class="profile-page">
  <div class="wrap">
    <div class="profile-hero">
      <div class="photo reveal"><img src="img/team/stuti.jpg" alt="Stuti Gupta"></div>
      <div>
        <div class="eyebrow reveal">The women · Stuti</div>
        <h1 class="reveal" data-delay="1">Stuti <em>Gupta</em></h1>
        <div class="role reveal" data-delay="1">Designer, Patraani · Founder, Rinestu</div>
        <p class="intro reveal" data-delay="2">“Patraani and I were born in the same year. I have never known a home without fabric in it.”</p>
      </div>
    </div>
    <div class="profile-body">
      <p class="first reveal">Nineteen ninety-five was the year my aunt, Ritu, came home from NIFT Delhi and started a label. It was also the year I was born. So I grew up surrounded by it all — the fashion, the fabrics, the embellishments — the way other children grow up around a family shop or a family farm. The dining table was a cutting table. The karigars were uncles. A tray of sequins was as ordinary as a bowl of fruit.</p>
      <p class="reveal">What I understood only later is how unusual the thing was that they were building. Our USP has always been extremely delicate, intricate Indian embroidery, done entirely by hand by our super-skilled embroiderers — men who have been with us longer than I have been alive. Our customers have stayed loyal for thirty years, and when you ask them why, they say the same things: the garments are evergreen, the quality is exceptional, and the price is nothing like what the market asks for work that is, honestly, far coarser than ours.</p>
      <h2 class="reveal">My mother's <em>table</em></h2>
      <p class="reveal">When my aunt got married and relocated, my mother, Neena, took over the label — and has run it ever since. I joined her soon after finishing my graduation in Fashion Design, to help with the designing. I like to say I joined the business; the truth is I simply came home and sat down at her table.</p>
      <h2 class="reveal">Ri · Ne · <em>Stu</em></h2>
      <p class="reveal">In time I started my own sub-label, Rinestu. Where Patraani is the hand, Rinestu is the machine — intricate machine embroidery, executed by our own karigars, with the same eye and the same standards. The name is an acronym, and a small act of gratitude: the first letters of the three women who built this house. <em>Ri</em>tu, my aunt. <em>Ne</em>ena, my mother. <em>Stu</em>ti, me.</p>
      <h2 class="reveal">What Patraani <em>is</em></h2>
      <p class="reveal">Patraani is fashion in its most cultivated form. A limited-edition, eclectic assortment of Indian clothes with fine ornate embroideries in traditional cuts, and Western clothes with delicate embroideries in atypical styles. We make garments for today's women — women of choice, women who live in the smaller details of life, women who believe in durability. That is why our clients fall in love with what they wear, and why they come back.</p>
      <p class="reveal">Our fabrics are of the finest quality, our workmanship exquisite, our designs original and our pricing genuinely competitive. I could say that about many labels. I can prove it about ours — come to Civil Lines and lean in close.</p>
      <div class="sig reveal">Stuti<small>Civil Lines, Delhi</small></div>
      <div class="reveal" style="margin-top:40px;display:flex;gap:14px;flex-wrap:wrap">
        <a class="btn dark" href="index.html#collection">View the collection</a>
        <a class="btn dark" href="{IG}" target="_blank" rel="noopener">@rinestuofficial</a>
      </div>
    </div>
  </div>
</main>
''' + footer()
    open(os.path.join(ROOT, 'stuti.html'), 'w', encoding='utf-8').write(page)


def prune():
    """Delete dress pages whose entry is no longer in dresses.json."""
    keep = {slug(d) + '.html' for d in DRESSES}
    folder = os.path.join(ROOT, 'dresses')
    for f in os.listdir(folder):
        if f.endswith('.html') and f not in keep:
            os.remove(os.path.join(folder, f))
            print('removed stale page:', f)


if __name__ == '__main__':
    build_index(); build_dresses(); build_stuti(); prune()
    print(f'Built index.html, stuti.html and {len(DRESSES)} dress pages.')
