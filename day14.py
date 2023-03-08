def main():
    part_one_text = open('inputtxt/day14input.txt', 'r')
    part_two_text = open('inputtxt/day14input.txt', 'r')
    ##part_one(part_one_text)
    part_two(part_two_text)

def part_one(text_file):
    item_set = set()
    item = 0

    for line in text_file:
        x = [list(map(int, y.split(","))) for y in line.strip().split(" -> ")]
        for (x1, y1), (x2, y2) in zip(x, x[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    item_set.add(x + y * 1j)
                    item = max(item , y + 1)

    time = 0

    while True:
        s = 500
        while True:
            if s.imag >= item:
                print(time)
                exit(0)
            if s + 1j not in item_set:
                s += 1j
                continue
            if s + 1j - 1 not in item_set:
                s += 1j - 1
                continue
            if s + 1j + 1 not in item_set:
                s += 1j + 1
                continue
            item_set.add(s)
            time += 1
            break



def part_two(text_file):
    item_set = set()
    item = 0

    for line in text_file:
        x = [list(map(int, y.split(","))) for y in line.strip().split(" -> ")]
        for (x1, y1), (x2, y2) in zip(x, x[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    item_set.add(x + y * 1j)
                    item = max(item, y + 1)
    time = 0
    while 500 not in item_set:
        s = 500
        while True:
            if s.imag >= item:
                break
            if s + 1j not in item_set:
                s += 1j
                continue
            if s + 1j - 1 not in item_set:
                s += 1j - 1
                continue
            if s + 1j + 1 not in item_set:
                s += 1j + 1
                continue
            break
        item_set.add(s)
        time += 1

    print(time)


if __name__ == "__main__":
    main()