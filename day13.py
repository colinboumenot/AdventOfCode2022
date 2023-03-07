from functools import cmp_to_key
from math import prod
def main():
    part_one_text = open('inputtxt/day13input.txt', 'r')
    part_two_text = open('inputtxt/day13input.txt', 'r')
    part_one(part_one_text)
    part_two(part_two_text)
def cmp(left, right):
    match left, right:
        case int(), int():
            return (left > right) - (left < right)
        case int(), list():
            return cmp([left], right)
        case list(), int():
            return cmp(left, [right])
        case list(), list():
            for x in map(cmp, left, right):
                if x:
                    return x
            return cmp(len(left), len(right))
def part_one(text_file):
    text = [[*map(eval, x.split())] for x in text_file.read().split('\n\n')]
    print(sum(x for x, y in enumerate(text, 1) if cmp(*y) == -1))

def part_two(text_file):
    text = [[*map(eval, x.split())] for x in text_file.read().split('\n\n')]
    text = sorted(sum(text, [[2], [6]]), key = cmp_to_key(cmp))
    print(prod(x for x, y in enumerate(text, 1) if y in [[2], [6]]))

if __name__ == "__main__":
    main()