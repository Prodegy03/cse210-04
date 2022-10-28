from fallingitem import falling_item

class gem(falling_item):
    def __init__(self):
        """Gems"""
        super().__init__()
        self._text = "*"