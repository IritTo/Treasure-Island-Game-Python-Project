print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First choice at the crossroad
choice1 = input("You are at a crossroad. Where would you go, left or right? (l/r) ").lower()

if choice1 == "l":
    # Second choice at the lake
    choice2 = input("You have turned left and found yourself in front of a lake. "
                    "There is an island in the middle of the lake. Will you swim across or wait for a boat? (s/w) ").lower()

    if choice2 == "w":
        # Third choice at the island
        choice3 = input(
            "You arrive at the island unharmed. There is a house inside there is a table with three boxes: one red, one yellow, and one blue. "
            "Which color do you choose? (r/y/b) ").lower()

        if choice3 == "y":
            print("You found the treasure! You win!")
        elif choice3 == "r":
            print("It's a box full of arrows that hit and kill you. Game over.")
        elif choice3 == "b":
            print("You open the box and a swarm of wild bees attacks you. Game over.")
        else:
            print("You chose a box that is empty. Game over.")
    else:
        print("You have been eaten by piranhas. Game over.")

elif choice1 == "r":
    # Second choice in the forest
    choice2 = input("You have turned right and entered a dense forest. "
                    "You see a path that splits into two: one path leads to a cave, the other to a village. "
                    "Which path do you choose? (c/v) ").lower()

    if choice2 == "c":
        # Third choice in the cave
        choice3 = input(
            "Inside the cave, you find a sleeping three-headed monster and a treasure chest. "
            "Do you take the treasure or leave quietly? (t/l) ").lower()

        if choice3 == "t":
            print("The three-headed monster wakes up and devours you. Game over.")
        else:
            print("You leave quietly. You win!")
    else:
        # Scenario for the village path
        choice3 = input(
            "You arrive at a village where the villagers are celebrating. They offer you food and shelter. "
            "Do you join the celebration or continue your journey? (j/c) ").lower()

        if choice3 == "j":
            print("You eat some of the food and feel sleepy. It was poisoned. Game over.")
        else:
            print("You continue your journey and find the treasure hidden in the forest. You win!")

else:
    print("You fell into a hole. Game over.")




