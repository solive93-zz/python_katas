from random import randint
from RockPaperScissorsLizardSpock import RockPaperScissorsLizardSpock

"""
 *Rock Paper Scissors Lizard Spock!*
 
 "Scissors cuts paper, paper covers rock, rock crushes lizard,
 lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard,
 lizard eats paper, paper disproves Spock, Spock vaporizes rock,
 and as it always has, rock crushes scissors." 
                                    - Sheldon Cooper
 """
if __name__ == '__main__':
    nameNumberEquivalence = {1: 'Rock', 2: 'Paper', 3: 'Scissors', 4: 'Lizard', 5: 'Spock'}
    rpsls = RockPaperScissorsLizardSpock()
    print("Sheldon wants to play!")
    userChoice = input("Rock, Paper, Scissors, Lizard or Spock; what's your choice? ")
    print("You chose " + userChoice)
    sheldonChoice = nameNumberEquivalence.get(randint(1, 5))
    print("Sheldon chose " + str(sheldonChoice))
    winner = rpsls.play(userChoice, sheldonChoice)
    print(winner)
