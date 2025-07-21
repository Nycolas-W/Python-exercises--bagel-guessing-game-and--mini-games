#rock paper scissors
import random
choices = ('rock', 'paper', 'scissors')
i_wins = 0
user_wins = 0
while True :
    userInput = input('Welcome to rock paper scissors, chose which one you want, win the one with 3 points! If you wanna quit press Q ').strip().lower()
    if userInput == 'q':
        print('Program closed! Thanks for playing ')
        break
    if userInput not in choices:
        print('Wrong word typed, please use rock, paper or scissors ')
        continue
        
    wincon = {'rock': 'scissors', 'paper':'rock', 'scissors':'rock'}

    
    i = random.choice(choices) 
    
    if userInput == i:
        print('tie!No one gets points ')
    elif wincon.get(userInput) == i:
        user_wins += 1
        print(f'you won! +1 points! You have {user_wins} points ')
    else:
        i_wins += 1
        print(f'you lost! +1 points! the computer have {i_wins} points')

    if user_wins == 3:
        print(f'You won 3 while the computer only won {i_wins}')
        break
    elif i_wins == 3:
        print(f'You lost {user_wins} while the computer won {i_wins}')
        break