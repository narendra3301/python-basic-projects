import random as ra

random_number = ra.randint(1,10)
#print(random_number)
guess = None 
while True:
    guess = input('Guess a number (1-10) : ')
    guess = int(guess)
    if (guess > random_number):
        print('####   NUM HIGH ###')
    elif (guess < random_number):
        print('### NUM TOO Low ###')
    else:
        print('###  YOU WON ###')
        play_again = input(' Do You Want To Play again? (y/n) : ')
        if (play_again == 'y'):
            random_number = ra.randint(1,10)
            #print(random_number)
            guess = None
        else:
            print('###   Thankyou For playing')
        
    
#print(random_number)   
