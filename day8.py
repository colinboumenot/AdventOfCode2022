def main():
    part_one_text = open('inputtxt/day8input.txt', 'r')
    part_two_text = open('inputtxt/day8input.txt', 'r')
    part_one(part_one_text)
    part_two(part_two_text)

def part_one(text_file):
    text = text_file.readlines()
    trees = [[int(x) for x in r.strip()] for r in text]
    trees_other = list(zip(*trees))

    counter = 0
    for x in range(len(trees[0])):
        for y in range(len(trees)):
            individual_tree = trees[x][y]
            if all(z < individual_tree for z in trees[x][0:y]) or all(z < individual_tree for z in trees[x][y+1:]) or all(z < individual_tree for z in trees_other[y][0:x]) or all(z < individual_tree for z in trees_other[y][x+1:]):
                counter+= 1
    print(counter)

def part_two(text_file):
    text = text_file.readlines()
    trees = [[int(x) for x in r.strip()] for r in text]
    trees_other = list(zip(*trees))
    max_val = 0

    for x in range(len(trees[0])):
        for y in range(len(trees)):
            tree = trees[x][y]

            east_view = view_value(tree, trees[x][0:y][::-1])
            west_view = view_value(tree, trees[x][y+1:])
            south_view = view_value(tree, trees_other[y][0:x][::-1])
            north_view = view_value(tree, trees_other[y][x+1:])
            score = east_view * west_view * south_view * north_view
            if score > max_val:
                max_val = score
    print(max_val)


def view_value(tree, direction):
    length = 0
    for d in direction:
        length += 1
        if d >= tree:
            break
    return length

if __name__ == "__main__":
    main()