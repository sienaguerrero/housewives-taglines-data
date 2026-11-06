# housewives-taglines data

Every opening-credits tagline from the Real Housewives franchises, as structured data. This is the dataset behind [notafriendof.siena.codes](https://notafriendof.siena.codes), which also serves it as a [JSON API](https://notafriendof.siena.codes/v2/index.json).

## Files

| File | What it is |
|---|---|
| `data/taglines.json` | The dataset: franchises, eras, seasons, housewives and their taglines |
| `data/taglines.csv` | The same taglines flattened, one row per season per housewife |
| `data/schema.json` | JSON Schema for `taglines.json` |
| `script/check_schema.py` | Checks `taglines.json` against the schema |
| `CHANGELOG.md` | One line per data version, and what each kind of bump means |
| `SOURCES.md` | Where each franchise's taglines came from |

```sh
pip install jsonschema && python3 script/check_schema.py
```

## Data model

Taglines nest under the housewife, because the housewife is the stable entity and a season is just an occasion on which she said something. `seasons` is an array, not an integer: a tagline that ran unchanged across several seasons is stored once, with every season it covered.

Every franchise, era, housewife and tagline has an `id` of three show-themed words, like `sequin-reunion-clutch`. It never changes, even when a name, slug or season is corrected, so it is the safe thing to link to.

## Versions

Each commit here is one data version, tagged `data-vX.Y.Z`, so `git show data-v1.11.0:data/taglines.json` returns exactly what shipped. The first commit is 1.11.0. `CHANGELOG.md` covers every version, including the earlier ones.

This repository is published from a private one where the data is edited and checked, so pull requests here can't be merged. Spotted a typo? [Open an issue](https://github.com/sienaguerrero/housewives-taglines-data/issues/new/choose). Anything else goes to [notafriendof@siena.codes](mailto:notafriendof@siena.codes).

## License

The code in `script/` and the schema in `data/schema.json` are MIT licensed. The tagline text is quoted from Bravo's programming and is not ours to license. See `LICENSE` and `SOURCES.md`.

Unofficial. Not affiliated with, sponsored by, or endorsed by Bravo or NBCUniversal.

Taglines are short phrases, which the U.S. Copyright Office lists as material not subject to copyright: [37 CFR 202.1(a)](https://www.ecfr.gov/current/title-37/chapter-II/subchapter-A/part-202/section-202.1), and [Circular 33, *Works Not Protected by Copyright*](https://www.copyright.gov/circs/circ33.pdf).

Using real people’s names in factual reference material is protected.

Takedown notices and our responses are published in `TAKEDOWNS.md`.
