def main():
    part_one_text = open('inputtxt/day9input.txt', 'r')
    part_two_text = open('inputtxt/day9input.txt', 'r')
    part_one(part_one_text)
    part_two(part_two_text)





def part_one(text_file):
    directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    adjacent = lambda position_one, position_two: all([abs(position_one[x] - position_two[x]) <= 1 for x in range(2)])
    text = text_file.read().splitlines()
    visited_one = {(0, 0)}
    visited_two = {(0, 0)}
    rope_knots = [[0] * 2 for _ in range(10)]
    for line in text:
        direction = directions[line[0]]
        for _ in range(int(line[2:])):
            for x in range(2):
                rope_knots[0][x] += direction[x]
                for y in range(9):
                    s, t = rope_knots[y:y+2]
                    if not adjacent(s,t):
                        for z in range(2):
                            t[z] += (s[z] != t[z]) * (2*(s[z] > t[z]) - 1)
                visited_one.add(tuple(rope_knots[1]))
                visited_two.add(tuple(rope_knots[9]))
    print(len(visited_one))


def part_two(text_file):
    directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    adjacent = lambda position_one, position_two: all([abs(position_one[x] - position_two[x]) <= 1 for x in range(2)])
    text = text_file.read().splitlines()
    visited_one = {(0, 0)}
    visited_two = {(0, 0)}
    rope_knots = [[0] * 2 for _ in range(10)]
    for line in text:
        direction = directions[line[0]]
        for _ in range(int(line[2:])):
            for x in range(2):
                rope_knots[0][x] += direction[x]
                for y in range(9):
                    s, t = rope_knots[y:y + 2]
                    if not adjacent(s, t):
                        for z in range(2):
                            t[z] += (s[z] != t[z]) * (2 * (s[z] > t[z]) - 1)
                visited_one.add(tuple(rope_knots[1]))
                visited_two.add(tuple(rope_knots[9]))
    print(len(visited_two))
if __name__ == "__main__":
    main()