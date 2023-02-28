def main():
    part_one_text = open('inputtxt/day6input.txt', 'r')
    part_two_text = open('inputtxt/day6input.txt', 'r')
    part_one(part_one_text)
    part_two(part_two_text)

def part_one(text_file):
    text = text_file.read()
    for x in range(4, len(text)):
        y = text[x-4:x]
        if len(set(y)) == 4:
            print(x)
            return

def part_two(text_file):
    text = text_file.read()
    for x in range(14, len(text)):
        y = text[x - 14:x]
        if len(set(y)) == 14:
            print(x)
            return
if __name__ == "__main__":
    main()