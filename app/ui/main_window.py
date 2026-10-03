import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget
from PyQt6.QtGui import QAction, QKeySequence
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

        button_tambah = QAction("Tambah", self)
        button_kurang = QAction("Kurang", self)
        button_kali = QAction("Kali", self)
        button_bagi = QAction("Bagi", self)
        button_hasil = QAction("Hasil", self)
        button_C = QAction("Clear All", self)
        buttonKhusus1 = QAction("Kuadrat ", self)
        buttonKhusus2 = QAction("kebalikan", self)
        buttonKhusus3 = QAction("Akar kuadrat", self)

        button_tambah.setShortcut(QKeySequence("Ctrl+1"))
        button_kurang.setShortcut(QKeySequence("Ctrl+2"))
        button_kali.setShortcut(QKeySequence("Ctrl+3"))
        button_bagi.setShortcut(QKeySequence("Ctrl+4"))
        button_hasil.setShortcut(QKeySequence("Return"))
        button_C.setShortcut(QKeySequence("Delete"))
        buttonKhusus1.setShortcut(QKeySequence("Ctrl+5"))
        buttonKhusus2.setShortcut(QKeySequence("Ctrl+6"))
        buttonKhusus3.setShortcut(QKeySequence("Ctrl+7"))

        button_tambah.setStatusTip("Tambah (+)")
        button_kurang.setStatusTip("Kurang (-)")
        button_kali.setStatusTip("Kali (x)")
        button_bagi.setStatusTip("Bagi (/)")
        button_hasil.setStatusTip("Hasil (=)")
        button_C.setStatusTip("Clear All (C)")
        buttonKhusus1.setStatusTip("Kuadrat (x²)")
        buttonKhusus2.setStatusTip("kebalikan (1/x)")
        buttonKhusus3.setStatusTip("Akar kuadrat (√x)")
        
        menu = self.menuBar()

        file_menu = menu.addMenu("&Operasi matematika")
        file_menu.addSeparator()
        file_menu.addAction(button_tambah)
        file_menu.addAction(button_kurang)
        file_menu.addAction(button_kali)
        file_menu.addAction(button_bagi)
        file_menu.addAction(button_hasil)
        file_menu.addAction(button_C)
        file_menu.addAction(buttonKhusus1)
        file_menu.addAction(buttonKhusus2)
        file_menu.addAction(buttonKhusus3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
