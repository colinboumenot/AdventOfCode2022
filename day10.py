def main():
    part_one_text = open('inputtxt/day10input.txt', 'r')
    part_two_text = open('inputtxt/day10input.txt', 'r')
    part_one(part_one_text)
    part_two(part_two_text)

def part_one(text_file):
    signal = 0
    multiplier = 1
    cycles = 0
    checkpoint = 20
    for line in text_file.readlines():
        cycles += 1
        if line.startswith('addx'):
            cycles += 1
            if cycles >= checkpoint:
                signal += multiplier * checkpoint
                checkpoint += 40
            multiplier += int(line.split()[1])
    print(signal)
def execute(cycles, multiplier, pixels):
    cycles += 1
    if multiplier <= cycles <= multiplier + 2:
        pixels.append(cycles - 1)
    if cycles == 40:
        for x in range(40):
            print("=", end = "") if x in pixels else print(" ", end = "")
        print()
        pixels.clear()
        cycles = 0
    return cycles

def part_two(text_file):
    pixels = []
    multiplier = 1
    cycles = 0
    for line in text_file.readlines():
        cycles = execute(cycles, multiplier, pixels)
        if line.startswith('addx'):
            cycles = execute(cycles, multiplier, pixels)
            multiplier += int(line.split()[1])

if __name__ == "__main__":
    main()