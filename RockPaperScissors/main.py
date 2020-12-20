import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("------------ROCK PAPER SCISSORS------------")
print("\n\nRules:\n1.This is a best of 3 game.\n2.In case you don't know or don't remember\n\t*ROCK beats SCISSOR\n\t"
      "*PAPER beats ROCK\n\t*SCISSOR beats PAPER\n3.Type:\n\t'0' for ROCK\n\t'1' for PAPER\n\t'2' for SCISSORS")
print("\n\nALL THE BEST")

count = 0
player_point = 0
comp_point = 0

while count < 3:
    choice = int(input("\n\nWhat do you choose? : "))
    
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    else:
        print(scissors)
    
    print("Computer chooses : ")
    comp = random.randint(0,2)
    if comp == 0:
        print(rock)
    elif comp == 1:
        print(paper)
    else:
        print(scissors)

    if choice == comp:
        print("\nIts a draw")
    elif choice == 0 and comp == 1:
        print("Computer gets a point")
        comp_point += 1
    elif choice == 0 and comp == 2:
        print("You get a point")
        player_point += 1
    elif choice == 1 and comp == 2:
        print("Computer gets a point")
        comp_point += 1
    elif choice == 1 and comp == 0:
        print("You get a point")
        player_point += 1
    elif choice == 2 and comp == 0:
        print("Computer gets a point")
        comp_point += 1
    elif choice == 2 and comp == 1:
        print("You get a point")
        player_point += 1
    else:
        print("Enter valid choice")
    
    count += 1

print(f"\n\nPlayer Points : {player_point}")
print(f"\nComputer Points : {comp_point}")

if player_point > comp_point:
    print("\nYOU WIN")
elif player_point < comp_point:
    print("\nYOU LOSE")
else:
    print("\nITS A DRAW")
