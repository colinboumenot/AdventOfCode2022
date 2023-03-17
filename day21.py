import sympy
monkeys = {}

text = [line.strip() for line in open('inputtxt/day21input.txt', 'r')]

for line in text:
    name, expression = line.split(': ')
    if expression.isdigit():
        monkeys[name] = int(expression)
    else:
        left, operation, right = expression.split()
        if left in monkeys and right in monkeys:
            monkeys[name] = eval(f"{monkeys[left]} {operation} {monkeys[right]}")
        else:
            text.append(line)
print(int(monkeys['root']))

monkeys_two = { 'humn': sympy.Symbol('x')}
text_two = [line.strip() for line in open('inputtxt/day21input.txt', 'r')]
operations = { '+' : lambda x, y: x + y, '-': lambda  x, y: x - y, '*' : lambda x, y: x * y, '/' : lambda x, y: x / y,}
for line in text_two:
    name, expression = line.split(': ')
    if name in monkeys_two:
        continue
    if expression.isdigit():
        monkeys_two[name] = sympy.Integer(expression)
    else:
        left, operation, right = expression.split()
        if left in monkeys_two and right in monkeys_two:
            if name == 'root':
                print(sympy.solve(monkeys_two[left] - monkeys_two[right]))
                break
            monkeys_two[name] = operations[operation](monkeys_two[left], monkeys_two[right])

        else:
            text_two.append(line)
