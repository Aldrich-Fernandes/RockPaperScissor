# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from random import choice

#Abby and kris are a problem
# resetting probabities helps improtve for aby and kris

#Choose rather than guess
# Told thier previous choice and combine it with thier prev_play as a ky.

def player(prev_play, PrevKey = [""], Guess = [""], Probs = [{}], game = [0]):

    OpponentChoices = ["R", "P", "S"]
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    if prev_play == '' or game[0] > 50: # check the probability of each choice after these 2 then use that 
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
        Guess[0] = choice(["R", "P", "S"])
        prev_play = choice(["R", "P", "S"])
        
    
    game[0] += 1
    if len(PrevKey[0]) == 2:
        Probs[0][PrevKey[0]][prev_play] += 1
        
    try:
        Guess = max(Probs[0][PrevKey[0]], key=Probs[0][PrevKey[0]].get)
    except:
        Guess = choice(OpponentChoices)
        
    #MostCommon = max(set(Guess), key=Guess.count)
    PrevKey[0] = Guess[0] + prev_play
    #print(f"Opponent = {opponent_history[-1]} \n Player Played = {ideal_response[Guess[0]]}")
    return ideal_response[Guess]
