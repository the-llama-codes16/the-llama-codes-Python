import random
res=random.choice([1,2,3,4,5,6,7,8,9])
while True:
    guess=input('Guess a number from 1 to 9:')
    try:
        guess=int(guess)
        if guess<1 or guess>9:
            print('Please choose a number from 1 to 9.')
            continue
        if guess==res:
            print('Well guessed!')
            break
        else:
            print('Try again.')
            continue
    except:
        print('Please enter a valid number')
