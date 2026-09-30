def hitung(ekspresi):
    if ekspresi not in ("", "+", "-", "*", "/"):
        return str(eval(ekspresi))
    else:
        return "Error"
