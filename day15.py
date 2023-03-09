import re

def main():
    part_one_text = open('inputtxt/day15input.txt', 'r')
    part_two_text = open('inputtxt/day15input.txt', 'r')
    part_one(part_one_text)
    part_two(part_two_text)

def part_one(text_file):
    ints = lambda s: map(int, re.findall(r'-?\d+',s))
    distance = lambda x,y,r,s: abs(x-r) + abs(y-s)
    data = [(x,y, distance(x,y,r,s)) for x,y,r,s in map(ints, text_file)]
    X = 2_000_000
    print(max(x- abs(X-y) + d for x,y,d in data) - min(x + abs(X-y) - d for x,y,d in data))




def part_two(text_file):
    ints = lambda s: map(int, re.findall(r'-?\d+', s))
    distance = lambda x, y, r, s: abs(x - r) + abs(y - s)
    data = [(x, y, distance(x, y, r, s)) for x, y, r, s in map(ints, text_file)]
    X, Y = 2_000_000, 4_000_000
    t = lambda x,y,d,p,q,r: ((p + q + r + x - y - d)//2, (p + q + r - x + y + d)//2 + 1)
    for A, B in [t(*a, *b) for a in data for b in data]:
        if 0<A<Y and 0<B<Y and all(distance(A,B,x,y) > d for x,y,d in data):
            print(Y * A + B)


if __name__ == "__main__":
    main()