'''
Faça um jogo de Pedra-Papel-Tesoura para dois jogadores.
(Dica: peça as jogadas dos jogadores (usando entrada),
compare-as, imprima uma mensagem de parabéns ao vencedor
e pergunte se os jogadores querem começar um novo jogo)



import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))

'''
from getpass import getpass

print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(getpass("Player a: ").lower())
    player_b = str(getpass("Player b: ").lower())
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b


    print("Player a choose: " + player_a)
    print("Player b choose: " + player_b)
    if dif in [-1, 2]:
        print('Player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('Player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')