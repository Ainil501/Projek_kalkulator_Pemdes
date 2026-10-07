from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QLineEdit, QPushButton, QSizePolicy, QWidget

from app.logic.calculator_engine import CalculatorEngine


class CalculatorGrid(QWidget):
    def __init__(self):
        super().__init__()
        self.engine = CalculatorEngine()

        self.setStyleSheet("background:#000;")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        grid = QGridLayout()
        self.line = QLineEdit()
        self.line.setReadOnly(True)
        self.line.setMinimumSize(200, 50)
        self.line.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        self.line.setStyleSheet(
            "background:#545454;color:white;border-radius:8px;font-size:22px;"
        )
        grid.addWidget(self.line, 0, 0, 1, 4)

        data = [
            ("x²", 1, 0),
            ("1/x", 1, 1),
            ("√x", 1, 2),
            ("C", 1, 3),
            ("/", 2, 0),
            ("x", 2, 1),
            ("=", 2, 2),
            ("6", 3, 0),
            ("7", 3, 1),
            ("9", 3, 2),
            ("+", 3, 3),
            ("0", 4, 0),
            ("1", 4, 1),
            ("5", 4, 2),
            ("-", 4, 3),
        ]

        for t, r, c in data:
            b = QPushButton(t)
            b.setMinimumSize(50, 50)
            b.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            warna = (
                "#FF3131"
                if t == "C"
                else "#00BF63"
                if t == "="
                else "#FF751F"
                if t in ("x²", "1/x", "√x", "/", "+", "-", "x")
                else "#545454"
            )
            b.setStyleSheet(
                f"background:{warna};color:white;border-radius:8px;font-size:20px;font-weight:bold;"
            )
            if t == "C":
                b.clicked.connect(self.hapus_semua)
            elif t == "x²":
                b.clicked.connect(self.pangkat)
            elif t == "1/x":
                b.clicked.connect(self.respirokal)
            elif t == "√x":
                b.clicked.connect(self.akar)
            elif t == "=":
                b.clicked.connect(self.proses_hasil)
                grid.addWidget(b, r, c, 1, 2)
                continue
            else:
                b.clicked.connect(
                    lambda _, k="*" if t == "x" else t: self.tambah_ke_layar(k)
                )
            grid.addWidget(b, r, c)

        self.setLayout(grid)

    def tambah_ke_layar(self, k):
        self.line.setText(self.engine.tambah_karakter(k))

    def hapus_semua(self):
        self.line.setText(self.engine.hapus_semua())

    def proses_hasil(self):
        self.line.setText(self.engine.proses_hasil())

    def pangkat(self):
        self.line.setText(self.engine.pangkat())

    def respirokal(self):
        self.line.setText(self.engine.respirokal())

    def akar(self):
        self.line.setText(self.engine.akar())
