class Boxxy:
    def __init__(self, title, previous, data, style="single", padding=0):
        self._title = title
        self._prev = previous
        self._data = data
        self._style = style
        self._padding = padding

        # Draw box on initialize
        self.draw_box()

    def draw_box(self):

        styles = {
            "single": {
                "topLeft": "┌",
                "topRight": "┐",
                "bottomRight": "┘",
                "bottomLeft": "└",
                "vertical": "│",
                "horizontal": "─"
            },
            "double": {
                "topLeft": "╔",
                "topRight": "╗",
                "bottomRight": "╝",
                "bottomLeft": "╚",
                "vertical": "║",
                "horizontal": "═"
            },
            "round": {
                "topLeft": "╭",
                "topRight": "╮",
                "bottomRight": "╯",
                "bottomLeft": "╰",
                "vertical": "│",
                "horizontal": "─"
            },
            "single-double": {
                "topLeft": "╓",
                "topRight": "╖",
                "bottomRight": "╜",
                "bottomLeft": "╙",
                "vertical": "║",
                "horizontal": "─"
            },
            "double-single": {
                "topLeft": "╒",
                "topRight": "╕",
                "bottomRight": "╛",
                "bottomLeft": "╘",
                "vertical": "│",
                "horizontal": "═"
            },
            "classic": {
                "topLeft": "+",
                "topRight": "+",
                "bottomRight": "+",
                "bottomLeft": "+",
                "vertical": "|",
                "horizontal": "-"
            }
        }

        vertical = styles.get(self._style).get("vertical")
        horizontal = styles.get(self._style).get("horizontal")
        corner_top_l = styles.get(self._style).get("topLeft")
        corner_top_r = styles.get(self._style).get("topRight")
        corner_bot_l = styles.get(self._style).get("bottomLeft")
        corner_bot_r = styles.get(self._style).get("bottomRight")
        padding = self._padding

        horizontal_count = self.largest_data(
            self._title, self._prev, self._data)

        # print top
        print(corner_top_l, horizontal*(horizontal_count +
              padding), corner_top_r, sep="")

        # Print Title
        print(vertical, self._title.center(
            horizontal_count+padding), vertical, sep="")

        # Print Seperator
        print(vertical, horizontal*(horizontal_count+padding), vertical, sep="")

        # Print middle
        for entry in self._data:
            print(vertical, entry.ljust(
                horizontal_count+padding), vertical, sep="")

        # Print Seperator
        print(vertical, horizontal*(horizontal_count+padding), vertical, sep="")

        # Print Previous
        print(vertical, self._prev.ljust(
            horizontal_count+padding), vertical, sep="")

        # print bottom
        print(corner_bot_l, horizontal*(horizontal_count +
              padding), corner_bot_r, sep="")

    # Returns length of largest string that belongs in box
    def largest_data(self, title, prev, data):
        largest_entry = 1

        # Find largest entry
        for entry in data:
            if (len(entry) > largest_entry):
                largest_entry = len(entry)
        # Check Title
        if (len(title) > largest_entry):
            largest_entry = len(title)
        # Check Prev
        if (len(prev) > largest_entry):
            largest_entry = len(prev)
        return largest_entry
