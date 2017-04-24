def generate_triangle_numbers():
    triangle_numbers = []
    for i in range(10000):
        t_number = int(0.5 * i * (i + 1))
        triangle_numbers.append(t_number)
    return triangle_numbers


def check_if_triangle(number):
    triangle_numbers = generate_triangle_numbers()
    if number in triangle_numbers:
        return 1
    return 0


def calculate_word_value(word):
    word = str(word).upper()
    word_value = 0
    alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,'T': 20, 'U': 21, 'V': 22, 'W': 23,
                'X': 24, 'Y': 25, 'Z': 26}
    for i in range(len(word)):
        word_value += alphabet[word[i]]
    return word_value


def read_words(filename):
    word_list = []
    file = open(filename)
    for word in file.read().split(','):
        word_list.append(word.replace('"', ''))
    return word_list


def main():
    result = 0
    word_list = read_words('words.txt')
    for word in word_list:
        word_value = calculate_word_value(word)
        if check_if_triangle(word_value) == 1:
            result += 1
    print(result)

if __name__ == "__main__":
    main()
