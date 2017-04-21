def order_digits(number):
    number = str(number)
    ordered_digits = []
    for digit in number:
        ordered_digits.append(digit)
    ordered_digits.sort()
    return ordered_digits


def check_multiples(number):
    for i in range(2, 7):
        if order_digits(number) != order_digits(i * number):
            return 0
    return 1


def main():
    current_number = 1
    while True:
        if check_multiples(current_number) == 1:
            print(current_number)
            break
        else:
            current_number += 1

if __name__ == "__main__":
    main()

