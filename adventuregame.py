import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def intro(item, option):
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.\n")
    print_pause("Ancient folklore has it that a " + option + " is somewhere around "
                "here, and has been terrifying the nearby town.\n")
    print_pause("In front of you is a haunted manor.\n")
    print_pause("To your right is a dark dungeon.\n")
    print_pause("In your arsenal you hold a rusty and dull knife.\n")


def dungeon(item, option):
    if "sword" in item:
        print_pause("\nYou look cautiously into the dark dungeon.")
        print_pause("\nYou've visited here before, and gotten all"
                    " the loot boxes. It's just an dark silent dungeon"
                    " now.")
        print_pause("\nYou walk back to the field.\n")
    else:
        print_pause("\nYou peer cautiously into the dungeon.")
        print_pause("\nIt turns out to be only a level 1 dungeon.")
        print_pause("\nYou sense a reflection of metal behind a "
                    "an old tombstone.")
        print_pause("\nYou have found the magical Heavy Sword of Rathamon!")
        print_pause("\nYou discard your useless dull knife and take "
                    "the Heavy sword with you.")
        print_pause("\nYou walk back out to the field.\n")
        item.append("sword")
    field(item, option)


def manor(item, option):
    print_pause("\nYou approach the door of the manor.")
    print_pause("\nReady to knock when the door "
                "opens and out appears a " + option + ".")
    print_pause("\nHoly smokes! This is the " + option + "'s manor!")
    print_pause("\nThe " + option + " lunges at you!\n")
    if "sward" not in item:
        print_pause("You feel a outclassed for this, "
                    "what with only having a worn out knife.\n")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "flee?")
        if choice2 == "1":
            if "sword" in item:
                print_pause("\nAs the " + option + " moves to charge at you, "
                            "you draw your heavy sword.")
                print_pause("\nHeavy Sword of Rathamon powers through "
                            "your hand as you are ready to strike with a heavy "
                            "attack.")
                print_pause("\nBut the " + option + "takes one glance at "
                            "your weapon and scatters into the night!")
                print_pause("\nYou have rid the town of the " + option +
                            ". You are a champion!\n")
            else:
                print_pause("\nYou do what you could...")
                print_pause("but your knife is no contender for the "
                            + option + ".")
                print_pause("\nYou have been slained!\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou run back into the field. "
                        "\nIt appears that you havent been "
                        "tracked.\n")
            field(item, option)
            break

def play_game():
    item = []
    option = random.choice(["zombie pikachu", "dark demon", "evil fairie", "turned centaur",
                            "possessed ronin"])
    intro(item, option)
    field(item, option)


def field(item, option):
    print_pause("Enter 1 to slam on the door of the manor.")
    print_pause("Enter 2 to quietly move into the dungeon.")
    print_pause("What is your next move?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            manor(item, option)
            break
        elif choice1 == "2":
            dungeon(item, option)
            break


def play_again():
    again = input("Play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nGreat! Reloading the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you on the next quest\n\n\n")
    else:
        play_again()





play_game()
