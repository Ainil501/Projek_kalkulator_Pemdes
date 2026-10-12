import math


class CalculatorEngine:
    def __init__(self):
        self.inputan = ""

    def tambah_karakter(self, karakter):
        if karakter in ("+", "-", "*", "/"):
            if self.inputan == "":
                return self.inputan
            if self.inputan[-1] in ("+", "-", "*", "/"):
                self.inputan = self.inputan[:-1]
        elif self.inputan == "0" or self.inputan[-2:] in ("+0", "-0", "*0", "/0"):
            self.inputan = self.inputan[:-1]

        self.inputan += karakter
        return self.inputan

    def hapus_semua(self):
        self.inputan = ""
        return self.inputan

    def rapikan(self, nilai):
        if nilai == int(nilai):
            return str(int(nilai))
        return str(round(nilai, 6))

    def proses_hasil(self):
        try:
            if self.inputan not in ("", "+", "-", "*", "/"):
                self.inputan = self.rapikan(eval(self.inputan))
                return self.inputan
            return self.inputan
        except Exception:
            self.inputan = ""
            return "Error"

    def pangkat(self):
        if not self.inputan:
            return ""
        try:
            self.proses_hasil()
            self.inputan = self.rapikan(math.pow(float(self.inputan), 2))
            return self.inputan
        except Exception:
            self.inputan = ""
            return "Error"

    def resiprokal(self):
        if not self.inputan or self.inputan == "0":
            self.inputan = ""
            return "Error"
        try:
            self.proses_hasil()
            self.inputan = self.rapikan(1 / float(self.inputan))
            return self.inputan
        except Exception:
            self.inputan = ""
            return "Error"

    def akar(self):
        if not self.inputan:
            return ""
        try:
            self.proses_hasil()
            self.inputan = self.rapikan(math.sqrt(float(self.inputan)))
            return self.inputan
        except Exception:
            self.inputan = ""
            return "Error"
