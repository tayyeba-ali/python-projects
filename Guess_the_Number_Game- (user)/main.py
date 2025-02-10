import random

def guess(x):
   random_num = random.randint(1,x)
   guess = 0
   while guess != random_num:
    guess = int (input(f'Guess the number between 1 and {x}: '))
    if guess < random_num :
      print("Sorry, guess again, To low .")
    elif guess > random_num:
       print("Sorry, guess again, To high.")
   print("Yay, Congratulations. You have guessed the number{random_num} correctly ")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':  
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low  
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


computer_guess(10)