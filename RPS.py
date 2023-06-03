# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from random import choices
#Abby and kris are a problem

def player(prev_play, opponent_history=[], Count = [{}], game = [0]):

    OpponentChoices = ["R", "P", "S"]
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    if prev_play == '':
        Count[0] = {"RR": 0,
             "RP": 0,
             "RS": 0,
             "PR": 0,
             "PP": 0,
             "PS": 0,
             "SR": 0,
             "SP": 0,
             "SS": 0}
        game[0] = 0
        prev_play = choices(["R", "P", "S"])[0]
        
    opponent_history.append(prev_play)
    game[0] += 1
    
    LastTwo = ''.join(opponent_history[-2:])
    if len(LastTwo) == 2:
        Count[0][LastTwo] += 1

    try:
        Guess = choices(OpponentChoices,
                        weights=(Count[0][prev_play+"R"], Count[0][prev_play+"P"], Count[0][prev_play+"S"]),
                        k=3)
    except:
        Guess = choices(OpponentChoices, k=3)
        
    MostCommon = max(set(Guess), key=Guess.count)

    
    if game[0] == 1000:
        print(f"\nCount: {Count[0]} \nSum={sum(Count[0].values())}")
        
    
    #print(f"Opponent = {opponent_history[-1]} \n Player Played = {ideal_response[Guess[0]]}")
    return ideal_response[MostCommon]
