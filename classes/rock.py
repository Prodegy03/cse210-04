from fallingitem import falling_item


class rock(falling_item):
    def __init__(self):
        """Rocks"""
        super().__init__()
        self._text = "O"