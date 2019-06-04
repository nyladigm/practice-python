'''
Exerise 8 - Rock, Paper, Scissors from Practice Python
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner, and ask if the
players want to start a new game)

Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock
'''

#while loop to execute all this code and an input for each of the two users
while True:
    player_1 = input('player one, please enter one of the following: rock, paper, scissors')
    player_2 = input('player two, please enter one of the following: rock, paper, scissors')

    if player_1 == player_2:
        print('we have a tie!')
    elif player_1 == 'rock' and player_2 == 'scissors':
        print('player one wins - congrats!')
    elif player_1 == 'paper' and player_2 == 'rock':
        print('player one wins - congrats!')
    elif player_1 == 'scissors' and player_2 == 'paper':
        print('player one wins - congrats!')
    else:
        print('player two wins - congrats')

    #ask the user if they'd like to continue playing the game
    play_again = input("If you'd like to play again, please type 'yes'")
    if play_again == "yes":
        continue
    else:
        break
