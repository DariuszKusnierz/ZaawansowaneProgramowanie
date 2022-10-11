def CheckNumber(number:int) -> bool:
    return number%2 == 0

isEven = CheckNumber(8)

if isEven:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")