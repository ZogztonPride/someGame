import random
import time

attackCD = 0
dodgeCD = 0


class Enemy:
    def __init__(self,hp):
        self.hp = hp
    
while True:
    print(" ")
    e = None
    if e == None:
        e = Enemy(random.randint(0,5))
        print("A new enemy aproaches!")
        print(" ")
        time.sleep(1)
        
    print("Options:")
    print("Strike: Deal some damage to the enemy. Cooldown: " + str(attackCD))
    print("Dodge: Dodge an incoming attack. Cooldown: " + str(dodgeCD))
    print("GiveUp: Give up like the coward you are.")
    print("")
    x = input("What is your aproach:")
    print("")
    if x.lower() == "strike":
        dmg = random.randint(1,2)
        e.hp -= dmg
        print("You strike your enemy with " + str(dmg) + " points of damage, leaving the enemy at " + str(e.hp) + " hitpoints!")
    elif x.lower() == "dodge":
        print("You dodged the enemy, even though he can't attack yet in the current state of this shiz program")
    elif x.lower() == "giveup":
        print("COWARD!")
        break
    else:
        print("I do not understand gibberish")
    
    if e.hp <= 0:
        print("You slayed your foe!")
        e == None
    time.sleep(2)

