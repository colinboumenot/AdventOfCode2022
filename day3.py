def main():
    part_one_text = open('inputtxt/day3input.txt', 'r')
    part_two_text = open('inputtxt/day3input.txt', 'r')
    part_one(part_one_text)
    part_two(part_two_text)

def get_value(letter):
    return ord(letter) - ord('a') + 1 if letter.islower() else ord(letter) - ord('A') + 27

def part_one(text_file):
    points = 0

    for line in text_file:
        middle = len(line) // 2
        combined, = set(line[:middle]) & set(line[middle:])
        points += get_value(combined)
    print(points)

def part_two(text_file):
    readable_text_file = text_file.read().strip().split("\n")
    points = 0

    for i in range(0, len(readable_text_file), 3):
        line_one, line_two, line_three = readable_text_file[i:i+3]
        combined, = set(line_one) & set(line_two) & set(line_three)
        points += get_value(combined)
    print(points)

if __name__ == "__main__":
    main()