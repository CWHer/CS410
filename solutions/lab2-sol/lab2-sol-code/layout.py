import numpy as np

LAYOUTS = {
    "testMaze": "./examples/testMaze.lay",
    "tinyMaze": "./examples/tinyMaze.lay",

    "Maze_lab2_1_1": "./examples/Maze_lab2_1_1.lay",
    "Maze_lab2_1_2": "./examples/Maze_lab2_1_2.lay",
    "Maze_lab2_2_1": "./examples/Maze_lab2_2_1.lay",
    "Maze_lab2_3_1": "./examples/Maze_lab2_3_1.lay",
}


class Layout:
    def __init__(self, layout_name):
        self._raw_layout = self._process_file(LAYOUTS[layout_name])
        self._width = len(self._raw_layout[0])
        self._height= len(self._raw_layout)
        self._walls = np.zeros(shape=(self._width, self._height), dtype=bool)
        self._start, self._goal = None, None

        # Upside down.
        max_Y = self._height - 1
        for y in range(self._height):
            for x in range(self._width):
                char = self._raw_layout[max_Y - y][x]
                self._process_char(x, y, char)

        assert self._start is not None and self._goal is not None, "Starting point or destination not identified."

    @property
    def start(self):
        return self._start

    @property
    def goal(self):
        return self._goal

    def display(self):
        print("^y")
        for line in self._raw_layout:
            print("|" + line)
        print("0" + "-" * self._width + ">x")

    def is_wall(self, pos):
        x, y = pos
        return self._walls[x][y]

    @staticmethod
    def _process_file(layout_path):
        with open(layout_path) as f:
            raw_layout = [line.strip() for line in f]
        return raw_layout

    def _process_char(self, x, y, char):
        if char == '%':
            self._walls[x][y] = True
        elif char == 'G':
            self._goal = (x, y)
        elif char == 'S':
            self._start = (x, y)

    def __str__(self):
        return "\n".join(self._raw_layout)
