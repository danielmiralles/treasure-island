image = """
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=\"\"_;=.______________|_____________________|_______
|                   |  ,-\"_,=\"\"     `\"=.|                  |
|___________________|__\"=._o`\"-._        `\"=.______________|___________________
          |                `\"=._o`\"=._      _`\"=._                     |
 _________|_____________________:=._o \"=._.\"_.-=\"'\"=.__________________|_______
|                   |    __.--\" , ; `\"=._o.\" ,-\"\"\"-._ \".   |
|___________________|_._\"  ,. .` ` `` ,  `\"-._\"-._   \". '__|___________________
          |           |o`\"=._` , \"` `; .\". ,  \"-._\"-._; ;              |
 _________|___________| ;`-.o`\"=._; .\" ` '`.\"\` . \"-._ /_______________|_______
|                   | |o;    `\"-.o`\"=._``  '` \" ,__.--o;   |
|___________________|_| ;     (#) `-.o `\"=.`_.--\"_o.-; ;___|___________________
____/______/______/___|o;._    \"      `\".o|o_.--\"    ;o;____/______/______/____
/______/______/______/_\"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__\"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____\"=._o._; | ;_.--\"o.--\"_/______/______/______/_
____/______/______/______/______/_____\"=.o|o_.--\"\"___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
"""
print(image)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

direction = input("What direction would you like to (left or right) ? ")

if direction == "left":
    print("You find a boat and a lake.")
    action = input("What action would you like to (swim or wait) ? " )
    if action == "wait":
        print("You find three doors with different colors, blue, red and yellow")
        color = input("What color would you like to select ? ")
        if color.lower() == "yellow":
            print("You Win!!!!!!")
        elif color.lower() == "blue":
            print("You are eating by several beasts.")
            print("Game Over")
        elif color.lower() == "red":
            print("You are burned by fire")
            print("Game Over")
        else:
            print("Game Over")
    else:
        print("You are attacked by trouts")
        print("Game Over")
else:
    print("You fall into a hole")
    print("Game Over")
