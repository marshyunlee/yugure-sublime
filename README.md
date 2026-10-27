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

| name    | hex       | role                                                 |
| ------- | --------- | ---------------------------------------------------- |
| base    | `#141518` | background                                           |
| surface | `#18191D` | popups                                               |
| low     | `#1B1C21` | current line                                         |
| overlay | `#1F2026` | inactive selection, guides, rulers                   |
| med     | `#2A2C34` | selection                                            |
| high    | `#383A43` | selection border, active guide, minimap border       |
| text    | `#9DA4B2` | body text, caret                                     |
| iron    | `#8F97A6` | parameters, inactive selection text                  |
| subtle  | `#7F8797` | punctuation, operators, fold markers                 |
| muted   | `#5E6577` | comments, quotes, deprecated                         |
| faint   | `#454A58` | gutter numbers, invisibles                           |
| rose    | `#B98590` | keywords, storage, tags, list bullets, h1            |
| gold    | `#BFA077` | strings, find and bracket highlights, modified, h2   |
| foam    | `#7AA3B5` | functions, links, accent, h3                         |
| teal    | `#7BA09F` | types, inline code, added, h4                        |
| iris    | `#9A8EB9` | numbers, constants, attributes, decorators, h5       |
| love    | `#BA6B70` | errors, deletions, misspellings, nothing else        |

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

MIT. The palette is reproduced from the Inkdrop theme's published color table.
