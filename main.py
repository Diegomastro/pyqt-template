# I'd say never touch this file

import sys
from PyQt5.QtWidgets import QApplication

from main_window import MainWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication([])
    win = MainWindow()

    app.exec()
