import random
import time


class Character:
    def __init__(self,maxHp):
        self.maxHp = maxHp
        self.hp = maxHp
        self.attackCD = 0
        self.attack = 0
        
    def displayHP(self):
        w = str(self.hp) + "/" + str(self.maxHp)
        return str(w)

class Player(Character):
    def __init__(self,maxHp):
        super().__init__(maxHp)
        self.dodgeCD = 0
    
    #Displays commands
    def help(self):
        print("Options:")
        print("Strike: Deal some damage to the enemy. Cooldown: " + str(self.attackCD))
        print("Dodge: Dodge an incoming attack. Cooldown: " + str(self.dodgeCD))
        print("Help: Get a list of commands.")
        print("GiveUp: Give up like the coward you are.")
        print("")
    
    def cooldownOptions(self):
        if self.attackCD != 0:
            self.attackCD -= 1
        if self.dodgeCD != 0:   
            self.dodgeCD -= 1
    
    
    
    def chooseAttack(self, x):
            if x.lower() == "strike":
                if self.attackCD == 0:
                    print("You try to strike your foe...")
                    self.attack = 0
                    return True
                return False
            elif x.lower() == "dodge":
                if self.dodgeCD == 0:
                    print("You try to dodge your foe...")
                    self.attack = 1
                    self.dodgeCD += 2
                    return True
                return False
            else:
                print("Don't talk gibberish.")
                return False
    
    def commitAttack(self):
        if self.attack == 0:
            return random.randint(2,4)
        if self.attack == 1:
            return -1
        
        
class Enemy(Character):
    def __init__(self,maxHp):
        super().__init__(maxHp)

    def cooldownOptions(self):
        if self.attackCD != 0:
            self.attackCD -= 1
    
    def chooseAttack(self):
        while True:
            n = random.randint(0,1)
            if n == 0:
                if self.attackCD == 0:
                    print("The enemy is trying to strike you!")
                    self.attack = 0
                    break
            else:
                continue
    
    def commitAttack(self):
        if self.attack == 0:
            return random.randint(2,4)
        
p = Player(10)
e = None    



#Where the game begins
while True:
    print(" ")
    if e == None or e.hp <= 0:
        e = Enemy(random.randint(1,5))
        print("A new enemy aproaches with " + str(e.displayHP) + " hitpoints!")
        print(" ")
        time.sleep(1)
    e.chooseAttack()
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
    if x.lower() == "giveup":
        break    
    
    pA = p.commitAttack
    eA = e.commitAttack
    if pA == -1:
        pA = eA
        
    if pA > eA:
        e.hp -= pA - eA
        print("You strike your enemy with " + str(pA - eA) + "damage, leaving it with " + e.displayHP + " hitpoints!")
    elif pA < eA:
        p.hp -= eA - pA
        print("You are struck by your foe with " + str(eA - pA) + "damage, leaving you with " + p.displayHP + " hitpoints!")
    else:
        print("You clash with the enemy")
    p.cooldownOptions()
    e.cooldownOptions()

    if p.hp <= 0:
        print("You are dead now, and will never return.")
        break
    #Checks if the enemy is dead
    if e.hp <= 0:
        print("You slayed your foe!")
    time.sleep(2)