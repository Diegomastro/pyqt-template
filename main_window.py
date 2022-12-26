from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

# Cpushbutton is the overriden QPushButton, C for custom


class MainWindow(QMainWindow):
    path = None
    wins = 0
    losses = 0
    wb = None
    dialog = None
    mandando = False

    def __init__(self):
        super().__init__()

        # Setup window
        self.ui: QMainWindow = uic.loadUi("ui_mainwindow.ui")  # This line translates the designer file to python
        self.ui.setWindowTitle("Grid")

        # center
        frame_geometry = self.ui.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.ui.move(frame_geometry.topLeft())

        # Show or exec
        self.ui.show()

        # conectar signals a slot
        # noinspection PyUnresolvedReferences
        self.buttons = [self.ui.pushButton, self.ui.pushButton_2, self.ui.pushButton_3, self.ui.pushButton_4,
                        self.ui.pushButton_5, self.ui.pushButton_6, self.ui.pushButton_7, self.ui.pushButton_8,
                        self.ui.pushButton_9, self.ui.pushButton_10, self.ui.pushButton_11, self.ui.pushButton_12]

        self.costs = ["1", "1", "1", "1", "1", "1", "2", "2", "3", "4", "4", "5"]

        i: CPushButton
        j: str
        for i, j in zip(self.buttons, self.costs):
            i.clicked.connect(self.on_clicked)
            i.setText(j)
            font = i.font()
            font.setPointSize(40)
            i.setFont(font)

        # conectar signals a slots mas simple
#        self.ui.pushButton.clicked.connect(self.on_clicked())

    # noinspection PyTypeChecker
    def on_clicked(self):
        sender: CPushButton = self.sender()
        sender.cycle_color()
