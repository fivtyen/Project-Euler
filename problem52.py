def orderDigits(number):
    number = str(number)
    orderedDigits = []
    for digit in number:
        orderedDigits.append(digit)
    orderedDigits.sort()
    return orderedDigits


def checkMultis(number):
    for i in range(2, 7):
        if orderDigits(number) != orderDigits(i * number):
            return 0
    return 1


def main():
    currentNumber = 1
    while True:
        print(currentNumber)
        if checkMultis(currentNumber) == 1:
            print(currentNumber)
            break
        else:
            currentNumber += 1

if __name__ == "__main__":
    main()

