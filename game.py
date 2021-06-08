import random
import time
from classes import TestCharacter
from classes import Fencer
from classes import Enemy

killcount = 0
p = None
#Character select
print("Character Select!")
print("TestCharacter")
print("Fencer")
while True:
    x = input("Choose your character: ")
    if x.lower() == "testcharacter":
        p = TestCharacter()
        break
    elif x.lower() == "fencer":
        p = Fencer()
        break
    else:
        print("Please input a real character.")

e = None    

while True:
    print(" ")
    
    #Checks if there are any enemy present. If not, it creates a new Enemy instance
    if e == None or e.hp <= 0:
        e = Enemy(random.randint(3,7))
        print("A new enemy aproaches with " + e.displayHP() + " hitpoints!")
        print(" ")
        time.sleep(1)
    #The enemy chooses an attack
    e.chooseAttack()
    time.sleep(1)
    p.chaHelp
    x = ""
    #print("light: " + str(e.lightAttackCD) + " medium: " + str(e.mediumAttackCD) + " heavy: " + str(e.heavyAttackCD))
    print("")
    #The player types a command to choose an attack, or option
    while True:
        x = input("What is your aproach:")
        #Brings out the list of commands.
        if x.lower() == "help":
            p.chaHelp
        #Displays the players hp.
        elif x.lower() == "hp":
            print("You have " + p.displayHP() + " hitpoints.")
        #Displays the enemy's hp.
        elif x.lower() == "enemyhp":
            print("Your enemy has " + e.displayHP() + " hitpoints.")
        #Quits the game. Rename the input later
        elif x.lower() == "giveup" or x.lower() == "g":
            print("COWARD!")
            break
        else:
            if p.chooseAttack(x) == True:
                break
            else:
                print("Attack is on cooldown.")
    
    #Is here to fully break out of the loop
    if x.lower() == "giveup" or x.lower() == "g":
        break    
    time.sleep(1)
    
    #This is the section where the damage result is calculated
    pA = p.commitAttack()
    eA = e.commitAttack()
    
    #ForceClash
    if pA == -1:
        pA = eA

    
    if pA == -2: 
        #Fencer Riposte
        e.hp -= eA
        print("You riposte the attack, and strike an equal blow, dealing " + str(eA) + " damage, leaving it with " + e.displayHP() + " hitpoints!")
    else:   
        
        if pA > eA:
            #Player wins the round
            e.hp -= pA - eA
            print("You strike your enemy with " + str(pA - eA) + " damage, leaving it with " + e.displayHP() + " hitpoints!")
        
        elif pA < eA:
            #Enemy wins the round
            p.hp -= eA - pA
            print("You are struck by your foe with " + str(eA - pA) + " damage, leaving you with " + p.displayHP() + " hitpoints!")
        else:
            if p.type == "fencer":
                #Fencer passive ability
                r = random.randint(1,2)
                e.hp -= r
                print("You clash with the enemy, and slice your it before it recovers, dealing " + str(r) + " damage, leaving it with " + e.displayHP() + " hitpoints!")
            else:
                #Neither the Player or Enemy wins the round
                print("You clash with the enemy!")
    p.cooldownOptions()
    p.cooldownClass()
    e.cooldownOptions()
    #This is the section for checking if anyone died
    if p.hp <= 0:
        #Checks if the player died
        print("You are dead now, and will never return. You slayed " + str(killcount) + " enemies.")
        break
    
    if e.hp <= 0:
        #Checks if the enemy is dead
        print("You slayed your foe!")
        killcount += 1
        if p.specialCooldown > 0:
            p.specialCooldown -= 1
        if killcount % 4 == 0:
            p.hp += 2
            if p.maxHp < p.hp:
                p.hp = p.maxHp
        print("You have healed a bit of health! You are now at " + str(p.displayHP()) + " hp.")
    time.sleep(2)