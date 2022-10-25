def showNumbers(numbers):
    counter = 1
    for number in numbers:
        if counter % 2 == 0:
            print(number)
        counter += 1


listNumbers = [2, 34, 15, 19, 4, 16, 26, 65, 36, 23]

showNumbers(listNumbers)
