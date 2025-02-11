import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors:")
    computer = random.choice(['r' , 'p' , 's'])

    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You Win!'
    
    return 'You Lose!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())

def main():
    while True:
        print(play())
        if input("Play again? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
