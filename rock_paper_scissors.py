import random

def play():
    user = input(" Print r for rock, p for paper or s for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie :p'
    
    # r>s , p>r, s>p
    if is_win(user, computer):
        print(f'Computer\'s input is {computer}')
        return 'You won!!'
    
    return 'You lost :('

#return true if the player wins
def is_win(player, opponent):
    
    # r>s , p>r, s>p
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') \
        or (player == 's' and opponent == 'p'):
        return True
    

print(play())