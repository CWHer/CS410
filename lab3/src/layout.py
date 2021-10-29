import numpy as np

LAYOUTS = {
    "classroom": {
        "fail": "./examples/classroom/fail.lay",
        "easy": "./examples/classroom/easy.lay",
        "harder": "./examples/classroom/harder.lay",
        "hardest": "./examples/classroom/hardest.lay",
    },
    "sudoku": {
        "easy": "./examples/sudoku/easy.lay",
        "harder": "./examples/sudoku/harder.lay",
        "hardest": "./examples/sudoku/hardest.lay"
    }
}


class Layout:
    def __init__(self, layout_type, layout_name):
        self._raw_layout = self._process_file(
            LAYOUTS[layout_type][layout_name])
        self.width = len(self._raw_layout[0].split())
        self.height = len(self._raw_layout)
        self.matrix = np.array([i.split() for i in self._raw_layout])
        # for i in range(self.height):
        #     for j in range(self.width):
        #         self.vanilla_matrix[i][j] = int(self.vanilla_matrix[i][j])

    def display(self):
        print("^y")
        for line in self._raw_layout:
            print("|" + line)
        print("0" + "-" * self.width + ">x")

    @staticmethod
    def _process_file(layout_path):
        with open(layout_path) as f:
            raw_layout = [line.strip() for line in f]
        return raw_layout

    def __str__(self):
        return "\n".join(self._raw_layout)
