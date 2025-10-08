import re
import os
from typing import override
import boxy_py.constructs as constructs


def hex_to_rgb(hex_code: str) -> tuple[int, ...]:
    hex_code = hex_code.lstrip("#")
    return tuple(int(hex_code[i : i + 2], 16) for i in (0, 2, 4))


class BoxyPy:
    def __init__(self, boxtype: str, boxcolor: str) -> None:
        self.data: list[list[str]] = []
        self.colors: list[list[str]] = []
        self.seg_count: int = 0
        self.type: str = boxtype
        self.box_col: str = boxcolor
        self.align: list[str] = []

    def add_text_segment(self, text: str, text_col: str, text_align: str = "left"):
        self.data.append([text])
        self.colors.append([text_col])
        self.align.append(text_align)
        self.seg_count += 1

    def add_text_line(self, text: str, text_col: str):
        self.data[self.seg_count - 1].append(text)
        self.colors[self.seg_count - 1].append(text_col)

    def set(
        self,
        box_color: str | None = None,
        box_type: str | None = None,
        seg_align: str | None = None,
        seg_index: int | None = None,
    ):
        if box_color:
            self.box_col = box_color
        if box_type:
            self.type = box_type
        if seg_align and seg_index is not None and 0 <= seg_index < self.seg_count:
            self.align[seg_index] = seg_align

    def display(self):
        printable_length = os.get_terminal_size().columns - 2
        egde_pscs = constructs.get_edges()

    @override
    def __repr__(self) -> str:
        return f"BoxyPy(type: {self.type}, color: {self.box_col}, segments: {self.seg_count})"

    @override
    def __str__(self) -> str:
        return f"BoxyPy(type: {self.type}, color: {self.box_col}, segments: {self.seg_count})"
