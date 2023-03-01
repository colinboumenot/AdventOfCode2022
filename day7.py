from collections import defaultdict
def main():
    part_one_text = open('inputtxt/day7input.txt', 'r')
    part_two_text = open('inputtxt/day7input.txt', 'r')
    part_one(part_one_text)
    part_two(part_two_text)

def part_one(text_file):
    file = map(str.split, text_file.read().splitlines())
    path, directions = [], defaultdict(int)

    for line in file:
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    path.pop()
                else:
                    path.append(line[2])
        elif line[0] != "dir":
            for x in range(len(path)):
                directions[tuple(path[: x + 1])] += int(line[0])
    print(sum(size for size in directions.values() if size <= 100000))


def part_two(text_file):
    file = map(str.split, text_file.read().splitlines())
    path, directions = [], defaultdict(int)

    for line in file:
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    path.pop()
                else:
                    path.append(line[2])
        elif line[0] != "dir":
            for x in range(len(path)):
                directions[tuple(path[: x + 1])] += int(line[0])
    required_space = 30000000 - (70000000 - directions[("/",)])
    print(min(x for x in directions.values() if x >= required_space))

if __name__ == "__main__":
    main()