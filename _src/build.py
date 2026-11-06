# Regenerates the site pages from the templates in this folder.
# Run from the repo root:  python3 _src/build.py
import os, sys
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
from partials import HEAD, FOOT, EMAIL, PHONE, WHATSAPP, ADDRESS
pages = {
    'index': 'PT Duta Retail Indonesia (DRI)',
    'terms': 'Syarat & Ketentuan / Terms & Conditions — DRI',
    'privacy': 'Kebijakan Privasi / Privacy Policy — DRI',
    'refund': 'Kebijakan Pengembalian Dana / Refund Policy — DRI',
}
root = os.path.dirname(here)
for k, t in pages.items():
    body = open(os.path.join(here, f'{k}_body.html'), encoding='utf-8').read()
    for a, b in {'{EMAIL}': EMAIL, '{PHONE}': PHONE, '{WHATSAPP}': WHATSAPP, '{ADDRESS}': ADDRESS}.items():
        body = body.replace(a, b)
    with open(os.path.join(root, f'{k}.html'), 'w', encoding='utf-8') as f:
        f.write(HEAD.replace('{title}', t) + body + FOOT)
print('Pages rebuilt.')
