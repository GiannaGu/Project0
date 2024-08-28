import Character from character
import Item from coins
import playWordle from wordle

print("Welcome to the game")
d1 = input("You come up to a field and see a star! Do you want to pick it up? (yes/no)")
if d1 == "yes":
    star = Item("Star", "A shiny star",10)
    d1a = input("You pick up the star and put it in your pocket. Now you see a dude. Want to talk to him? (yes/no)")
    if d1a == "yes":
        character = Character("Dude", 100, [], {"Hello": "Hello! How are you?", "Goodbye": "Goodbye!"})
        character.talk_to_player("Hello")

   
    

