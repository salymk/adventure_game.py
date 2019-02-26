import time
import random


items = []
enemies = random.choice(["wicked fairie", "ogre", "goblin"])


def print_pause(string):
    print(string)
    time.sleep(1)


def fight():
    while True:
        if "magical sword" in items:
            print_pause("As the " + enemies + " moves to attack, "
                        "you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your "
                        "hand as you brace yourself for the attack.")
            print_pause("But the " + enemies + " takes one look at "
                        "your shiny new toy and runs away!")
            print_pause("You have rid the town of the " + enemies + ". "
                        "You are victorious!\n")
            print_pause("GAME OVER!")
            break
        else:
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the " + enemies + ".")
            print_pause("You have been defeated!\n")
            print_pause("GAME OVER!")
            break


def run():
    print_pause("You run back into the field. "
                "Luckily, you don't seem to have been followed.\n")


def field():
    print_pause("You find yourself standing in an "
                "open field, filled with grass and yellow wildflower.")
    print_pause("Rumor has it that a " + enemies + " is "
                "somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the "
                "door opens and out steps a " + enemies + ".")
    print_pause("Eep! This is the " + enemies + "'s house!")
    print_pause("The " + enemies + " attacks you!")
    if "magical sword" not in items:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")


def cave():
    if "magical sword" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.\n")
        print_pause("You walk back out to the field.\n")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
        print_pause("You walk back out to the field.\n")
        items.append("magical sword")


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            return response
        elif option2 in response:
            return response
        else:
            print_pause("Sorry, I don't understand.")


def play_game():
    field()
    while True:

        choice = valid_input("Enter 1 to knock on the door of the house.\n"
                             "Enter 2 to peer into the cave.\n"
                             "What would you like to do?\n"
                             "(Please enter 1 or 2.)\n", '1', '2')
        if '1' in choice:
            house()
            battle = valid_input("Would you like to "
                                 "(1) fight or (2) run away?\n",
                                 '1', '2')
            if '1' in battle:
                fight()
                break
            elif '2' in battle:
                run()
        elif '2' in choice:
            cave()

    play_again = valid_input("Would you like to play again? (y/n)\n",
                             'y', 'n')

    if 'n' in play_again:
        print_pause("Thanks for playing! See you next time.")
    elif 'y' in play_again:
        print_pause("Excellent! Restarting the game ...\n")
        if "magical sword" in items:
            items.remove("magical sword")
        play_game()


play_game()
