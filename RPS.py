# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from random import choices

#Abby and kris are a problem

def player(prev_play, opponent_history=[], Count = [{}], game = [0]):

    OpponentChoices = ["R", "P", "S"]
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    if prev_play == '': # check the probability of each choice after these 2 then use that 
        Count[0] = {"RR": {"R": 0, "P": 0, "S": 0},
             "RP": {"R": 0, "P": 0, "S": 0},
             "RS": {"R": 0, "P": 0, "S": 0},
             "PR": {"R": 0, "P": 0, "S": 0},
             "PP": {"R": 0, "P": 0, "S": 0},
             "PS": {"R": 0, "P": 0, "S": 0},
             "SR": {"R": 0, "P": 0, "S": 0},
             "SP": {"R": 0, "P": 0, "S": 0},
             "SS": {"R": 0, "P": 0, "S": 0}}
        game[0] = 0
        prev_play = choices(["R", "P", "S"])[0]
        
    opponent_history.append(prev_play)
    game[0] += 1
    
    LastTwo = ''.join(opponent_history[-2:])
    LastThree = ''.join(opponent_history[-3:])
    if len(LastThree) == 3 and game[0] < 250 and game[0] > 3:
        Count[0][LastThree[:-1]][prev_play] += 1

    try:
        Guess = choices(OpponentChoices,
                        weights=(Count[0][LastTwo]["R"], Count[0][LastTwo]["P"], Count[0][LastTwo]["S"]),
                        k=10)
    except:
        Guess = choices(OpponentChoices)
        
    MostCommon = max(set(Guess), key=Guess.count)

    
    #print(f"Opponent = {opponent_history[-1]} \n Player Played = {ideal_response[Guess[0]]}")
    return ideal_response[MostCommon]
