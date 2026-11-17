"""Generate the static GitHub Pages site into docs/. Run: python3 -I build_site.py <out_dir>"""
import sys, pathlib
from urllib.parse import quote

OUT = pathlib.Path(sys.argv[1])
PHONE = "60193685562"
PHONE_PRETTY = "+60 19-368 5562"
NAME = "Azeery"
# --- Dealership details: placeholders until the user supplies them ---
DEALER = "[NAMA PENGEDAR PERODUA]"
ADDRESS = "[ALAMAT PENUH PENGEDAR], Kota Bharu, Kelantan"
HOURS = "[WAKTU OPERASI, cth. Isnin–Sabtu 9 pagi – 6 petang]"
MAPS = "https://www.google.com/maps/search/?api=1&query=" + quote("Perodua Kota Bharu Kelantan")

def wa(msg):
    return f"https://wa.me/{PHONE}?text={quote(msg + ' (dari Google)')}"

WA_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3Z"/></svg>'
GENERAL = "Salam, saya nak tanya pasal kereta Perodua"

def page(slug, title, desc, body):
    return f"""<!doctype html>
<html lang="ms">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="azeery.jpg">
<link rel="icon" href="azeery.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
<nav class="nav"><div class="nav-in">
  <a href="index.html"{' aria-current="page"' if slug=='index' else ''}>Utama</a>
  <a href="cara-beli.html"{' aria-current="page"' if slug=='cara-beli' else ''}>Cara Beli</a>
  <a href="tentang.html"{' aria-current="page"' if slug=='tentang' else ''}>Tentang Saya</a>
  <a href="privasi.html"{' aria-current="page"' if slug=='privasi' else ''}>Privasi</a>
</div></nav>
<main class="wrap">
{body}
<footer>
  <p><strong>{NAME}</strong> · Sales Advisor di {DEALER}, pengedar Perodua sah.<br>{ADDRESS}<br>WhatsApp / telefon: {PHONE_PRETTY}</p>
  <p>Laman ini dikendalikan oleh {NAME} sebagai sales advisor dan bukan laman web rasmi Perodua. Harga, promosi dan tarikh serahan tertakluk kepada pengesahan semasa.</p>
  <p><a href="privasi.html">Dasar Privasi</a></p>
</footer>
</main>
<div class="bar"><a class="btn-wa" href="{wa(GENERAL)}" target="_blank" rel="noopener">{WA_ICON} WhatsApp Saya Sekarang</a></div>
</body>
</html>
"""

MODELS = [
    ("Axia", "Hatchback 5 tempat duduk"), ("Bezza", "Sedan 5 tempat duduk"),
    ("Myvi", "Hatchback 5 tempat duduk"), ("Ativa", "SUV kompak 5 tempat duduk"),
    ("Traz", "SUV 5 tempat duduk"), ("Alza", "MPV 7 tempat duduk"), ("Aruz", "SUV 7 tempat duduk"),
]
chips = "\n".join(
    f'      <a class="chip" href="{wa(f"Salam, saya berminat dengan Perodua {m}. Boleh bagi harga dan bayaran bulanan?")}" target="_blank" rel="noopener"><b>{m}</b><small>{d}</small><em>Tanya harga →</em></a>'
    for m, d in MODELS)

who = f"""<div class="who">
      <img class="avatar" src="azeery.jpg" alt="Gambar {NAME}" width="80" height="80">
      <div><strong>{NAME}</strong><span class="muted">Sales Advisor · {DEALER}<br>Kota Bharu, Kelantan</span></div>
    </div>"""

index = f"""  <header>
    {who}
    <p class="eyebrow">Kereta baru Perodua di Kota Bharu</p>
    <h1>Tanya harga, bayaran bulanan dan booking terus di WhatsApp</h1>
    <p class="lead muted">Saya sales advisor di {DEALER}. Saya bantu kira bayaran bulanan, semak kelayakan loan dan uruskan booking sampai kereta diserahkan.</p>
    <a class="btn-wa" href="{wa(GENERAL)}" target="_blank" rel="noopener">{WA_ICON} WhatsApp Saya Sekarang</a>
    <p class="muted small">No. WhatsApp: <a href="tel:+{PHONE}">{PHONE_PRETTY}</a></p>
  </header>

  <section aria-labelledby="m-h">
    <h2 id="m-h">Pilih model, terus tanya harga</h2>
    <div class="models">
{chips}
    </div>
  </section>

  <section class="card" aria-labelledby="l-h">
    <h2 id="l-h">Lokasi bilik pameran</h2>
    <p><strong>{DEALER}</strong><br>{ADDRESS}<br><span class="muted">{HOURS}</span></p>
    <p><a href="{MAPS}" target="_blank" rel="noopener">Buka di Google Maps →</a></p>
  </section>
"""

cara = f"""  <header>
    <p class="eyebrow">Cara beli</p>
    <h1>Langkah beli kereta Perodua dengan saya</h1>
  </header>
  <section>
    <ol class="steps">
      <li><div><b>WhatsApp saya</b><span class="muted">Beritahu model, warna dan bajet bulanan anda.</span></div></li>
      <li><div><b>Kira bayaran &amp; semak loan</b><span class="muted">Saya kira bayaran bulanan dan bantu semak kelayakan pinjaman bank.</span></div></li>
      <li><div><b>Booking</b><span class="muted">Sahkan model dan warna, kemudian buat booking di {DEALER}.</span></div></li>
      <li><div><b>Ambil kereta</b><span class="muted">Saya maklumkan tarikh serahan dan uruskan sampai kunci di tangan anda.</span></div></li>
    </ol>
  </section>
  <section class="card" aria-labelledby="d-h">
    <h2 id="d-h">Dokumen biasa untuk loan kereta</h2>
    <ul>
      <li>Salinan kad pengenalan (depan dan belakang)</li>
      <li>Slip gaji 3 bulan terkini</li>
      <li>Penyata bank 3 bulan terkini</li>
      <li>Lesen memandu</li>
    </ul>
    <p class="muted small">Bekerja sendiri? WhatsApp saya untuk senarai dokumen yang sesuai.</p>
  </section>
  <a class="btn-wa" href="{wa('Salam, saya nak semak kelayakan loan kereta Perodua')}" target="_blank" rel="noopener">{WA_ICON} Semak kelayakan loan</a>
"""

tentang = f"""  <header>
    {who}
    <p class="eyebrow">Tentang saya</p>
    <h1>Sales advisor Perodua di Kota Bharu</h1>
  </header>
  <section>
    <p>Saya {NAME}, sales advisor di <strong>{DEALER}</strong>, pengedar Perodua sah di Kota Bharu, Kelantan. Saya bantu pelanggan pilih model yang sesuai, kira bayaran bulanan, uruskan permohonan loan dan booking, sehingga kereta diserahkan.</p>
    <p>Laman ini saya kendalikan sendiri untuk memudahkan pelanggan menghubungi saya. Ia bukan laman web rasmi Perodua.</p>
  </section>
  <section class="card" aria-labelledby="c-h">
    <h2 id="c-h">Hubungi &amp; lokasi</h2>
    <p><strong>{DEALER}</strong><br>{ADDRESS}<br><span class="muted">{HOURS}</span></p>
    <p>WhatsApp / telefon: <a href="tel:+{PHONE}">{PHONE_PRETTY}</a></p>
    <p><a href="{MAPS}" target="_blank" rel="noopener">Buka di Google Maps →</a></p>
  </section>
"""

privasi = f"""  <header>
    <p class="eyebrow">Privasi</p>
    <h1>Dasar Privasi</h1>
  </header>
  <section>
    <p>Laman ini tidak mempunyai borang dan tidak mengumpul maklumat peribadi anda secara automatik.</p>
    <p>Apabila anda menghubungi saya melalui WhatsApp atau telefon, nombor telefon dan maklumat yang anda kongsi hanya digunakan untuk menjawab pertanyaan anda dan menguruskan pembelian kereta. Maklumat ini tidak dijual atau dikongsi dengan pihak lain, kecuali kepada bank atau pengedar apabila perlu untuk permohonan loan dan booking yang anda minta.</p>
    <p>Anda boleh minta saya memadam maklumat anda pada bila-bila masa dengan menghubungi {PHONE_PRETTY}.</p>
    <p class="muted small">Laman ini mungkin memuatkan fon daripada Google Fonts. Jika iklan Google digunakan, Google mungkin menggunakan kuki mengikut dasar privasi Google.</p>
  </section>
"""

pages = {
    "index": (f"{NAME} · Sales Advisor Perodua Kota Bharu", f"Sales advisor Perodua di Kota Bharu, Kelantan. WhatsApp {NAME} untuk sebut harga, bayaran bulanan dan booking.", index),
    "cara-beli": ("Cara Beli Kereta Perodua · " + NAME, "Langkah beli kereta Perodua di Kota Bharu dan dokumen yang diperlukan untuk loan kereta.", cara),
    "tentang": ("Tentang " + NAME + " · Sales Advisor Perodua", f"{NAME}, sales advisor di {DEALER}, Kota Bharu, Kelantan.", tentang),
    "privasi": ("Dasar Privasi · " + NAME, "Bagaimana maklumat anda digunakan apabila menghubungi saya.", privasi),
}
for slug, (t, d, b) in pages.items():
    (OUT / f"{slug}.html").write_text(page(slug, t, d, b), encoding="utf-8")
(OUT / "robots.txt").write_text("User-agent: *\nAllow: /\n")
print("ok", sorted(p.name for p in OUT.iterdir()))
