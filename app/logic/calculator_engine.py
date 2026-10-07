import math


class CalculatorEngine:
    def __init__(self):
        self.ekspresi = ""

    def tambah_karakter(self, karakter):
        self.ekspresi += karakter
        return self.ekspresi

    def hapus_semua(self):
        self.ekspresi = ""
        return self.ekspresi

    def proses_hasil(self):
        if self.ekspresi not in ("", "+", "-", "*", "/"):
            return str(eval(self.ekspresi))
        return self.ekspresi

    def pangkat(self):
        if not self.ekspresi:
            return ""
        self.ekspresi = str(math.pow(int(self.ekspresi), 2))
        return self.ekspresi

    def respirokal(self):
        if not self.ekspresi:
            return ""
        elif self.ekspresi == "0":
            self.ekspresi = ""
            return "Error"
        self.ekspresi = str(eval(f"1/({self.ekspresi})"))
        return self.ekspresi

    def akar(self):
        if not self.ekspresi:
            return ""
        self.ekspresi = str(math.sqrt(int(self.ekspresi)))
        return self.ekspresi
