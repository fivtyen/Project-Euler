# messy brute force, rather slow one


def get_next_number(number):
    next_number = 0
    for char in str(number):
        next_number += (int(char))**2
    return next_number


# returns chain for a given number
# stops at first '89' in a chain unless there isn't one then it goes to the end
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
    for i in range(1000):
        n = get_chain(i)
        if 89 in n:
            result += 1
    print(result)


if __name__ == "__main__":
    main()