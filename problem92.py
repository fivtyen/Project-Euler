#messy bruteforce, rather slow one

def get_digits(number):
    s_number = str(number)
    digits = []
    for char in s_number:
        digits.append(int(char))
    return digits


def get_next_number(number):
    digits = get_digits(number)
    squared = 0
    for digit in digits:
        squared += digit**2
    return squared


def get_chain(start_number):
    chain = [start_number]
    current_number = start_number
    while True:
        next_number = get_next_number(current_number)
        if next_number == 89:
            chain.append(next_number)
            return chain
        if next_number in chain:
            chain.append(next_number)
            return chain
        current_number = next_number
        chain.append(current_number)


def main():
    result = 0
    for i in range(10**7):
        if i % 100000 == 0:
            print(i)
        n = get_chain(i)
        if 89 in n:
            result += 1
    print(result)


if __name__ == "__main__":
    main()