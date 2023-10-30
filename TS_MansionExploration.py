"""

Thomas Sheehan
CYOA Project - Mansion Exploration
Intensive Data Science II
10/19/23

"""

import sys
from time import sleep
import random


def print_slow(text):
    """A function that prints one character at a time."""
    for x in text:                    # Cycle through the text
        print(x, end='', flush=True)  # Print character, no new line
        sleep(0.02)                   # Delay between characters
    print()                           # New line
    sleep(0.5)                        # Delay after finishing the line


def choose(valid_choices):
    """Prompts the user to enter one of several valid choices,
    where valid_choices is a list of desired values."""
    for i in range(5):
        choice = input("Enter your choice: ")
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Try again.")
    else:
        # Prompt for if user runs out of attempts
        print("You have run out of attempts. GAME OVER")
        sys.exit()


# Asking user for name

name = input("Before leaving to go on a hike, you must write your name on your belongings:    ")
dogname = input("You also can't forget to feed your beloved doggy named:    ")

# Starting Narration

print_slow("On your late night hike through the woods, you come across an "
           "abandonded mansion. Do you choose to explore it?")
print_slow("Yes: 1")
print_slow("No: 2")

choice = choose(["1", "2"])

if choice == "1":    # Beginning
    print_slow("Ah, a brave one. You have entered the mansion.")
    print()
    print_slow("Inside the mansion you are met with two doors. Which one shall you enter?")
    print_slow("Door 1: 1")
    print_slow("Door 2: 2")

    choice = choose(["1", "2"])

    if choice == "1":           # Masked Man Path
        print_slow("You walk into a brightly lit bedroom and hear noises coming from the closet.")
        print()
        print_slow("Do you choose to open the closet or run away?")
        print_slow("Open the closet: 1")
        print_slow("Run Away: 2")

        choice = choose(["1", "2"])

        if choice == "1":          # Masked Man Death Ending
            print_slow("A masked man jumps out and kills you. GAME OVER")
        elif choice == "2":
            print_slow("You make it home. Do you choose to lock your door?")
            print()
            print_slow("Yes: 1")
            print_slow("No: 2")

            choice = choose(["1", "2"])

            if choice == "1":           # Locked Door Ending
                print_slow("A masked man tries to open the door, but fails. "
                           "You survived the night, well done.")
            elif choice == "2":
                print_slow("A masked man enters through your unlocked door, "
                           "laughing at your ignorance.")
                print_slow("He chooses to steal your dog and spare your life.")
                print()
                print_slow("The fate of your dog is now out of your hands.")
                print()
                coin = random.randint(1, 2)

                if coin == 1:            # Dog Returns Ending
                    print_slow("Your dog comes back and you live together happily ever after.")
                elif coin == 2:          # Dog Gone Forever Ending
                    print_slow(f"You wait by the window everyday, but {dogname} never returns. "
                               f"{name}, you might have survived, but have lost your only true companion. GAME OVER")

    elif choice == "2":         # Old Woman Path
        print_slow("You shove open the stubborn door and see an old woman "
                   "standing motionless across from you.")
        print()
        print_slow("Do you approach the woman or run away?")
        print_slow("Approach her: 1")
        print_slow("Run away: 2")

        choice = choose(["1", "2"])

        if choice == "1":
            print_slow("The woman is surpised and impressed. Every person to "
                       "explore the mansion has run from her, but you chose to talk.")
            print()
            print_slow("She offers you the riches of the mansion...gold and ancient art.")
            print_slow("Will you accept her offer?")
            print_slow("Yes: 1")
            print_slow("No: 2")

            choice = choose(["1", "2"])

            if choice == "1":           # Best Ending
                print_slow("You leave with millions worth of riches and a new friend!")
                print_slow(f"You have truly gotten the most out of the mansion. Well done, {name}.")

            elif choice == "2":            # Rejecting The Woman's Offer Ending
                print_slow("The woman feels disrepected and becomes furious.")
                print_slow("She wipes the tears from her face and "
                           "charges at you, killing you almost instantly. GAME OVER")

        elif choice == "2":            # Run Away From Old Woman Ending
            print_slow("The woman hates cowards. She chases and kills you. GAME OVER")


elif choice == "2":            # Avoiding Mansion Death Ending
    print_slow("Coward. You get kidnapped on the way home, never to be seen again. GAME OVER.")
