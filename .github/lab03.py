import random

# dice options created usinglist() and range()
disceOptions = list(range(1,7))

# weapons list
weapons = ["Fist", "knife", "Club", "Bomb", "Nuclear Bomb"]

print("Available Weapons: ", ', '.join(weapons))

def getCombatStength(prompt):
    while True:
        value = int(input(prompt))
        if 1 <= value <= 6:
            return value
    else:
        print("Invalid Input! Please enter a number between 1-6")

CombatStength = getCombatStength("Please enter a number between 1-6 for player")
mCombatStength = getCombatStength("Please enter a number between 1-6 for monster")


for j in range(1, 21, 2):
    heroRoll = random.choice(disceOptions)
    monsterRoll = random.choice(disceOptions)

    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    heroTotal = CombatStength + heroRoll
    monsterTotal = mCombatStength + monsterRoll

    print(f"\n Hero rolled {heroRoll}, Monster rolled {monsterRoll}")
    print(f"\n Hero selected {heroWeapon}, Monster selected {monsterWeapon}")
    print(f"\n Hero Total Strength {heroTotal}, Monster Total strength {monsterTotal}")

    if heroTotal > monsterTotal:
        print("Hero Wins!")
    elif heroTotal < monsterTotal:
        print("Monster Wins!")
    else:
        print("Its a tie!")