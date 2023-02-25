def main():
    part_one_text = open('inputtxt/day2input.txt', 'r')
    part_two_text = open('inputtxt/day2input.txt', 'r')
    part_one(part_one_text)
    part_two(part_two_text)



def part_one(text_file):
    my_score = 0
    opponent_score = 0
    for line in text_file:
        opponent_score += points_for_move(str(line[0]))
        my_score += points_for_move(str(line[2]))
        move_one_value = points_for_move(str(line[0]))
        move_two_value = points_for_move(str(line[2]))
        winner = determine_winner(move_one_value, move_two_value)
        if (winner == 0):
            opponent_score += 3
            my_score += 3
        elif (winner == 1):
            opponent_score += 6
        else:
            my_score += 6
    print(opponent_score)
    print(my_score)


def part_two(text_file):
    opponent_score = 0
    my_score = 0
    for line in text_file:
        opponent_score += points_for_move(str(line[0]))
        my_score += points_for_move(response_move(str(line[0]), str(line[2])))
        if str(line[2]) == "X":
            opponent_score += 6
        elif str(line[2]) == "Y":
            opponent_score += 3
            my_score += 3
        else:
            my_score += 6
    print(opponent_score)
    print(my_score)

def response_move(move, result):
    if result == "X":
        if move == "A":
            return "Z"
        if move == "B":
            return "X"
        if move == "C":
            return "Y"
    elif result == "Y":
        if move == "A":
            return "X"
        if move == "B":
            return "Y"
        if move == "C":
            return "Z"
    elif result == "Z":
        if move == "A":
            return "Y"
        if move == "B":
            return "Z"
        if move == "C":
            return "X"



def points_for_move(move):
    if move == "A" or move == "X":
        return 1
    if move == "B" or move == "Y":
        return 2
    if move == "C" or move == "Z":
        return 3

def determine_winner(move_one, move_two):
    if move_one == move_two:
        return 0
    elif move_one == 1 and move_two == 3 or (move_one == 2 and move_two == 1) or (move_one == 3 and move_two == 2):
        return 1
    else:
        return 2




if __name__ == "__main__":
    main()