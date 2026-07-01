import boxy_py
import time

# ── Basic smoke test ──────────────────────────────────────────────────────────

def test_basic():
    b = boxy_py.Boxy("single", "#00ffff")
    b.add_text_sgmt("Hello from Python!", "#ffffff", "center")
    lines = b.render(60)
    assert lines, "render() returned empty list"
    print("test_basic passed")
    for line in lines:
        print(line)

# ── Columnar layout ───────────────────────────────────────────────────────────

def test_columnar():
    b = boxy_py.Boxy("double", "#00ffff")
    b.add_text_sgmt("Project Status", "#ffffff", "center")
    b.add_col_text_sgmt("left", 3)
    b.add_col_text_line("Name",     "#aaaaaa", 0)
    b.add_col_text_line("Status",   "#aaaaaa", 1)
    b.add_col_text_line("Notes",    "#aaaaaa", 2)
    b.add_col_text_line("boxy-py",  "#ffffff", 0)
    b.add_col_text_line("Works",    "#32CD32", 1)
    b.add_col_text_line("pyo3 binding", "#ffffff", 2)
    b.set_segment_ratios(1, [1, 1, 2])
    lines = b.render(80)
    assert lines, "columnar render() returned empty list"
    print("test_columnar passed")
    for line in lines:
        print(line)

# ── Unicode ───────────────────────────────────────────────────────────────────

def test_unicode():
    b = boxy_py.Boxy("rounded", "#ff00ff")
    b.add_text_sgmt("日本語テスト 🦀 emoji", "#ffffff", "center")
    lines = b.render(60)
    assert lines, "unicode render() returned empty list"
    print("test_unicode passed")
    for line in lines:
        print(line)

# ── Benchmark ─────────────────────────────────────────────────────────────────

def benchmark(n: int = 1000):
    def build():
        b = boxy_py.Boxy("single", "#00ffff")
        b.add_text_sgmt("Benchmarking boxy-py bindings", "#ffffff", "center")
        b.add_text_sgmt("Second segment with more text to wrap across lines", "#aaaaaa", "left")
        b.add_col_text_sgmt("left", 2)
        b.add_col_text_line("Left col",  "#ffffff", 0)
        b.add_col_text_line("Right col", "#ffffff", 1)
        return b.render(80)

    # Warmup
    for _ in range(10):
        _ = build()

    start = time.perf_counter()
    for _ in range(n):
        _ = build()
    elapsed = time.perf_counter() - start

    print(f"benchmark: {n} renders in {elapsed:.3f}s  ({elapsed/n*1000:.3f}ms each)")

# ── Run ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    test_basic()
    print()
    test_columnar()
    print()
    test_unicode()
    print()
    benchmark(1000)
