# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from random import choices

#Abby and kris are a problem

def player(prev_play, Previous=[""], Probs = [{}], game = [0]):

    OpponentChoices = ["R", "P", "S"]
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    if prev_play == '': # check the probability of each choice after these 2 then use that 
        Probs[0] = {"RR": {"R": 0, "P": 0, "S": 0},
             "RP": {"R": 0, "P": 0, "S": 0},
             "RS": {"R": 0, "P": 0, "S": 0},
             "PR": {"R": 0, "P": 0, "S": 0},
             "PP": {"R": 0, "P": 0, "S": 0},
             "PS": {"R": 0, "P": 0, "S": 0},
             "SR": {"R": 0, "P": 0, "S": 0},
             "SP": {"R": 0, "P": 0, "S": 0},
             "SS": {"R": 0, "P": 0, "S": 0}}
        game[0] = 0
        prev_play = choices(OpponentChoices)[0]
        Previous = choices(OpponentChoices)[0]
       
    game[0] += 1
    
    lastTwo = Previous + prev_play
    if len(LastTwo) != 2:
        LastTwo = choices(OpponentChoices)[0]+prev_play

    Probs[0][LastTwo][prev_play] += 1
    Guess = choices(OpponentChoices,
                    weights=(Probs[0][LastTwo]["R"], Probs[0][LastTwo]["P"], Probs[0][LastTwo]["S"]),
                    k=1)
    
        
    MostCommon = max(set(Guess), key=Guess.count)

    
    #print(f"Opponent = {opponent_history[-1]} \n Player Played = {ideal_response[Guess[0]]}")
    return ideal_response[MostCommon]
