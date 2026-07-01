# boxy-py

Python bindings for [`boxy-cli`](https://github.com/BastaMasta/boxy-cli), a Rust crate
for creating styled terminal boxes with multi-segment layouts, columnar grids, true-color
borders, and full Unicode support.

All rendering logic lives in the Rust crate — this package is a thin PyO3 wrapper.
Performance is near-native; bug fixes and features in `boxy-cli` propagate here on the
next release.

## Install

```bash
pip install boxy-py
```

## Quick Start

```python
import boxy_py

b = boxy_py.Boxy("double", "#00ffff")
b.add_text_sgmt("Hello from Python!", "#ffffff", "center")
b.add_text_sgmt("Powered by boxy-cli", "#32CD32", "left")

# render() returns list[str] — print, pipe, buffer, whatever you want
for line in b.render(60):
    print(line)

# or print directly, auto-sized to the current terminal width
b.display()
```

## Columnar Layout

```python
import boxy_py

b = boxy_py.Boxy("single", "#00ffff")
b.add_text_sgmt("Project Status", "#ffffff", "center")
b.add_col_text_sgmt("left", 3)
b.add_col_text_line("Name",     "#aaaaaa", 0)
b.add_col_text_line("Status",   "#aaaaaa", 1)
b.add_col_text_line("Notes",    "#aaaaaa", 2)
b.add_col_text_line("boxy-py",  "#ffffff", 0)
b.add_col_text_line("Works",    "#32CD32", 1)
b.add_col_text_line("PyO3 binding", "#ffffff", 2)
b.set_segment_ratios(1, [1, 1, 2])
b.display()
```

## API Reference

### `Boxy(box_type, color)`
Create a new box.
- `box_type`: `"classic"`/`"c"`, `"single"`/`"s"`, `"double"`/`"d"`, `"double_horizontal"`/`"dh"`, `"double_vertical"`/`"dv"`, `"bold"`/`"b"`, `"rounded"`/`"r"`, `"bold_corners"`/`"bc"`, `"empty"`/`"e"`
- `color`: hex color string for the border, e.g. `"#00ffff"`

### Text segments
| Method | Description |
|---|---|
| `add_text_sgmt(text, color, align)` | Add a new text segment |
| `add_text_line(text, color)` | Append a line to the last segment |
| `add_text_line_indx(text, color, seg_index)` | Append a line to a specific segment |

### Columnar segments
| Method | Description |
|---|---|
| `add_col_text_sgmt(align, column_count)` | Add a new columnar segment |
| `add_col_text_line(text, color, col_index)` | Add a line to a column in the last segment |
| `add_col_text_line_indx(text, color, seg_index, col_index)` | Add a line to a column in a specific segment |
| `set_segment_ratios(seg_index, ratios)` | Set relative column widths, e.g. `[1, 2, 1]` |

### Layout
| Method | Description |
|---|---|
| `set_align(align)` | Set alignment for the last segment: `"left"`, `"center"`, `"right"` |
| `set_padding(internal, external)` | Set uniform padding inside and outside the border |

### Rendering
| Method | Description |
|---|---|
| `render(width)` | Render into `list[str]` at a given column width |
| `display()` | Render and print directly to stdout, auto-sized to terminal |

## Unicode Support

Full Unicode support inherited from `boxy-cli`:
- Grapheme-cluster-aware word wrapping — emoji sequences and combining marks are never split
- Display-width-correct alignment for CJK text and emoji

**Note:** ZWJ sequences (e.g. 👨‍👩‍👧) may display with slightly incorrect padding on some
terminals due to disagreements between the Unicode standard and individual terminal
emulators on ZWJ rendering width. Plain emoji (🦀, 🚀) and CJK text are unaffected.

## Performance

~0.1ms per render for typical boxes — roughly 50–100x faster than equivalent `rich`
Panel output, since all rendering happens in native Rust.

## License

MIT OR Apache-2.0