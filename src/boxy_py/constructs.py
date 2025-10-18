class BoxPad:
    def __init__(self, top: int, left: int, down: int, right: int):
        self.top: int = top
        self.left: int = left
        self.down: int = down
        self.right: int = right

    def uniform(self, pad: int) -> "BoxPad":
        return BoxPad(pad, pad, pad, pad)


def get_edges(boxtype: str | None = None):
    match boxtype:
        case "square":
            return ["┌", "┐", "└", "┘", "│", "─", "├", "┤", "┬", "┴", "┼"]
        case "rounded":
            return ["╮", "╭", "╯", "╰", "│", "─", "├", "┤", "┬", "┴", "┼"]
        case "double":
            return ["╗", "╔", "╝", "╚", "║", "═","╠", "╣", "╦", "╩", "╬"]
        case "bold":
            return ["┓", "┏", "┛", "┗", "┃", "━", "┣", "┫", "┳", "┻", "╋"]
        case "classic":
            return ["+", "+", "+", "+", "┇", "-", "+", "+", "+", "+", "+"]
        case "empty":
            return [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        case "boldEdges":
            return ["┓", "┏", "┛", "┗", "│", "─", "├", "┤", "┬", "┴", "┼"]
        case _:
            raise ValueError(f"Invalid box type: {boxtype}")
