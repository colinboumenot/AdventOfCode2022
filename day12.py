import sys, collections

def main():
    part_one_text = open('inputtxt/day12input.txt', 'r')
    part_two_text = open('inputtxt/day12input.txt', 'r')
    part_one(part_one_text)
    part_two(part_two_text)

def part_one(text_file):
   grid = text_file.read().splitlines()
   print(find(grid, 'S'))

def part_two(text_file):
    grid = text_file.read().splitlines()
    print(find(grid, 'S', 'a'))

def find(grid, *start):
    queue = collections.deque((x, y, 0, 'a') for x in range(len(grid)) for y in range(len(grid[x])) if grid[x][y] in start)
    visited_points = set((x,y) for x, y, _, _ in queue)
    while queue:
        x, y, z, a = queue.popleft()
        if grid[x][y] == 'E':
            return z
        for nx, ny in (x + 1, y), (x - 1, y), (x, y+1), (x, y-1):
            if not 0 <= nx < len(grid):
                continue
            if not 0 <= ny < len(grid[nx]):
                continue
            if (nx, ny) in visited_points:
                continue
            coordinate = grid[nx][ny].replace('E', 'z')
            if ord(coordinate) > ord(a) + 1:
                continue
            visited_points.add((nx, ny))
            queue.append((nx, ny, z + 1, coordinate))
if __name__ == "__main__":
    main()