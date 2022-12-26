from PyQt5.QtWidgets import QPushButton


class CPushButton(QPushButton):
    def __init__(self, parent):
        super(CPushButton, self).__init__(parent)
        self.current_color = "grey"
        self.make_grey()

    def cycle_color(self):
        if self.current_color == "red":
            self.make_green()
        elif self.current_color == "green":
            self.make_grey()
        elif self.current_color == "grey":
            self.make_red()

    def make_red(self):
        self.setStyleSheet("background-color: lightcoral")
        self.current_color = "red"

    def make_green(self):
        self.setStyleSheet("background-color: lightgreen")
        self.current_color = "green"

    def make_grey(self):
        self.setStyleSheet("background-color: lightgrey")
        self.current_color = "grey"
