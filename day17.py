rocks, i = ((0,1,2,3),(1,0+1j, 2+1j, 1+2j), (0,1,2,2+1j,2+2j),(0,0+1j,0+2j,0+3j),(0,1,0+1j,1+1j)),0
jets, j = [ord(x) - 61 for x in open('inputtxt/day17input.txt').read()], 0
set, dict, height = set(), dict(), 0
empty = lambda pos: pos.real in range(7) and pos.imag > 0 and pos not in set
check = lambda pos, dir, rock: all(empty(pos + dir + r) for r in rock)

for step in range(int(1e12)):
    position = complex(2, height + 4)
    if step == 2022: print(height)

    value = i, j
    if value in dict:
        X, Y = dict[value]
        d, m = divmod(1e12 - step, step - X)
        if m == 0: print(height + (height - Y) * d); break
    else: dict[value] = step, height

    rock = rocks[i]
    i = (i + 1) % len(rocks)

    while True:
        jet = jets[j]
        j = (j + 1) % len(jets)
        if check(position, jet, rock): position += jet
        if check(position, -1j, rock): position += -1j
        else: break

    set |= {position + x for x in rock}
    height = max(height, position.imag+[1,0,2,2,3][i])



