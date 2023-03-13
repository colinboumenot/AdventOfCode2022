from collections import deque
def main():
    part_one_text = open('inputtxt/day18input.txt', 'r')
    part_two_text = open('inputtxt/day18input.txt', 'r')
    part_one(part_one_text)
    part_two(part_two_text)

def part_one(text_file):
    text = text_file.read().strip().splitlines()
    points = set()
    for line in text:
        x,y,z = line.split(',')
        x,y,z = int(x), int(y), int(z)
        points.add((x,y,z))
    return_value = 0
    for (x,y,z) in points:
        if (x + 1, y, z) not in points:
            return_value += 1
        if (x - 1, y, z) not in points:
            return_value += 1
        if (x, y + 1, z) not in points:
            return_value += 1
        if (x, y - 1, z) not in points:
            return_value += 1
        if (x, y, z + 1) not in points:
            return_value += 1
        if (x, y, z - 1) not in points:
            return_value += 1
    print(return_value)

def is_outside(x,y,z, points):
    previous_coordinates = set()
    queue = deque([(x,y,z)])
    while queue:
        x,y,z = queue.popleft()
        if (x,y,z) in points:
            continue
        if (x,y,z) in previous_coordinates:
            continue
        previous_coordinates.add((x,y,z))
        if len(queue) > 7000:
            return True
        for h in [-1,1]:
            queue.append((x + 1,y,z))
            queue.append((x - 1,y,z))
            queue.append((x,y + 1,z))
            queue.append((x,y - 1,z))
            queue.append((x,y,z + 1))
            queue.append((x,y,z - 1))
    return False

def part_two(text_file):
    text = text_file.read().strip().splitlines()
    points = set()
    for line in text:
        x, y, z = line.split(',')
        x, y, z = int(x), int(y), int(z)
        points.add((x, y, z))
    return_value = 0
    for (x, y, z) in points:
        if is_outside(x + 1,y,z, points):
            return_value += 1
        if is_outside(x - 1,y,z, points):
            return_value += 1
        if is_outside(x,y + 1,z, points):
            return_value += 1
        if is_outside(x,y - 1,z, points):
            return_value += 1
        if is_outside(x,y,z + 1, points):
            return_value += 1
        if is_outside(x,y,z - 1, points):
            return_value += 1
    print(return_value)

if __name__ == "__main__":
    main()