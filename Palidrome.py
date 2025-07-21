def is_palidrome(word):
    return word == word[::-1]
while True :
    userInput= input('Welcome to palidrome testing! Chose a word! If youre done type Q ').lower()
    if userInput == 'q':
        print('thanks for testing')
        break
    print('is palidrome' if is_palidrome(userInput) else 'its not palidrome')