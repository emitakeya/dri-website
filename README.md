# PT Duta Retail Indonesia — company website

Static site (no build step) for PT Duta Retail Indonesia (DRI), Daisei Group. Indonesian, English and Japanese.

- `index.html` — home: about, businesses & brands, products & prices, how to order, contact
- `terms.html`, `privacy.html`, `refund.html` — policy pages
- `assets/` — styles, language switcher, logo

## Editing
Page text lives in `_src/` (`*_body.html` per page; shared header/footer and contact details in `partials.py`).
Edit there, run `python3 _src/build.py` to regenerate the HTML files, and commit both.
Each text appears three times: `data-l="id"`, `data-l="en"`, `data-l="ja"`.

`_src/` is excluded from the deployed site (`.vercelignore`).
