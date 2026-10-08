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
        try:
            if self.ekspresi not in ("", "+", "-", "*", "/"):
                self.ekspresi = str(eval(self.ekspresi))
                return self.ekspresi
            return self.ekspresi
        except Exception:
            self.ekspresi = ""
            return "Error"

    def pangkat(self):
        if not self.ekspresi:
            return ""
        try:
            self.ekspresi = str(math.pow(int(self.ekspresi), 2))
            return self.ekspresi
        except Exception:
            self.ekspresi = ""
            return "Error"

    def resiprokal(self):
        if not self.ekspresi or self.ekspresi == "0":
            self.ekspresi = ""
            return "Error"
        try:
            self.ekspresi = str(eval(f"1/({self.ekspresi})"))
            return self.ekspresi
        except Exception:
            self.ekspresi = ""
            return "Error"

    def akar(self):
        if not self.ekspresi:
            return ""
        try:
            self.ekspresi = str(math.sqrt(int(self.ekspresi)))
            return self.ekspresi
        except Exception:
            self.ekspresi = ""
            return "Error"
