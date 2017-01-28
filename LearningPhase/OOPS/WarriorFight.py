import random
import math

class Warrior:
    def __init__(self, name="Warrior", maxHealth=0, maxAttack=0, maxBlock=0):
        self.name = name;
        self.maxAttack = maxAttack
        self.maxHealth = maxHealth
        self.maxBlock = maxBlock

    def attack(self):
        maxAttack = self.maxAttack*(random.random()+ .5)
        return maxAttack

    def block(self):
        maxBlock = self.maxBlock*(random.random()+ .5)
        return maxBlock

class Battle:
    def startBattle(self, warriorA, warriorB):
        while True:
            if self.goAttack(warriorA, warriorB) == "game over":
                print("game over")
                break;

            if self.goAttack(warriorB, warriorA) == "game over":
                print("game over")
                break;

    @staticmethod
    def goAttack(warriorA, warriorB):
        warAattack = warriorA.attack();
        warBblock = warriorB.block()
        warBdamage = math.ceil(warAattack - warBblock)
        warriorB.maxHealth = warriorB.maxHealth - warBdamage
        print("{} attacks {} and gave {} damage.".format(warriorA.name, warriorB.name, warBdamage))
        print("{} is down to {} health.".format(warriorB.name, warriorB.maxHealth))
        if (warriorB.maxHealth <= 0):
            print("{} is victorious and {} is lost".format(warriorA.name, warriorB.name))
            return "game over"

def main():
    maximus = Warrior("maximus", 50, 20, 10)
    galaxin = Warrior("galaxin", 50, 20, 10)
    battle = Battle()
    battle.startBattle(maximus, galaxin)

main()