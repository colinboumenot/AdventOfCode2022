def main():
    part_one_text = open('inputtxt/day5input.txt', 'r')
    part_two_text = open('inputtxt/day5input.txt', 'r')
    ##part_one(part_one_text)
    part_two(part_two_text)

one = ['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P']
two = ['M', 'Q', 'H']
three = ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L']
four = ['Z', 'T', 'F', 'Q', 'M', 'W', 'G']
five = ['M', 'T', 'H', 'P']
six = ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T']
seven = ['M', 'N', 'B', 'F', 'V', 'R']
eight = ['P', 'L', 'H', 'M', 'R', 'G', 'S']
nine = ['P', 'D', 'B', 'C', 'N']
stacks = [one, two, three, four, five, six, seven, eight, nine]

def part_one(text_file):

    for line in text_file:
        data = line.split(' ')
        number_to_take = int(data[1])
        stack_to_move = int(data[3]) - 1
        stack_to_recieve = int(data[5]) - 1
        for x in range(number_to_take):
            stacks[stack_to_recieve].append(stacks[stack_to_move][-1])
            stacks[stack_to_move].pop()
    for stack in stacks:
        print(stack[-1])

def part_two(text_file):

    for line in text_file:
        data = line.split(' ')
        number_to_take = int(data[1])
        stack_to_move = int(data[3]) - 1
        stack_to_recieve = int(data[5]) - 1
        stacks[stack_to_recieve] += (stacks[stack_to_move][-number_to_take:])
        del stacks[stack_to_move][-number_to_take:]
    for stack in stacks:
        print(stack[-1])


if __name__ == "__main__":
    main()