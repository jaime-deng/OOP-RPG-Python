import random
    
# def badguy(mobType,equipment):
#     badguy=mobType
#     weapon=equipment
#     hp=90
#     ac=random.randrange(40,55)
#     return [badguy,weapon,hp,ac]
    
    # Sorry Boss! I ran out of time and couldn't implement the fight method!
    # -----------Add it here ----------

class mob:
    def __init__(self,badguy, weapon, hp, ac):
        self.badguy= badguy
        self.weapon=weapon
        self.hp= hp
        self.ac= ac

    def fight(self):
        print(f"You take a swing at the {self.badguy}")
        hitAmount = random.randrange(40,55)
        ac = random.randrange(40,55)
        #print (hitAmount)
        if hitAmount > ac:
            print(f"You hit the {self.badguy} for {hitAmount} damage!")
            newHP = self.hp - hitAmount 
            #print (newHP)
            self.hp = newHP
        else:
            print("You missed")
    


# foe=badguy("troll","great axe")
mob = mob("troll", "great axe", 90, random.randrange(40,55))
print(f"You meet a {mob.badguy} wielding a {mob.weapon}")
print("Type the a key and then RETURN to attack.")


    
while True:
    action=input()
    
    if action.lower() == "a":
        mob.fight()
    
    if (mob.hp) < 1:
        print("You killed your foe!")
    else:
        print("The " + mob.badguy + " has " + str(mob.hp) + " HP remaining")



