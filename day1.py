def main():
    part_one_text = open('day1input.txt', 'r')
    part_two_text = open('day1input.txt', 'r')
    part_one(part_one_text)
    part_two(part_two_text)


def part_one(text_file):
    current = 0
    largest = 0

    for line in text_file.readlines():
        if line == "\n":
            if current > largest:
                largest = current
            current = 0
        else:
            current += int(line)
    print(largest)

def part_two(text_file):
    current = 0
    totals = []

    for line in text_file.readlines():
        if line == "\n":
            totals += [current]
            current = 0
        else:
            current += int(line)

    totals.sort()
    return_value = 0
    for x in totals[-3:]:
        return_value += x
    print(return_value)

if __name__ == "__main__":
    main()