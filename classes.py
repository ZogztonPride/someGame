import random
import time


class Character:
    def __init__(self,maxHp):
        self.maxHp = maxHp
        self.hp = maxHp
        self.attack = 0
        self.lightAttackCD = 0
        self.mediumAttackCD = 0
        self.heavyAttackCD = 0
        self.specialCooldown = 0
        
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
    def __init__(self,maxHp,type,superDesc):
        super().__init__(maxHp)
        self.type = type
        self.superDesc = superDesc
        self.clashCD = 0
    def help(self, special):
        print("Options:")
        print("LightAttack: Deal some minor damage to the enemy. Cooldown: " + str(self.lightAttackCD))
        print("MediumAttack: Deal some medium damage to the enemy. Cooldown: " + str(self.mediumAttackCD))
        print("HeavyAttack: Deal some major damage to the enemy. Cooldown: " + str(self.heavyAttackCD))
        print("Clash: Force a clash with the enemy. Cooldown: " + str(self.clashCD))
        print(special)
        print("Hp: Display your current health.")
        print("EnemyHp: Display your enemy's current hp.")
        print("Help: Get a list of commands.")
        print("GiveUp: Give up like the coward you are.")
        print("")
    
class TestCharacter(Player):
    def __init__(self):
        super().__init__(10, "testCharacter")
    
    def cooldownClass(self):
        if self.clashCD != 0:   
            self.clashCD -= 1
    
    #Displays commands
    

    def chooseAttack(self, x):
            if x.lower() == "lightattack":
                if self.lightAttackCD == 0:
                    print("You try to strike your foe with a quick jab...")
                    self.attack = 0
                    self.lightAttackCD += 0
                    return True
            elif x.lower() == "mediumattack":
                if self.mediumAttackCD == 0:
                    print("You try to strike your foe with a good punch...")
                    self.attack = 1
                    self.mediumAttackCD += 3
                    return True
            elif x.lower() == "heavyattack":
                if self.heavyAttackCD == 0:
                    print("You try to hit your foe very hard...")
                    self.attack = 2
                    self.heavyAttackCD += 4
                    return True
            elif x.lower() == "clash":
                if self.clashCD == 0:
                    print("You try to force a clash with your foe...")
                    self.attack = 3
                    self.clashCD += 4
                    return True
            else:
                print("Don't talk gibberish.")

class Fencer(Player):
    def __init__(self):
        super().__init__(8, "fencer","Riposte: Dodge the attack and strike an equal blow. specialCooldown: " + str(self.specialCooldown))
    
    def chaHelp(self):
        help(self.superDesc)
    
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
            elif x.lower() == "mediumattack":
                if self.mediumAttackCD == 0:
                    print("You try to strike your foe with a good punch...")
                    self.attack = 1
                    self.mediumAttackCD += 3
                    return True
            elif x.lower() == "heavyattack":
                if self.heavyAttackCD == 0:
                    print("You try to hit your foe very hard...")
                    self.attack = 2
                    self.heavyAttackCD += 4
                    return True
            elif x.lower() == "clash":
                if self.clashCD == 0:
                    print("You try to force a clash with your foe...")
                    self.attack = 3
                    self.clashCD += 4
                    return True
            elif x.lower() == "riposte":
                if self.specialCooldown == 0:
                    print("You prepare to riposte your enemy's next attack...")
                    self.attack = 4
                    self.specialCooldown += 3
                    return True
            else:
                print("Don't talk gibberish.")

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
        #Riposte(Fencer special)
        elif self.attack == 4:
            return -2
        
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