print('''
            *******************************************************************************
                    |                   |                  |                     |
            ________|________________.=""_;=.______________|_____________________|_________
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                    |                `"=._o`"=._      _`"=._                     |
            ________|_____________________:=._o "=._."_.-="'"=.__________________|_________
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                    |           |o`"=._` , "` `; .". ,  "-._"-._; ; '            |
            ________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /'______________|_________
            |                   | |o;    `"-.o`"=._``  '` " ,__.--o|   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; |___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o|____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; |/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o|____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/_____ /
            *******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print("You are on the beach. There's an island 200m from you. "
      "It is rumoured that theres a treasure hidden amidst the rocks in that island.\n"
      "Beware! Danger awaits you on this path. You may choose to take the risks and "
      "find the treasure or play it safe and quit.\n")

ch = input("\nWould you like to embark on this journey? (Y/N)\t")

if ch.upper() == "Y":
    print("\nI like your spirit! Wish you luck on your journey. "
          "Remember, choose wisely. Your every step may take you closer to the treasure or to your demise!")
    print("\nTo go to the island, you can swim or wait for a boat.")
    ch = input("\nWould you rather swim or wait? (S/W)\t")

    if ch.lower() == "w":
        print("\nThere he is...The boat is here. You get into the boat and off to the island you go.")
        print("\nAfter a lot of hunting, you now see the treasure chest...or wait, its chests!\n"
              "You see before you 3 boxes and 1 letter.\n"
              "The letter reads : 'One of these 3 boxes has gold enough to last you a lifetime. "
              "Choose correctly and the gold is yours. One wrong move, and no one will know you ever existed'\n"
              "OMG! That's scary.")
        ch = input("\nWould you like to continue or quit? (C/Q)")

        if ch.lower() == "c":
            print("\nLooks like mama didn't raise no quitters! "
                  "You have in front of you a Gold, Silver and a Bronze coloured box. "
                  "Remember to choose carefully, lest your efforts be all in vain")
            ch = input("Which box do you open? (G/S/B)\t")

            if ch.lower() == "g":
                print("\nAll that glitters is not gold! "
                      "Within the box lied hundreds of poisonous scorpions. You get bit by it and you die :(")
                print("\nThat was a good game. Better luck next time (or not ;))")
            elif ch.lower() == "s":
                print("\nOMG! Whats all that glittery stuff?!! Well, I'll be damned if that's not the treasure!!")
                print("\nCONGRATULATIONS!!! You win! Looks like all that risk-taking paid off. "
                      "Good bye, and see you next time!")
            else:
                print("\nDid you think that the story of the hardworking woodcutter would happen to you?! "
                      "\nWell, well, well, isn't that a shame. \n"
                      "The box contents were empty but the box itself was lined with minute needles coated with poison."
                      " You prick yourself while opening the box, and die because of the poison :(")
                print("\nWell played. Better luck next time (or not ;))")

        else:
            print("I don't blame you for quitting. The odds were pretty bad. "
                  "The boat is still waiting. Hurry and go on back.\nUntil next time!")

    else:
        print("\nUh-oh! I guess no one warned you of the hungry alligators in the sea!"
              "\nWell Played. Better Luck Next Time!")

else:
    print("\nPlaying it safe I see...Well, there is no greater treasure than life itself. "
          "Bye for now. Good Luck with your future adventures.")
