from collections import defaultdict
text = open('inputtxt/day23input.txt', 'r').read()
lines = [x for x in text.split('\n')]

elves = set()
grid = lines

for x, row in enumerate(grid):
    for y, item in enumerate(row):
        if item == '#':
            elves.add((x,y))

def show(elves):
    row_one = min(r for (r,c) in elves)
    row_two = max(r for (r,c) in elves)
    col_one = min(c for (r, c) in elves)
    col_two = max(c for (r, c) in elves)
    for r in range(row_one, row_two + 1):
        row = ''
        for c in range(col_one, col_two + 1):
            row += ('#' if (r,c) in elves else '.')

directions = ['N', 'S', 'W', 'E']
for t in range(10000):
    moved = False
    positions = defaultdict(list)
    for (r,c) in elves:
        neighbor = False
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if (dr != 0 or dc != 0) and (r + dr, c + dc) in elves:
                    neighbor = True
        if not neighbor:
            continue

        move = False
        for direction in directions:
            if direction == 'N' and (not move) and (r-1,c) not in elves and (r-1,c-1) not in elves and (r-1, c+1) not in elves:
                positions[(r-1,c)].append((r,c))
                move = True
            elif direction == 'S' and (not move) and (r+1,c) not in elves and (r+1,c-1) not in elves and (r+1, c+1) not in elves:
                positions[(r+1,c)].append((r,c))
                move = True
            elif direction == 'W' and (not move) and (r,c-1) not in elves and (r-1,c-1) not in elves and (r+1, c-1) not in elves:
                positions[(r,c-1)].append((r,c))
                move = True
            elif direction == 'E' and (not move) and (r,c+1) not in elves and (r-1,c+1) not in elves and (r+1, c+1) not in elves:
                positions[(r,c+1)].append((r,c))
                move = True
    directions = directions[1:] + [directions[0]]
    for k, vs in positions.items():
        if len(vs) == 1:
            moved = True
            elves.discard(vs[0])
            elves.add(k)
    if not moved:
        print(t + 1)
        break
    if t == 9:
        row_one = min(r for (r,c) in elves)
        row_two = max(r for (r, c) in elves)
        col_one = min(c for (r, c) in elves)
        col_two = max(c for (r, c) in elves)
        ans = 0
        for r in range(row_one, row_two + 1):
            for c in range(col_one, col_two + 1):
                if (r,c) not in elves:
                    ans += 1
        print(ans)
