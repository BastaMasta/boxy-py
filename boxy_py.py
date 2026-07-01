"""Python bindings for boxy-cli — styled terminal boxes in Python."""


class Boxy:
    """A styled terminal box with multi-segment layouts, columnar grids,
    true-color borders, Unicode box-drawing, and word wrapping.

    Args:
        box_type: Border style. One of ``"classic"``/``"c"``, ``"single"``/``"s"``,
            ``"double"``/``"d"``, ``"double_horizontal"``/``"dh"``,
            ``"double_vertical"``/``"dv"``, ``"bold"``/``"b"``,
            ``"rounded"``/``"r"``, ``"bold_corners"``/``"bc"``, ``"empty"``/``"e"``.
        color: Hex color string for the border, e.g. ``"#00ffff"``.

    Example:
        >>> import boxy_py
        >>> b = boxy_py.Boxy("double", "#00ffff")
        >>> b.add_text_sgmt("Hello!", "#ffffff", "center")
        >>> b.display()
    """

    def __init__(self, box_type: str, color: str) -> None: ...
    def add_text_sgmt(self, text: str, color: str, align: str) -> None:
        """Add a new text segment to the box.

        Each call adds a new section separated from the previous by a divider.
        Text is word-wrapped automatically to fit the box width.

        Args:
            text: The text content for this segment.
            color: Hex color string for this segment's text, e.g. ``"#ffffff"``.
            align: One of ``"left"``, ``"center"``, ``"right"``.
        """
        ...

    def add_text_line(self, text: str, color: str) -> None:
        """Append a line to the most recently added text segment.

        Args:
            text: The text content for the new line.
            color: Hex color string for this line's text.
        """
        ...

    def add_text_line_indx(self, text: str, color: str, seg_index: int) -> None:
        """Append a line to a text segment at a specific index.

        Args:
            text: The text content for the new line.
            color: Hex color string for this line's text.
            seg_index: Zero-based index of the segment to append to.
        """
        ...

    def add_col_text_sgmt(self, align: str, column_count: int) -> None:
        """Add a new columnar segment to the box.

        Columnar segments place content side-by-side. Use ``set_segment_ratios``
        to control relative column widths.

        Args:
            align: One of ``"left"``, ``"center"``, ``"right"`` — applies to all columns.
            column_count: Number of columns. Must be at least 1.

        Raises:
            ValueError: If ``column_count`` is 0.
        """
        ...

    def add_col_text_line(self, text: str, color: str, col_index: int) -> None:
        """Add a line to a column in the most recently added columnar segment.

        Args:
            text: The text content for this cell.
            color: Hex color string for this cell's text.
            col_index: Zero-based column index.
        """
        ...

    def add_col_text_line_indx(
        self, text: str, color: str, seg_index: int, col_index: int
    ) -> None:
        """Add a line to a column in a specific columnar segment.

        Args:
            text: The text content for this cell.
            color: Hex color string for this cell's text.
            seg_index: Zero-based index of the columnar segment.
            col_index: Zero-based column index.
        """
        ...

    def set_align(self, align: str) -> None:
        """Set the text alignment for the most recently added segment.

        Args:
            align: One of ``"left"``, ``"center"``, ``"right"``.
        """
        ...

    def set_padding(self, internal: int, external: int) -> None:
        """Set uniform padding for the box.

        Args:
            internal: Padding in columns between the border and the text.
            external: Padding in columns between the terminal edge and the border.
        """
        ...

    def set_segment_ratios(self, seg_index: int, ratios: list[int]) -> None:
        """Set relative column width ratios for a columnar segment.

        Args:
            seg_index: Zero-based index of the columnar segment to adjust.
            ratios: One ratio value per column. ``[1, 2, 1]`` gives the middle
                column twice the width of the outer columns.
        """
        ...

    def render(self, width: int) -> list[str]:
        """Render the box into a list of strings without printing.

        Args:
            width: Total column width to render into.

        Returns:
            One fully-composed terminal line per entry, including ANSI color
            codes and box-drawing characters.
        """
        ...

    def display(self) -> None:
        """Render and print the box directly to stdout.

        Auto-sizes to the current terminal width. Use ``render()`` instead
        if you need the output as a list of strings.
        """
        ...


__version__: str
"""Version of the installed boxy-py package."""
