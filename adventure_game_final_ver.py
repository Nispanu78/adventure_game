import time
import random

monsters = ["troll", "bugbear", "orc"]
actual_monster = random.choice(monsters)

weapon = ["sword of Ogoroth", "spear of Leothas",
          "poisoned dagger of Vannaras"]
current_weapon = random.choice(weapon)

monster_weapon = ["two-hand sword", "enormous flanged mace",
                  "morning-star"]
enemy_weapon = random.choice(monster_weapon)

monster_attack = ["hit you with powerful cutting blows "
                  "that try to reach the vital parts "
                  "of your body",
                  "hit you with blows from "
                  "top to bottom as well as "
                  "with lateral ones"]
enemy_attack = random.choice(monster_attack)

hero_attacks = ["you mortally hit your enemy in the "
                "head and stomach.",
                "you cut the monster's arm in two and "
                "take advantage of this to deliver "
                "mortal blows to him.",
                "you take advantage of the "
                "monster's slowness to hit his legs; "
                "once he is unable to stand, "
                "you finish him."]

hero_counterattack = random.choice(hero_attacks)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with tall grass and yellow wildflowers.\n")
    print_pause("Rumor has it that a " + actual_monster +
                " is somewhere around here, "
                "and has been terrifying\n"
                "the nearby village.")
    print_pause("In your hand you hold your "
                "not very effective training dagger, "
                "unfortunately you are so poor \n"
                "that you cannot afford a better weapon.")


def house(items):
    print_pause("You approach the entrance of the hut.")
    print_pause("Suddenly out steps a" + " " + actual_monster)
    print_pause("The " + actual_monster + " attacks you!")
    fight(items)


def cave(items):
    print_pause("You peer cautiously into the cave.")
    if current_weapon in items:
        print_pause("The cave is now empty, there is not much to do here.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind some rocks.")
        print_pause("You have found the " + current_weapon + "!")
        print_pause("You discard your training dagger and "
                    "take your new weapon with you.")
        items.append(current_weapon)
        print("You walk back out to the field")
    entrance(items)


def victory(items):
    print_pause("As the " + actual_monster +
                " moves to attack, you wield your weapon")
    print_pause("The " + current_weapon +
                " shines brightly in your hand "
                "as you brace yourself for "
                "the " + actual_monster + "'s attack")
    print_pause("The " + actual_monster +
                " brandishes his " + enemy_weapon +
                " and tries to " + enemy_attack +
                " but you dodge some of his attacks and block others "
                "with your new weapon.")
    print_pause("Once it his your time to counterattack "
                + hero_counterattack)
    print_pause("You have rid the town of the " + actual_monster +
                ". Inside the monster's den you find a considerable "
                "treasure that will made you rich! "
                "your are victorious! "
                "GAME OVER!")
    play_again(items)


def fight(items):
    alternative = input("Would you like to 1 fight or 2 run away? ")
    if "1" in alternative:
        if current_weapon in items:
            victory(items)
        else:
            print_pause("You feel a bit under-prepared for this, "
                        "with only having a training dagger.")
            print_pause("You do your best but your dagger "
                        "is no mach for the " + actual_monster +
                        ". He manages to "
                        + enemy_attack +
                        ", the fury of his attacks overwhelms"
                        " you till his blows cuts through your "
                        "vital organs.")
            print_pause("You have been defeated!\n"
                        "GAME OVER!")
            items.append(items)
            play_again(items)
    if "2" in alternative:
        print("The " + actual_monster +
              " is very slow and you manage "
              "to run away from him\n"
              "and hide inside the tall grass. "
              "Luckily, you don't seem to "
              "have been followed.")
        entrance(items)


def entrance(items):
    while True:
        choice = input("In front of you stand a derelict hut and a cave.\n"
                       "Enter 1 to enter the hut. "
                       "Enter 2 to peer into the cave "
                       "(Please enter 1 or 2) ")
        if choice == "1":
            house(items)
        elif choice == "2":
            cave(items)
        else:
            print("Please choose either option 1 or 2")


def play_again(items):
    while True:
        choice = input("Do you want to play again? (y/n) ")
        if "y" in choice:
            print_pause("Excellent...restarting the game")
            play_game()
        elif "n" in choice:
            print("Thank you for playing")
        else:
            print("Please choose either 'y' or 'n'")


def play_game():
    items = []
    intro()
    entrance(items)
    play_again(items)


play_game()
