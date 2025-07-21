import random

def bagle():
    print('Welcome to Bagle game! Guess a secret three-digit number based on clues, RULES:')
    print('----1 ) Pico: One digit is correct but in the wrong position. ---')
    print('----2 ) Fermi: One digit is correct and in the right position.---')
    print('----3 ) Bagels: The digit is correct.                          ---')
    
    while True:
        a = tuple(random.randint(1, 9) for _ in range(3))
        tries = 0

        while True:
            b = input('Choose 3 numbers (ex: 1 2 3): ').strip().split()
            if len(b) != 3 or not all(x.isdigit() for x in b):
                print('Wrong, use only numbers and only 3 (e.g., 1 2 3)')
                continue
            guess = tuple(int(x) for x in b)
            clues = []
            for i in range(3):
                if guess[i] == a[i]:
                    clues.append('Fermi')
                elif guess[i] in a:
                    clues.append('Pico')
                else:
                    clues.append('Bagels')
            tries += 1
            print(f'Clues: {clues}')
            print(f'Your total tries: {tries} {a}')
            if guess == a:
                print('You won!')
                break
            elif tries == 10:
                print(f'Used your maximum amount of tries! You lost. The correct number was {a}')
                break

        play_again = input('Wanna play again? (yes or no): ').strip().lower()
        if play_again != 'yes':
            print('Thanks for playing!')
            break

bagle()