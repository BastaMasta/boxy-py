use boxy_cli::BoxPad;
use boxy_cli::boxer::{resolve_align, resolve_type};
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

#[pyclass]
struct Boxy {
    inner: boxy_cli::prelude::Boxy,
}

#[pymethods]
impl Boxy {
    #[new]
    fn new(box_type: &str, color: &str) -> Self {
        Self {
            inner: boxy_cli::prelude::Boxy::new(resolve_type(box_type.to_string()), color),
        }
    }

    fn add_text_sgmt(&mut self, data_string: &str, color: &str, text_align: &str) {
        self.inner
            .add_text_sgmt(data_string, color, resolve_align(text_align.to_string()));
    }

    pub fn add_col_text_sgmt(&mut self, align: &str, column_count: usize) -> PyResult<()> {
        if column_count == 0 {
            return Err(PyValueError::new_err("column_count must be at least 1"));
        }
        self.inner
            .add_col_text_sgmt(resolve_align(align.to_string()), column_count);
        Ok(())
    }

    pub fn add_text_line_indx(&mut self, data_string: &str, color: &str, seg_index: usize) {
        self.inner.add_text_line_indx(data_string, color, seg_index);
    }

    pub fn add_col_text_line_indx(
        &mut self,
        data_string: &str,
        color: &str,
        seg_index: usize,
        col_index: usize,
    ) {
        self.inner
            .add_col_text_line_indx(data_string, color, &seg_index, &col_index);
    }

    pub fn add_text_line(&mut self, data_string: &str, color: &str) {
        self.inner.add_text_line(data_string, color);
    }

    pub fn add_col_text_line(&mut self, data_string: &str, color: &str, col_index: usize) {
        self.inner.add_col_text_line(data_string, color, &col_index);
    }

    pub fn set_align(&mut self, align: &str) {
        self.inner.set_align(resolve_align(align.to_string()));
    }

    fn set_padding(&mut self, internal: usize, external: usize) {
        self.inner
            .set_padding(BoxPad::uniform(external), BoxPad::uniform(internal));
    }

    fn set_segment_ratios(&mut self, seg_index: usize, ratios: Vec<usize>) {
        self.inner.set_segment_ratios(seg_index, ratios);
    }

    fn render(&mut self, width: usize) -> Vec<String> {
        self.inner.render(width)
    }

    fn display(&mut self) {
        self.inner.display();
    }

    fn __repr__(&self) -> &str {
        "Boxy(...)"
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn boxy_py(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Boxy>()?;
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;
    Ok(())
}
