
def main():
    part_one_text = open('inputtxt/day11input.txt', 'r')
    part_two_text = open('inputtxt/day11input.txt', 'r')
    part_one(part_one_text)
    part_two(part_two_text)

def part_one(text_file):
    text = text_file.read().splitlines()
    monkey_ops = [(text[x][23:]) for x in range(2, len(text), 7)]
    monkey_test = [int(text[x][21:]) for x in range(3, len(text), 7)]
    monkey_conditions = [[int(text[x][29:]), int(text[x+1][30:])] for x in range(4, len(text), 7)]
    mod = 1
    for x in monkey_test:
        mod *= x
    inspections = [0 for _ in range(len(monkey_test))]
    items = [[[int(x) for x in (text[y][18:]).split(", ")] for y in range(1, len(text), 7)]][0]
    for _ in range(0, 20):
        for x in range(0, len(inspections)):
            for y in range(0, len(items[x])):
                current = items[x][y]
                if monkey_ops[x] == "* old":
                    current *= current
                elif monkey_ops[x][:2] == "* ":
                    current *= int(monkey_ops[x][2:])
                elif monkey_ops[x][:2] == "+ ":
                    current += int(monkey_ops[x][2:])
                current = current // 3
                if current % monkey_test[x] == 0:
                    items[monkey_conditions[x][0]].append(current)
                else:
                    items[monkey_conditions[x][1]].append(current)
                inspections[x] += 1
            items[x] = []
    print(sorted(inspections)[-1]*sorted(inspections)[-2])

def part_two(text_file):
    text = text_file.read().splitlines()
    monkey_ops = [(text[x][23:]) for x in range(2, len(text), 7)]
    monkey_test = [int(text[x][21:]) for x in range(3, len(text), 7)]
    monkey_conditions = [[int(text[x][29:]), int(text[x + 1][30:])] for x in range(4, len(text), 7)]
    mod = 1
    for x in monkey_test:
        mod *= x
    inspections = [0 for _ in range(len(monkey_test))]
    items = [[[int(x) for x in (text[y][18:]).split(", ")] for y in range(1, len(text), 7)]][0]
    for _ in range(0, 10000):
        for x in range(0, len(inspections)):
            for y in range(0, len(items[x])):
                current = items[x][y]
                if monkey_ops[x] == "* old":
                    current *= current
                elif monkey_ops[x][:2] == "* ":
                    current *= int(monkey_ops[x][2:])
                elif monkey_ops[x][:2] == "+ ":
                    current += int(monkey_ops[x][2:])
                current = current % mod
                if current % monkey_test[x] == 0:
                    items[monkey_conditions[x][0]].append(current)
                else:
                    items[monkey_conditions[x][1]].append(current)
                inspections[x] += 1
            items[x] = []
    print(sorted(inspections)[-1] * sorted(inspections)[-2])

if __name__ == "__main__":
    main()