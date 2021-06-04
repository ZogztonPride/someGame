import random
import time


class Character:
    def __init__(self,maxHp):
        self.maxHp = maxHp
        self.hp = maxHp
        self.lightAttackCD = 0
        self.lightAttackCD = 0
        self.mediumAttackCD = 0
        self.heavyAttackCD = 0
        
    def displayHP(self):
        return str(self.hp) + "/" + str(self.maxHp)
    def cooldownOptions(self):
        if self.lightAttackCD != 0:
            self.lightAttackCD -= 1
        if self.mediumAttackCD != 0:
            self.mediumAttackCD -= 1
        if self.heavyAttackCD != 0:
            self.heavyAttackCD -= 1

class Player(Character):
    def __init__(self,maxHp):
        super().__init__(maxHp)
        self.clashCD = 0
    
    #Displays commands
    def help(self):
        print("Options:")
        print("LightAttack: Deal some minor damage to the enemy. Cooldown: " + str(self.lightAttackCD))
        print("MediumAttack: Deal some medium damage to the enemy. Cooldown: " + str(self.mediumAttackCD))
        print("HeavyAttack: Deal some major damage to the enemy. Cooldown: " + str(self.heavyAttackCD))
        print("Clash: Force a clash with the enemy. Cooldown: " + str(self.clashCD))
        print("Help: Get a list of commands.")
        print("GiveUp: Give up like the coward you are.")
        print("")
    
    def cooldownClass(self):
        if self.clashCD != 0:   
            self.clashCD -= 1
    
    
    
    def chooseAttack(self, x):
            if x.lower() == "lightattack":
                if self.lightAttackCD == 0:
                    print("You try to strike your foe with a quick jab...")
                    self.attack = 0
                    self.lightAttackCD += 0
                    return True
                return False
            elif x.lower() == "mediumattack":
                if self.mediumAttackCD == 0:
                    print("You try to strike your foe with a good punch...")
                    self.attack = 1
                    self.mediumAttackCD += 2
                    return True
                return False
            elif x.lower() == "heavyattack":
                if self.heavyAttackCD == 0:
                    print("You try to hit your foe very hard...")
                    self.attack = 2
                    self.heavyAttackCD += 3
                    return True
                return False
            elif x.lower() == "clash":
                if self.clashCD == 0:
                    print("You try to force a clash with your foe...")
                    self.attack = 3
                    self.clashCD += 3
                    return True
                return False
            else:
                print("Don't talk gibberish.")
                return False
    
    def commitAttack(self):
        #Light attack
        if self.attack == 0:
            return random.randint(1,3)
        #Medium attack
        elif self.attack == 1:
            return random.randint(4,7)
        #Heavy attack 
        elif self.attack == 2:
            return random.randint(8,10)
        #Clash
        elif self.attack == 3:
            return -1
        
        
class Enemy(Character):
    def __init__(self,maxHp):
        super().__init__(maxHp)
    
    def chooseAttack(self):
        while True:
            n = random.randint(0,2)
            if n == 0:
                if self.lightAttackCD == 0:
                    print("The enemy is trying to jab you!")
                    self.attack = 0
                    break
            elif n == 1:
                if self.mediumAttackCD == 0:
                    print("The enemy is trying to strike you!")
                    self.attack = 1
                    self.mediumAttackCD += 2
                    break
            elif n == 2:
                if self.heavyAttackCD == 0:
                    print("The enemy is going for a mighty blow!")
                    self.attack = 2
                    self.heavyAttackCD += 3
                    break
            else:
                continue
    
    def commitAttack(self):
        #Light attack
        if self.attack == 0:
            return random.randint(1,3)
        if self.attack == 1:
            return random.randint(4,7)
        if self.attack == 2:
            return random.randint(8,10)
        
p = Player(10)
e = None    

#Where the game begins
while True:
    print(" ")
    
    if e == None or e.hp <= 0:
        e = Enemy(random.randint(1,5))
        #THESHIZZ!?!??!
        print("A new enemy aproaches with " + e.displayHP() + " hitpoints!")
        print(" ")
        time.sleep(1)
    e.chooseAttack()
    time.sleep(1)
    p.help()
    x = ""
    print("")
    
    while True:
        x = input("What is your aproach:")
        
        #Brings out the list of commands.
        if x.lower() == "help":
            p.help()
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
    if x.lower() == "giveup" or x.lower() == "g":
        break    
    time.sleep(1)
    pA = p.commitAttack()
    eA = e.commitAttack()
    #Checks who is gonna do damage
    if pA == -1:
        pA = eA
        
    if pA > eA:
        e.hp -= pA - eA
        print("You strike your enemy with " + str(pA - eA) + " damage, leaving it with " + e.displayHP() + " hitpoints!")
    elif pA < eA:
        p.hp -= eA - pA
        print("You are struck by your foe with " + str(eA - pA) + " damage, leaving you with " + p.displayHP() + " hitpoints!")
    else:
        print("You clash with the enemy!")
    p.cooldownOptions()
    p.cooldownClass()
    e.cooldownOptions()

    if p.hp <= 0:
        print("You are dead now, and will never return.")
        break
    #Checks if the enemy is dead
    if e.hp <= 0:
        print("You slayed your foe!")
    time.sleep(2)