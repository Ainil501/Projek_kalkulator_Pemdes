import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget

from .calculator_boxlayout import CalculatorBox
from .calculator_gridlayout import CalculatorGrid


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Calculator")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)

        tabs.addTab(CalculatorBox(), "Box")
        tabs.addTab(CalculatorGrid(), "Grid")

        self.setCentralWidget(tabs)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
