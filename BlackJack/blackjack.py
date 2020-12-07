import art
import random
import subprocess as sp

card = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def changeAce(user):
    user[user.index(11)]=1
    if sum(user)>21:
        changeAce(user)

def retry():
    choice = input("\nTry Again? (y/n) : ")
    if choice.lower() == 'y':
        tmp = sp.call('clear', shell=True)
        blackjack()
    else: 
        exit()

def display(user1,user2):
    print("\n----------------------------------------")
    print(f"\nPlayer Cards : {user1}")
    print(f"Player Total : {sum(user1)}")
    print(f"\nComputer Cards : {user2}")
    print(f"Computer Total : {sum(user2)}")
    print("\n----------------------------------------\n")

def blackjack():
    print(art.logo)
    player = []
    comp = []

    print("\nDealing Cards ...\n")
    for i in range(2):
        player.append(card[random.randint(0,len(card)-1)])
        comp.append(card[random.randint(0,len(card)-1)])

    p_sum = sum(player)
    c_sum = sum(comp)

    if 11 in player and p_sum>21:
        changeAce(player)
    print(f"\nPlayer Cards : {player}")
    print(f"Player Total : {p_sum}")
    print(f"\nComputer's first card : {comp[0]}\n")

    choice = input("Type 'H' to HIT and 'S' to STAND : ")

    if p_sum == 21:
        display(player,comp)
        print("\nPlayer gets a BLACKJACK")
        print("Player WINS\nComputer LOSES")
        retry()

    while choice.lower() =='h':
        player.append(card[random.randint(0,len(card)-1)])
        p_sum = sum(player)

        if p_sum>21:
            if 11 in player:
                changeAce(player)
                p_sum = sum(player)
                print(f"\nPlayer Cards : {player}")
                print(f"Player Total : {p_sum}")
            else:
                display(player,comp)
                print("Player BUST")
                print("Computer WINS")
                retry()

        else:
            print(f"\nPlayer Cards : {player}")
            print(f"Player Total : {p_sum}")

        choice = input("Type 'H' to HIT and 'S' to STAND : ")

    while c_sum < 16:
        comp.append(card[random.randint(0,len(card)-1)])
        c_sum = sum(comp)
        if c_sum == 21:
            display(player,comp)
            print("Computer gets a BLACKJACK")
            print("Computer WINS\nPlayer LOSES")
            retry()
        elif c_sum>21:
            if 11 in comp:
                changeAce(comp)
                c_sum = sum(comp)
            else:
                display(player,comp)
                print("Computer BUST\nPlayer WINS")
                retry()

    display(player,comp)

    if c_sum>p_sum:
        print("\nComputer WINS\nPlayer LOSES\n")
    elif c_sum == p_sum:
        print("PUSH")
    else:
        if p_sum == 21:
            print("Player gets a BLACKJACK")
        print("Computer LOSES\nPlayer WINS")

    retry()

blackjack()