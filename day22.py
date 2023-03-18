text = open('inputtxt/day22input.txt', 'r').read()
lines = [x for x in text.split('\n')]

G, instr = text.split('\n\n')
G = G.split('\n')
instr = instr.strip()

Directions = [(-1,0), (0,1), (1,0), (0,-1)]

row = len(G)
column = len(G[0])
for r in range(row):
    while len(G[r]) < column:
        G[r] += ' '
    assert len(G[r]) == column

cube = column // 3
assert cube == row //4

Regions = [(0,1), (0,2), (1,1), (2,1), (2,0), (3,0)]

def regiontoGlobal(r,c,region):
    rr, cc = Regions[region - 1]
    return (rr * cube + r, cc * cube + c)

def getRegion(r,c):
    for i, (rr,cc) in enumerate(Regions):
        if rr * cube <= r < (rr + 1) * cube and cc * cube <= c < (cc + 1) * cube:
            return (i + 1, r - rr*cube, c -cc*cube)
    assert False, (r,c)

def newCoords(r,c,d,nd):
    if d == 0:
        assert r == 0
        x = c
    if d == 1:
        assert c == cube - 1
        x = r
    if d == 2:
        assert r == cube - 1
        x = cube - 1 - c
    if d == 3:
        assert c == 0
        x = cube - 1 - r
    if nd == 0:
        return (cube - 1, x)
    if nd == 1:
        return (x,0)
    if nd == 2:
        return (0, cube -1 -x)
    if nd == 3:
        return (cube - 1 - x, cube -1)

def getDest(r,c,d,part):
    if part == 1:
        r = (r +Directions[d][0]) % row
        c = (c + Directions[d][1]) % column
        while G[r][c] == ' ':
            r = (r+Directions[d][0]) % row
            c = (c + Directions[d][1]) % column
        return (r,c,d)

    region, rr, rc = getRegion(r,c)
    newRegion, nd = {(4,0):(3,0), (4,1):(2,3), (4,2):(6,3), (4,3):(5,3), (1,0):(6,1),
                     (1,1):(2,1), (1,2):(3,2), (1,3):(5,1), (3,0):(1,0), (3,1):(2,0),
                     (3,2):(4,2), (3,3):(5,2), (6,0):(5,0), (6,1):(4,0), (6,2):(2,2),
                     (6,3):(1,2), (2,0):(6,0), (2,1):(4,3), (2,2):(3,3), (2,3):(1,3),
                     (5,0):(3,1), (5,1):(4,1), (5,2):(6,2), (5,3):(1,1)}[(region, d)]
    nr, nc = newCoords(rr, rc, d, nd)
    nr, nc = regiontoGlobal(nr, nc, newRegion)
    return (nr, nc, nd)

def solve(part):
    r = 0
    c = 0
    d = 1
    while G[r][c] != '.':
        c += 1
    i = 0
    while i < len(instr):
        n = 0
        while i < len(instr) and instr[i].isdigit():
            n = n * 10 + int(instr[i])
            i += 1
        for _ in range(n):
            rr = (r + Directions[d][0]) % row
            cc = (c + Directions[d][1]) % column
            if G[rr][cc] == ' ':
                (nr, nc, nd) = getDest(r,c,d,part)
                if G[nr][nc] == '#':
                    break
                (r,c,d) = (nr, nc, nd)
                continue
            elif G[rr][cc] == '#':
                break
            else:
                r = rr
                c = cc
        if i == len(instr):
            break
        turn = instr[i]
        if turn == 'L':
            d = (d+3)%4
        elif turn == 'R':
            d = (d+1)%4
        else:
            assert False, (i, instr[i:], instr[i])
        i += 1
    DV = {0:3, 1:0, 2:1, 3:2}
    return ((r+1) * 1000 + (c+1)*4 + DV[d])
print(solve(1))
print(solve(2))

