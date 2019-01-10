import random

def main():

    player1name = input('Enter your name: ')
    player1score = 0
    player2name = input('Enter your name: ')
    player2score = 0
    rounds = 1

    while rounds != 4:
        print ("Round " + str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print(str(player1name) + " rolls: " + str(player1))
        print(str(player2name) + " rolls: " + str(player2))

        if player1 == player2:
            print("It's a draw!\n")
        elif player1 > player2:
            print(str(player1name) + " Wins!\n")
            player1score = player1score + 1
        else:
            player2score = player2score + 1
            print(str(player2name) + " Wins!\n")

        rounds = rounds+1

    if player1score == player2score:
        print("It's a draw!")
    elif player1score > player2score:
        print(str(player1name) + " Wins! Rounds won: " + str(player1score))
    else:
        print(str(player2name) + " Wins! Rounds won: " + str(player2score))

def dice_roll():
    diceRoll = random.randint(1, 6)
    return diceRoll

main()
