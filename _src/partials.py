HEAD = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="PT Duta Retail Indonesia (DRI) — the Daisei Group's retail, production and distribution company: Japanese food supply, La Mouette bakery and Jakaichi Mart, a Japanese store for groceries, household goods and everyday products. Jakarta Selatan, Indonesia.">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#111111">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body class="lang-id">
<header class="site">
  <div class="wrap">
    <a class="brand" href="/"><img src="/assets/logo-white.png" alt="DRI logo"><span>PT Duta Retail Indonesia<small>DRI</small></span></a>
    <nav class="main">
      <a href="/#about"><span data-l="id">Tentang</span><span data-l="en">About</span><span data-l="ja">会社概要</span></a>
      <a href="/#store"><span data-l="id">Toko</span><span data-l="en">Our Store</span><span data-l="ja">店舗</span></a>
      <a href="/#products"><span data-l="id">Produk &amp; Harga</span><span data-l="en">Products &amp; Prices</span><span data-l="ja">商品・価格</span></a>
      <a href="/#order"><span data-l="id">Cara Pesan</span><span data-l="en">How to Order</span><span data-l="ja">ご注文方法</span></a>
      <a href="/#contact"><span data-l="id">Kontak</span><span data-l="en">Contact</span><span data-l="ja">お問い合わせ</span></a>
    </nav>
    <div class="langs" role="group" aria-label="Language">
      <button data-set="id" aria-pressed="true">ID</button><button data-set="en" aria-pressed="false">EN</button><button data-set="ja" aria-pressed="false">日本語</button>
    </div>
  </div>
</header>
"""

# ===== CONTACT DETAILS — edit here, then regenerate (or edit every page's footer) =====
EMAIL = '<a href="mailto:hello@daiseigroup.com">hello@daiseigroup.com</a>'
PHONE = '<a href="tel:+6282320974945">0823-2097-4945</a>'
WHATSAPP = '<span class="todo">+62 8xx-xxxx-xxxx (TBC)</span>'
ADDRESS = "Kamome Building, Jl. Melawai Raya No. 189 B Lt. 3, Kramat Pela, Kebayoran Baru, Jakarta Selatan 12160, Indonesia"

FOOT = f"""
<footer class="site">
  <div class="wrap">
    <div class="cols">
      <div>
        <strong>PT Duta Retail Indonesia</strong><br>
        <span data-l="id">Perusahaan ritel, produksi dan distribusi Daisei Group.</span><span data-l="en">The Daisei Group's retail, production and distribution company.</span><span data-l="ja">ダイセイグループの小売・製造・流通会社。</span><br><br>
        {ADDRESS}<br>
        NIB 2007260033369
      </div>
      <div>
        <strong><span data-l="id">Kontak</span><span data-l="en">Contact</span><span data-l="ja">お問い合わせ</span></strong>
        <ul>
          <li>Email: {EMAIL}</li>
          <li><span data-l="id">Telepon</span><span data-l="en">Phone</span><span data-l="ja">電話</span>: {PHONE}</li>
        </ul>
      </div>
      <div>
        <strong><span data-l="id">Kebijakan</span><span data-l="en">Policies</span><span data-l="ja">規約・ポリシー</span></strong>
        <ul>
          <li><a href="/terms.html"><span data-l="id">Syarat &amp; Ketentuan</span><span data-l="en">Terms &amp; Conditions</span><span data-l="ja">利用規約</span></a></li>
          <li><a href="/privacy.html"><span data-l="id">Kebijakan Privasi</span><span data-l="en">Privacy Policy</span><span data-l="ja">プライバシーポリシー</span></a></li>
          <li><a href="/refund.html"><span data-l="id">Kebijakan Pengembalian Dana &amp; Pembatalan</span><span data-l="en">Refund &amp; Cancellation Policy</span><span data-l="ja">返金・キャンセルポリシー</span></a></li>
        </ul>
      </div>
    </div>
    <div class="copy">&copy; <span id="year">2026</span> PT Duta Retail Indonesia. <span data-l="id">Hak cipta dilindungi.</span><span data-l="en">All rights reserved.</span><span data-l="ja">All rights reserved.</span></div>
  </div>
</footer>
<script src="/assets/site.js"></script>
</body>
</html>
"""
