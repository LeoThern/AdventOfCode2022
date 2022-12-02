score_of_shape = {'rock':1, 'paper':2, 'scissors':3}
shape_of_score = {1:'rock', 2:'paper', 3:'scissors'}
shape_of_symbol = {'A':'rock', 'X':'rock',
                   'B':'paper', 'Y':'paper',
                   'C':'scissors', 'Z':'scissors'}

def score_of_round(opponent, player, TASK = 1):
    if TASK == 1:
        opponent, player = shape_of_symbol[opponent], shape_of_symbol[player]
    if TASK == 2:
        opponent = shape_of_symbol[opponent]
        player = shape_of_result(opponent, player)
    score = 0
    score += score_of_shape[player]
    score += score_of_outcome(opponent, player)
    print(f"{opponent} vs. {player} --> {score}")
    return score

#TASK 2
def shape_of_result(opponent, result):
    if result == 'Y': #Draw
        return opponent
    if result == 'X': #Lose
        player = score_of_shape[opponent] - 1
        if player == 0:
            player = 3
        return shape_of_score[player]
    if result == 'Z': #Win
        player = score_of_shape[opponent] + 1
        if player == 4:
            player = 1
        return shape_of_score[player]

def score_of_outcome(opponent, player):
    if player == opponent:
        return 3 #Draw
    opponent, player = score_of_shape[opponent], score_of_shape[player]
    if opponent + 1 == player or player == 1 and opponent == 3:
        return 6 #Player Wins
    else:
        return 0 #Player Loses

def main():
    total_score = 0
    with open('input.txt') as file:
        for line in file:
            a, b = line.strip().split(' ')
            total_score += score_of_round(a, b, TASK=2)
    
    print(f"Total: {total_score}")

if __name__ == '__main__':
    main()