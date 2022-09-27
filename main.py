import random

print("A static humanoid has dragged you into your TV.")
print(
    " You passed out after it stabbed you in the chest. You woke up in a nature filled world. You look at your chest, where that being stabbed you and there was a hole through the shirt, but not in you. You stand up and look around. A trio of goblins are standing around you. It seemed to be 3 well dressed goblins. One bigger than the other. The static humanoid sits in a throne behind the goblins. The static is wearing a suit? You turn around and see a shop where you can buy things from."
)
print("Hint: you can attack, or heal")

player_health = 100
goblin_1 = 100
goblin_2 = 150
goblin_3 = 200
boss = 1500
gold = 0

while player_health > 0 and goblin_1 > 0:
    while True:
        player_act = input("> ")
        if (player_act == "attack" or player_act == "heal"):
            break
        else:
            print("Please choose a valid input!")

    goblin1_type_number = random.randint(1, 2)
    if goblin1_type_number == 1:
        enemy1_type = "attack"
    elif goblin1_type_number == 2:
        enemy1_type = "heal"

    if player_act == "attack":
        print(f"You attacked the goblin!")
        goblin_1 -= random.randint(10, 30)
    if enemy1_type == "attack":
        print("The Goblin attacked you!")
        player_health -= random.randint(5, 15)
    if player_act == "heal":
        print("You healed...")
        player_health += random.randint(10, 30)
    if enemy1_type == "heal":
        print("The Goblin fixes his tie...")
        goblin_1 += random.randint(5, 15)

    print(f"Player health: {player_health}")
    print(f"Goblin one's health: {goblin_1}")

if player_health <= 0:
    print("You were defeted by Goblins!\n")
    quit()
elif goblin_1 <= 0:
    print("You defeated the first Goblin!\n")
    print("You collected ten gold")
    gold += 10

if goblin_1 <= 0:
    buy = input("Buy items? [yes or no] ")
while buy == "yes":
    print("What would you like to buy?")
    print("Upgrade Health (1)")
    print("Eat (2)")
    print("Buy forbiden objects (3)")
    print("Leave shop (4)")
    print("Amount of gold:", gold)
    shop = input("> ")
    if shop == "1":
        print("that would be 50 gold")
        print("Confirm?")
        atgold = input("> ")
        if atgold == "yes":
            if gold < 50:
                print("You dont have enough...")
                pass
            else:
                print("Sold!")
                player_health += random.randint(50, 100)
                print("Health:", player_health)
                gold -= 50
                pass
        else:
            pass
    elif shop == "2":
        print("Eating gives you 10-50 health, depending on your luck...")
        print("Would you like to test you luck? (10 gold)")
        eat = input("> ")
        if eat == "yes":
            if gold < 10:
                print("You dont have enough...")
                pass
            else:
                player_health += random.randint(10, 50)
                print("You gained some health!")
                print("Health:", player_health)
                gold -= 10
                pass
        else:
            pass
    elif shop == "3":
        print("THE FORBIDIN OBJECTS...")
        print("The Unknown product is for 200 gold")
        print("Buy it?")
        forbid = input("> ")
        if forbid == "yes":
            if gold < 200:
                print("You dont have enough...")
                pass
            else:
                print("Have MERCY on their souls...")
                print("You have obtained the binky on a string...")
                print("You wear it and suck on it.")
        else:
            pass
    elif shop == "4":
        break
    else:
        print("Can't understand what your answer is...")
        pass

print("The second Goblin emerges, what will you do now?")

while player_health > 0 and goblin_2 > 0:
    while True:
        player_act = input("> ")
        if (player_act == "attack" or player_act == "heal"):
            break
        else:
            print("Please choose a valid input!")

    goblin2_type_number = random.randint(1, 2)
    if goblin2_type_number == 1:
        enemy2_type = "attack"
    elif goblin2_type_number == 2:
        enemy2_type = "heal"

    if player_act == "attack":
        print(f"You attacked the goblin!")
        goblin_2 -= random.randint(30, 50)
    if enemy2_type == "attack":
        print("The Goblin attacked you!")
        player_health -= random.randint(25, 45)
    if player_act == "heal":
        print("You healed...")
        player_health += random.randint(30, 50)
    if enemy2_type == "heal":
        print("The Goblin throws bullets at the other goblin...")
        goblin_2 += random.randint(25, 30)

    print(f"Player health: {player_health}")
    print(f"Goblin two's health: {goblin_2}")

if player_health <= 0:
    print("You were defeated by Goblins!\n")
    quit()
elif goblin_2 <= 0:
    print("You defeated the second Goblin!\n")
    print("You collected 90 gold")
    gold += 90

if goblin_2 <= 0:
    buy = input("Buy items? [yes or no] ")
while buy == "yes":
    print("What would you like to buy?")
    print("Upgrade Attacks (1)")
    print("Eat (2)")
    print("Buy forbiden objects (3)")
    print("Leave shop (4)")
    print("Amount of gold:", gold)
    shop = input("> ")
    if shop == "1":
        print("that would be 50 gold")
        print("Confirm?")
        atgold = input("> ")
        if atgold == "yes":
            if gold < 50:
                print("You dont have enough...")
                pass
            else:
                gold -= 50
                player_health += random.randint(100, 200)
                print("Sold!")
                print("Health:", player_health)
                pass
        else:
            pass
    elif shop == "2":
        print("Eating gives you 50-100 health, depending on your luck...")
        print("Would you like to test you luck? (30 gold)")
        eat = input("> ")
        if eat == "yes":
            if gold < 30:
                print("You dont have enough...")
                pass
            else:
                player_health += random.randint(50, 100)
                print("You gained health!")
                print("Health:", player_health)
                gold -= 30
                pass
        else:
            pass
    elif shop == "3":
        print("THE FORBIDIN OBJECTS...")
        print("The Unknown product is for 200 gold")
        print("Buy it?")
        forbid = input("> ")
        if forbid == "yes":
            if gold < 200:
                print("You dont have enough...")
                pass
            else:
                print("Have MERCY on their souls...")
                print("You have obtained the binky on a string...")
                print("You wear it and suck on it.")
                static = random.randint(99, 100)
        else:
            pass
    elif shop == "4":
        break
    else:
        print("Can't understand what your answer is...")
        pass

print(
    "The third Goblin pokes you with a shotgun and yells 'bleck kek kek kek'!")
print("what now?")

while player_health > 0 and goblin_3 > 0:
    while True:
        player_act = input("> ")
        if (player_act == "attack" or player_act == "heal"):
            break
        else:
            print("Please choose a valid input!")

    goblin3_type_number = random.randint(1, 2)
    if goblin3_type_number == 1:
        enemy3_type = "attack"
    elif goblin3_type_number == 2:
        enemy3_type = "heal"

    if player_act == "attack":
        print(f"You attacked the shotgun Goblin!")
        goblin_3 -= random.randint(45, 65)
    if enemy3_type == "attack":
        print("The shotgun Goblin shot you!")
        player_health -= random.randint(40, 60)
    if player_act == "heal":
        print("You healed...")
        player_health += random.randint(60, 80)
    if enemy3_type == "heal":
        print("The Goblin reloads his shotgun...")
        goblin_3 += random.randint(50, 60)

    print(f"Player health: {player_health}")
    print(f"Goblin three's health: {goblin_3}")

if player_health <= 0:
    print("You were Shot by Goblins!\n")
    quit()
elif goblin_3 <= 0:
    print("You defeated the shotgun Goblin!\n")
    print("You collected 100 gold")
    gold += 100

if goblin_3 <= 0:
    buy = input("Buy items? [yes or no] ")
while buy == "yes":
    print("What would you like to buy?")
    print("Upgrade Attacks (1)")
    print("Eat (2)")
    print("Buy forbiden objects (3)")
    print("Leave shop (4)")
    print("Amount of gold:", gold)
    shop = input("> ")
    if shop == "1":
        print("that would be 50 gold")
        print("Confirm?")
        atgold = input("> ")
        if atgold == "yes":
            if gold < 50:
                print("You dont have enough...")
                pass
            else:
                gold -= 50
                player_health += random.randint(200, 400)
                print("Sold!")
                print("Health:", player_health)
                pass
        else:
            pass
    elif shop == "2":
        print("Eating gives you 1-1000 health, depending on your luck...")
        print("Would you like to test you luck? (100 gold)")
        eat = input("> ")
        if eat == "yes":
            if gold < 100:
                print("You dont have enough...")
                pass
            else:
                player_health += random.randint(1, 1000)
                print("You gained health!")
                print("Health:", player_health)
                gold -= 100
                pass
        else:
            pass
    elif shop == "3":
        print("THE FORBIDIN OBJECTS...")
        print("The Unknown product is for 200 gold")
        print("Buy it?")
        forbid = input("> ")
        if forbid == "yes":
            if gold < 200:
                print("You dont have enough...")
                pass
            else:
                print("Have MERCY on their souls...")
                print("You have obtained the binky on a string...")
                print("You wear it and suck on it.")
                player_health += random.randint(900, 1100)
                print("Health:", player_health)
                gold -= 200
        else:
            pass
    elif shop == "4":
        break
    else:
        print("Can't understand what your answer is...")
        pass

print("The Static stands up from his throne and walks towards you!")
print("It looks serious now")

while player_health > 0 and boss > 0:
    while True:
        player_act = input("> ")
        if (player_act == "attack" or player_act == "heal"):
            break
        else:
            print("Please choose a valid input!")

    boss_type_number = random.randint(1, 2)
    if boss_type_number == 1:
        boss_type = "attack"
    elif boss_type_number == 2:
        boss_type = "heal"

    if player_act == "attack":
        print(f"You attacked the static!")
        boss -= random.randint(210, 320)
    if boss_type == "attack":
        print("The Static attacked you!")
        player_health -= random.randint(250, 350)
    if player_act == "heal":
        print("You healed...")
        player_health += random.randint(69, 420)
    if boss_type == "heal":
        print("The static fixes his suit...")
        boss += random.randint(42, 380)

    print(f"Player health: {player_health}")
    print(f"The Static's health: {boss}")

if player_health <= 0:
    print("You were defeated by the static in charge!\n")
    print("Only if there was something to help you")
    quit()
elif boss <= 0:
    print("You defeated the static!\n")
    print("You win... for now!")
    print("END DEMO")