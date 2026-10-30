# Yūgure for Sublime Text

A quiet twilight color scheme for Sublime Text 4.

Yūgure (夕暮れ) is Japanese for dusk. The scheme sits on a neutral near-black
ground with softened body text and six muted accents that each do one job, so
code reads dark without being flat and colourful without being loud.

The palette and its role mapping follow the [Yūgure theme for
Inkdrop](https://github.com/stoykotolev/inkdrop-yugure) by stoykotolev. Sibling
ports: [yugure.nvim](https://github.com/marshyunlee/yugure.nvim) and
[yugure-vscode](https://github.com/marshyunlee/yugure-vscode).

This is a color scheme (editor colors). The window chrome stays with whichever
UI theme you use; Adaptive matches the ground well.

## Install

With Package Control, until it is in the default channel: **Package Control:
Add Repository** → `https://github.com/marshyunlee/yugure-sublime`, then
**Package Control: Install Package** → `yugure-sublime`.

Or clone into your packages directory:

```sh
git clone https://github.com/marshyunlee/yugure-sublime "$HOME/Library/Application Support/Sublime Text/Packages/Yugure"
```

Then **Preferences → Select Color Scheme → Yūgure**, or in settings:

```json
{ "color_scheme": "Yugure.sublime-color-scheme" }
```

## Palette

Text and accent colors sit 0.04 higher in OKLCH lightness than the Inkdrop
table, for more contrast; hues, chroma and the grounds are unchanged.

| name    | hex       | role                                                 |
| ------- | --------- | ---------------------------------------------------- |
| base    | `#141518` | background                                           |
| surface | `#18191D` | popups                                               |
| low     | `#1B1C21` | current line                                         |
| overlay | `#1F2026` | inactive selection, guides, rulers                   |
| med     | `#2A2C34` | selection                                            |
| high    | `#383A43` | selection border, active guide, minimap border       |
| text    | `#A9B0BF` | body text, caret                                     |
| iron    | `#9BA3B3` | parameters, inactive selection text                  |
| subtle  | `#8B93A3` | punctuation, operators, fold markers                 |
| muted   | `#697083` | comments, quotes, deprecated                         |
| faint   | `#505563` | gutter numbers, invisibles                           |
| rose    | `#C6919C` | keywords, storage, tags, list bullets, h1            |
| gold    | `#CCAC83` | strings, find and bracket highlights, modified, h2   |
| foam    | `#86B0C2` | functions, links, accent, h3                         |
| teal    | `#87ACAB` | types, inline code, added, h4                        |
| iris    | `#A69AC6` | numbers, constants, attributes, decorators, h5       |
| love    | `#C7777C` | errors, deletions, misspellings, nothing else        |

The `region.*ish` scopes used by plugins (GitGutter, LSP, Sublime Linter) map
onto the same accents.

## Development

```sh
python3 scripts/check.py
```

The check parses the scheme as strict JSON, verifies every color is a palette
variable or hex, rejects duplicate scopes, and keeps `love` out of syntax
scopes.

## License

MIT. The palette is adapted from the Inkdrop theme's published color table.
