def multipleNumbersWithFor(numbers):
    newNumbers = []
    for multiple in numbers:
        newNumbers.append(multiple * 2)
    return newNumbers


listNumber = [1, 2, 7, 3, 9]

print(multipleNumbersWithFor(listNumber))


def multipleNumbers(numbers):
    newNumbers = [multiple * 2 for multiple in numbers]

    return newNumbers


listNumber = [1, 2, 7, 3, 9]

print(multipleNumbers(listNumber))
