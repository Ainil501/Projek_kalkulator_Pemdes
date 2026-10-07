from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from app.logic.calculator_engine import CalculatorEngine


def buat_tombol(teks, warna_bg, lebar_min=50, tinggi_min=50, font_size=20):
    """Helper untuk bikin tombol dengan style seragam, tapi tetap bisa
    membesar mengikuti ukuran window (responsive)."""
    tombol = QPushButton(teks)
    tombol.setMinimumSize(lebar_min, tinggi_min)
    tombol.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    tombol.setStyleSheet(f"""
        background-color: {warna_bg};
        color: #FFFFFF;
        border-radius: 8px;
        font-size: {font_size}px;
        font-weight: bold;
    """)
    return tombol


class CalculatorBox(QWidget):
    def __init__(self):
        super().__init__()
        self.engine = CalculatorEngine()

        lebar_min = 50
        tinggi_min = 50

        layout_main = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QHBoxLayout()

        # PERBAIKAN: Gunakan self.line agar menjadi atribut class
        self.line = QLineEdit()
        self.line.setReadOnly(True)
        self.line.setMinimumSize(200, tinggi_min)
        self.line.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        self.line.setStyleSheet("""
            background-color: #545454;
            color: #FFFFFF;
            border-radius: 8px;
            font-size: 22px;
        """)
        layout1.addWidget(self.line)  # Update ke self.line

        # Baris 2: tombol khusus + clear
        buttonKhusus1 = buat_tombol("x²", "#FF751F", lebar_min, tinggi_min)
        buttonKhusus2 = buat_tombol("1/x", "#FF751F", lebar_min, tinggi_min)
        buttonKhusus3 = buat_tombol("√x", "#FF751F", lebar_min, tinggi_min)
        button_C = buat_tombol("C", "#FF3131", lebar_min, tinggi_min)
        button_C.clicked.connect(self.hapus_semua)
        buttonKhusus1.clicked.connect(self.pangkat)
        buttonKhusus2.clicked.connect(self.respirokal)
        buttonKhusus3.clicked.connect(self.akar)

        layout2.addWidget(buttonKhusus1)
        layout2.addWidget(buttonKhusus2)
        layout2.addWidget(buttonKhusus3)
        layout2.addWidget(button_C)

        # Baris 3: bagi, kali, hasil
        button_bagi = buat_tombol("/", "#FF751F", lebar_min, tinggi_min)
        button_kali = buat_tombol("x", "#FF751F", lebar_min, tinggi_min)
        button_hasil = buat_tombol("=", "#00BF63", lebar_min * 2, tinggi_min)
        button_bagi.clicked.connect(lambda: self.tambah_ke_layar("/"))
        button_kali.clicked.connect(lambda: self.tambah_ke_layar("*"))
        button_hasil.clicked.connect(self.proses_hasil)

        layout3.addWidget(button_bagi, 1)
        layout3.addWidget(button_kali, 1)
        layout3.addWidget(button_hasil, 2)

        # Baris 4: 6, 7, 9, tambah
        button_6 = buat_tombol("6", "#545454", lebar_min, tinggi_min)
        button_7 = buat_tombol("7", "#545454", lebar_min, tinggi_min)
        button_9 = buat_tombol("9", "#545454", lebar_min, tinggi_min)
        button_tambah = buat_tombol("+", "#FF751F", lebar_min, tinggi_min)
        button_6.clicked.connect(lambda: self.tambah_ke_layar("6"))
        button_7.clicked.connect(lambda: self.tambah_ke_layar("7"))
        button_9.clicked.connect(lambda: self.tambah_ke_layar("9"))
        button_tambah.clicked.connect(lambda: self.tambah_ke_layar("+"))

        layout4.addWidget(button_6)
        layout4.addWidget(button_7)
        layout4.addWidget(button_9)
        layout4.addWidget(button_tambah)

        # Baris 5: 0, 1, 5, kurang
        button_0 = buat_tombol("0", "#545454", lebar_min, tinggi_min)
        button_1 = buat_tombol("1", "#545454", lebar_min, tinggi_min)
        button_5 = buat_tombol("5", "#545454", lebar_min, tinggi_min)
        button_kurang = buat_tombol("-", "#FF751F", lebar_min, tinggi_min)
        button_0.clicked.connect(lambda: self.tambah_ke_layar("0"))
        button_1.clicked.connect(lambda: self.tambah_ke_layar("1"))
        button_5.clicked.connect(lambda: self.tambah_ke_layar("5"))
        button_kurang.clicked.connect(lambda: self.tambah_ke_layar("-"))

        layout5.addWidget(button_0)
        layout5.addWidget(button_1)
        layout5.addWidget(button_5)
        layout5.addWidget(button_kurang)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #000000;")

        layout_main.addLayout(layout1)
        layout_main.addLayout(layout2)
        layout_main.addLayout(layout3)
        layout_main.addLayout(layout4)
        layout_main.addLayout(layout5)

        self.setLayout(layout_main)

    def tambah_ke_layar(self, karakter):
        self.line.setText(self.engine.tambah_karakter(karakter))

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

    def perbarui_layar(self):
        self.line.setText(self.engine.ekspresi)
