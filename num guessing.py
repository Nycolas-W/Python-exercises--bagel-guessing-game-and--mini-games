import random
i = random.randint(1,9)
#chosing random number between 1 and 9

attempts = 0
#Variable to take record of the attempts made

while True:
#using while true so we can add things such as Try and Except and make good use of break whenver the game needs to end

    userInput = input('Welcome to number guessing! Chose a number between 1 and 9  or press Q the close the game ' ).lower()
    if userInput == 'q':
        print('Thanks for playing! Game closed ')
        break
    try:
        guess = int(userInput)
#putting userInput into int so we can inform the player that it only accepts numbers
        
    except ValueError:
        print("Error! Only numbers!") 
        continue
    attempts += 1
#increasing the attempts number til it reaches 3

    if attempts >= 3 and guess == i: 
#meaning more than 3 attempts and got it right then you won on last try
        print(f'Last try you guessed right! {i}')
#important code that lets you win if you got the right choice at last! (otherwise it would be wrong at the last try)
        break
    elif attempts >=3 and guess != i:
        print(f'too many attempts! Round is over, the correct number {i}')
        break
        
    if guess == i:
        print(f'Correct number ! {i}')
        break
    elif guess >= i:
        print('too high !')
    else:
        print('too low')
