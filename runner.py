"""
This code is part of the main game loop in the 'runner.py' file. It handles the player's interaction with a corn field, including the ability to pick and eat pink or purple corn. The code also handles the player's decision to set up camp, explore the corn field, or try to leave. Depending on the player's choices, the code can lead to various outcomes, including encountering a mysterious creature, solving a puzzle, and finding a valuable locket.
"""
import wordle
from character import Character
from wordle import playWordle
from coins import Item

main_character = Character("Old-Woman", 10000, [], {1: "Hello! How are you?", 2: "Goodbye!"})
main_character.talk_to_player(1)


print("Welcome to the game")
d1 = input("You come up to a field and a lot of stalks of corn, some are purple and some are pink. Do you want to pick a piece of corn? (y/n)")

if d1 == "y":
    corn_color = input("Would you like to pick a pink piece of corn or a purple piece of corn? (pink/purple)")

    
    if corn_color == "pink":
        corn = Item("Pink Corn","A pink corn", -100)
        main_character.recive_item(corn)
        d1a = input("Your stomach starts to rumble, would you like to eat the corn (y/n)")
        if d1a == "y":
            print("You eat the corn and you start to feel strange.Your skin starts to turn bright pink, and you pass out.")
            corn.use_item(main_character)


    if corn_color == "purple":
        corn = Item("Purple Corn","A purple corn",500)
        main_character.recive_item(corn)
        d1b = input("Your stomach starts to rumble, would you like to eat the corn (y/n)")
        if d1b == "y":
            print("You eat the corn and you start to feel strange.Your skin starts to turn bright purple and you begin to float. You instantly feel so much better. ")
            corn.use_item(main_character)
     

else:
    print("you chose to not gather any corn.")
    d2 = input("Its starting to get dark outside, would you like to a) set up camp b)explore the corn field c)try and leave the corn field?")
    if d2 == "a":
        night = input("You set up camp and start a fire,the fire is starting to die down and the smoke is starting to fill the air. Do you want to a) go to sleep b)keep the fire going?")
        if night == "a":
            print("You go to sleep and wake up the next day.")
        if night == "b":
            monsters = input("You keep the fire going, the smoke seems to have alerted people to your location. You start to hear noises approaching you. Do you want to a) run away b)stay and fight?")
            if monsters == "a":
                print("You run away and get lost, you have no where to go and die of starvation.")
            if monsters == "b":
                nice = input("You decide to stay and fight,the creature comes rumbling out of the corn field would you like to a) Try to attack it b) Tell it you come in peace c) cower in fear")
                if nice == "a":
                    print("You attack the creature and it quickly knocks you out to the ground. You wake up in a cage.")
                    cage = input("You are in a cage, would you like to a) try to escape b) wait for help c) look around the cage")
                    if cage == "a":
                        print("You try to escape but the cage and you find it has a puzzle code on the back of the lock.You must solve the lock")
                        wordle.playWordle()
                    if cage == "b":
                        print("You wait for help and the creature comes back and eats you.")
                    if cage == "c":
                        print("You look around the cage and find a golden locket,")
                        locket = Item("Locket","A golden locket", 1000000)
                        main_character.recive_item(locket)
                if nice == "b":
                        print("You tell the creature you come in peace and it as it slowly approches you, you realize that its actually an old woman. She gives you a warm smile")
                        character = Character("Old-Woman", 10000, [], {1: "Hello! How are you?", 2: "Goodbye!"})
                        character.talk_to_player(1)
                if nice == "c":
                        print("You cower in fear and the creature eats you.")
                
    
    if d2 == "b":
        explore = input("You are walking through the corn field and come across an empty camp. Surrounding you is a) pot to cook, b) satchel, c) sleeping bag or d) leave the campsite. Would item would you like to take? ")

    if d2 == "c":
        leave = input("you chose to leave the corn field. You walk for a while and come across a river. You see a boat on the other side of the river. Would you like to a) swim across the river b) try to find a bridge?")

