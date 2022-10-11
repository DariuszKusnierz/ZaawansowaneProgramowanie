import string


def helloFunc(name:str, surname:str) -> str:
    text = "Cześć {0} {1}" 
    return text.format(name, surname)

tekst = helloFunc("Dariusz", "Kuśnierz")
print(tekst)