class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


text = open('inputtxt/day20input.txt', 'r')
##lines = [Node(int(x)) for x in text]

#for x in range(len(lines)):
    #lines[x].right = lines[(x + 1) % len(lines)]
    #lines[x].left = lines[(x - 1) % len(lines)]

#m = len(lines) - 1

#for line in lines:
    #if line.value == 0:
        #z = line
        #continue
    #p = line
    #if line.value > 0:
        #for _ in range(line.value % m):
            #p = p.right
        #if line == p:
            #continue
        #line.right.left = line.left
        #line.left.right = line.right
        #p.right.left = line
        #line.right = p.right
        #p.right = line
        #line.left = p
    #else:
        #for _ in range(-line.value % m):
            #p = p.left
       # if line == p:
            #continue
        #line.left.right = line.right
        #line.right.left = line.left
        #p.left.right = line
        #line.left = p.left
       # p.left = line
        #line.right = p



##value = 0

##for _ in range(3):
    #for _ in range(1000):
        #z = z.right
    #value += z.value
#print(value)

lines = [Node(int(x) * 811589153) for x in text]

for x in range(len(lines)):
    lines[x].right = lines[(x + 1) % len(lines)]
    lines[x].left = lines[(x - 1) % len(lines)]

m = len(lines) - 1

for _ in range(10):
    for line in lines:
        if line.value == 0:
            z = line
            continue
        p = line
        if line.value > 0:
            for _ in range(line.value % m):
                p = p.right
            if line == p:
                continue
            line.right.left = line.left
            line.left.right = line.right
            p.right.left = line
            line.right = p.right
            p.right = line
            line.left = p
        else:
            for _ in range(-line.value % m):
                p = p.left
            if line == p:
                continue
            line.left.right = line.right
            line.right.left = line.left
            p.left.right = line
            line.left = p.left
            p.left = line
            line.right = p

value = 0

for _ in range(3):
    for _ in range(1000):
        z = z.right
    value += z.value
print(value)