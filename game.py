import random
import time


class Character:
    def __init__(self,hp):
        self.hp = hp
        self.attackCD = 0

class Player(Character):
    def __init__(self,hp):
        super(self,hp).__init__()
        self.dodgeCD = 0
    
    def cooldownOptions(self):
        if self.attackCD != 0:
            self.attackCD -= 1
        if self.dodgeCD != 0:   
            self.dodgeCD -= 1
        
class Enemy(Character):
    def __init__(self,hp):
        super(self,hp).__init__()
        self.attack = 0
        self.blockCD = 0

    def eCooldownOptions(self):
        if self.attackCD != 0:
            self.attackCD -= 1
        if self.blockCD != 0:   
            self.blockCD -= 1
    
    def eChooseAttack(self):
        while True:
            n = random.randint(0,1)
            if n == 0:
                if self.eAttackCD == 0:
                    print("The enemy is trying to strike you!")
                    self.attack = 0
                    break
            if n == 1:
                if self.eBlockCD == 0:
                    print("The enemy is preparing for a blow")
                    self.attack = 1
                    self.eBlockCD += 2
                    break
    
    def eCommitAttack(self):
        if self.attack == 0:
            return 0
        elif self.attack == 1:
            return 0
        

        

p = Player(10)
e = None    

#Displays commands
def help():
    print("Options:")
    print("Strike: Deal some damage to the enemy. Cooldown: " + str(p.attackCD))
    print("Dodge: Dodge an incoming attack. Cooldown: " + str(p.dodgeCD))
    print("Help: Get a list of commands.")
    print("GiveUp: Give up like the coward you are.")
    print("")

#Where the game begins
while True:
    print(" ")
    
    if e == None or e.hp <= 0:
        e = Enemy(random.randint(1,5))
        print("A new enemy aproaches with " + str(e.hp) + " hitpoints!")
        print(" ")
        time.sleep(1)
    e.eChooseAttack()
    help()
    
    x = ""
    print("")
    #The player's options. Note that every cooldown has to +1 the wanted cooldown value, since it will no matter what reduce every cooldown with 1.
    while True:
        x = input("What is your aproach:")
        #Strikes the opponent for some damage.
        if x.lower() == "strike":
            dmg = random.randint(1,2)
            e.hp -= dmg
            print("You strike your enemy with " + str(dmg) + " points of damage, leaving the enemy at " + str(e.hp) + " hitpoints!")
            break
        #Dodges an attack completely.
        elif x.lower() == "dodge":
            if p.dodgeCD == 0:
                print("You dodged the enemy, even though he can't attack yet in the current state of this shiz program")
                p.dodgeCD += 2
                break
            print("Your dodge action has to cooldown for " + str(p.dodgeCD) + " turns.")
        #Brings out the list of commands.
        elif x.lower() == "help":
            help()
        #Quits the game. Rename the input later
        elif x.lower() == "giveup" or x.lower() == "g":
            print("COWARD!")
            break
        else:
            print("I do not understand gibberish")
    
    if x.lower() == "giveup":
        break    
    
    e.eCommitAttack()
    
    p.cooldownOptions()

    
    
    #Checks if the enemy is dead
    if e.hp <= 0:
        print("You slayed your foe!")
    time.sleep(2)

