from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QSizePolicy
)
from PyQt6.QtCore import Qt


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

        lebar_min = 50
        tinggi_min = 50

        layout_main = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QHBoxLayout()

        # Layar / tampilan angka
        line = QLineEdit()
        line.setMinimumSize(200, tinggi_min)
        line.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        line.setStyleSheet("""
            background-color: #545454;
            color: #FFFFFF;
            border-radius: 8px;
            font-size: 22px;
        """)
        layout1.addWidget(line)

        # Baris 2: tombol khusus + clear
        buttonKhusus1 = buat_tombol("K", "#FF751F", lebar_min, tinggi_min)
        buttonKhusus2 = buat_tombol("K", "#FF751F", lebar_min, tinggi_min)
        buttonKhusus3 = buat_tombol("K", "#FF751F", lebar_min, tinggi_min)
        button_C = buat_tombol("C", "#FF3131", lebar_min, tinggi_min)

        layout2.addWidget(buttonKhusus1)
        layout2.addWidget(buttonKhusus2)
        layout2.addWidget(buttonKhusus3)
        layout2.addWidget(button_C)

        # Baris 3: bagi, kali, hasil (hasil 2x lebih lebar)
        button_bagi = buat_tombol("/", "#FF751F", lebar_min, tinggi_min)
        button_kali = buat_tombol("x", "#FF751F", lebar_min, tinggi_min)
        button_hasil = buat_tombol("=", "#00BF63", lebar_min * 2, tinggi_min)

        # stretch factor: hasil dapat jatah 2x lebih lebar dari tombol lain
        layout3.addWidget(button_bagi, 1)
        layout3.addWidget(button_kali, 1)
        layout3.addWidget(button_hasil, 2)

        # Baris 4: 6, 7, 9, tambah
        button_6 = buat_tombol("6", "#545454", lebar_min, tinggi_min)
        button_7 = buat_tombol("7", "#545454", lebar_min, tinggi_min)
        button_9 = buat_tombol("9", "#545454", lebar_min, tinggi_min)
        button_tambah = buat_tombol("+", "#FF751F", lebar_min, tinggi_min)

        layout4.addWidget(button_6)
        layout4.addWidget(button_7)
        layout4.addWidget(button_9)
        layout4.addWidget(button_tambah)

        # Baris 5: 0, 1, 5, kurang
        button_0 = buat_tombol("0", "#545454", lebar_min, tinggi_min)
        button_1 = buat_tombol("1", "#545454", lebar_min, tinggi_min)
        button_5 = buat_tombol("5", "#545454", lebar_min, tinggi_min)
        button_kurang = buat_tombol("-", "#FF751F", lebar_min, tinggi_min)

        layout5.addWidget(button_0)
        layout5.addWidget(button_1)
        layout5.addWidget(button_5)
        layout5.addWidget(button_kurang)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #000000;")  # warna background aplikasi

        layout_main.addLayout(layout1)
        layout_main.addLayout(layout2)
        layout_main.addLayout(layout3)
        layout_main.addLayout(layout4)
        layout_main.addLayout(layout5)

        self.setLayout(layout_main)
