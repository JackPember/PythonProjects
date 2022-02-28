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

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

beach = input(
    '''You land on the beach of Treasure Island. You notice three options to get to the center of the island and claim the treasure. You can either 1: go straight through the jungle, 2: walk to the left and go through a cave, or 3: go to the right along the beach to see what\'s there. Type \"Straight\",\"Left\"or\"Right\" \n''')
if beach == "Straight":
    monkey = input(
        '''You make your way through the jungle, to find a monkey hanging from a tree. The monkey beckons you to follow him. Will you follow him or will you keep going? Type \"Yes\" or \"No\" \n''')
    if monkey == "Yes":
        print(
            '''The monkey swings along the trees, leading you through a path in the jungle. But the monkey was up to no good, following him led you to fall into a pit that the monkey had set up earlier! He laughs and runs away. Game Over.''')
    if monkey == "No":
        lakeJG = input(
            '''You decided not to follow the monkey. You keep hacking through the dense vines of the jungle, to find a lake in the middle of the island, and an island within that lake. There is a little shack on the island, it must be the treasure, bingo! You notice a raft floating towards you. Type \"Wait\" to wait for the raft. If you're feeling impatient, type \"Swim\" to attempt to swim to the treasure.\n ''')
        if lakeJG == "Swim":
            print(
                '''You are impatient and decide to swim across. You make it about halfway through, but then suddenly hungry piranhas swim up to you and they look hungry! Game Over.''')
        elif lakeJG == "Wait":
            print(
                '''You decide to wait for the raft. It takes 20 minutes, but it finally arrives. You step on and use a nearby branch to steer towards the treasure.''')
            choiceLakeJG = input(
                '''You notice that the shack has three doors. One green, one purple, and one orange. Type \"Green\", \"Purple\", or \"Orange\" to pick the door containing the treasure.\n ''')
            if choiceLakeJG == "Green":
                print(
                    '''You open the green door and enter a room full of venemous snakes! The door locks behind you! Game Over.''')
            elif choiceLakeJG == "Purple":
                print(
                    '''You open the purple door and enter a room that contains purple energy crystals. The door locks behind you! They are beautiful, but they radiate too much energy and zap you! Game Over!''')
            elif choiceLakeJG == "Orange":
                print(
                    '''"You open the orange door and discover the treasure! But the door locks behind you! Fortunately, the treasure happens to contain the key, you open the door and make it out safely. You Win!''')
            else:
                print('''You picked a door that does not exist. Game Over.''')
elif beach == "Left":
    fork = input(
        '''You enter the cave and make your way through. You notice that it is getting darker and there are two paths in the cave now. The path on the left has a torch on the wall for you to grab and take, the path on the right is pitch black. Type \"Left\" or \"Right\" to pick your direction.\n ''')
    if fork == "Left":
        print(
            '''You take the torch and make your way through the cave. Suddenly, a gust of wind blows your torch out! You keep going and fall into a hole that you couldn\'t see! Game Over.''')
    if fork == "Right":
        choiceCave = input(
            '''You choose the dark path and stumble forward slowly for about 15 minutes. You eventually make it out on the other side, and see that there is a lake that contains a small island with a little shack. You notice that there is a small bridge that goes directly to the shack, how convenient! You walk up to the shack and notice three doors, one green, one purple, and one orange. Type \"Green\", \"Purple\", or \"Orange\" to pick the door containing the treasure. \n''')
        if choiceCave == "Green":
            print(
                '''You open the green door and enter a room full of venemous snakes! The door locks behind you! Game Over.''')
        elif choiceCave == "Purple":
            print(
                '''You open the purple door and enter a room that contains purple energy crystals. The door locks behind you! They are beautiful, but they radiate too much energy and zap you! Game Over!''')
        elif choiceCave == "Orange":
            print(
                '''"You open the orange door and discover the treasure! But the door locks behind you! Fortunately, the treasure happens to contain the key, you open the door and make it out safely. You Win!''')
        else:
            print('''You picked a door that does not exist. Game Over.''')
elif beach == "Right":
    riverChoice = input(
        '''You decide to go around the island to the right, and you come across a river. You notice that there is a rock path that you might be able to use to cross the river. There is also a small narrow opening at the base of the river that you notice. However, it is filled with water, so who knows if it is safe or not. Type \"Rocks\" to cross using the rock path, or type \"Opening\" to take the narrow opening.\n ''')
    if riverChoice == "Rocks":
        print(
            '''You start to cross the rock path at a steady pace. It starts to feel a little slippery though, Oh No! You slip and fall and hit your head too hard! Game Over.''')
    elif riverChoice == "Opening":
        choiceRiver = input(
            '''You go through the little opening and walk through. It is filled with water, so you slowly wade through. Fortunately, the water is only up to your chest, so you can still breathe. You come through to the other side and find yourself on a small island on a lake that has a little shack on it. You notice three doors; one green, one purple, and one orange. Type \"Green\", \"Purple\", or \"Orange\" to pick the door containing the treasure.\n ''')
        if choiceRiver == "Green":
            print(
                '''You open the green door and enter a room full of venemous snakes! The door locks behind you! Game Over.''')
        elif choiceRiver == "Purple":
            print(
                '''You open the purple door and enter a room that contains purple energy crystals. The door locks behind you! They are beautiful, but they radiate too much energy and zap you! Game Over!''')
        elif choiceRiver == "Orange":
            print(
                '''"You open the orange door and discover the treasure! But the door locks behind you! Fortunately, the treasure happens to contain the key, you open the door and make it out safely. You Win!''')
        else:
            print("You picked a door that does not exist. Game Over.")
else:
    print("You did not choose a valid path. Game Over.")






