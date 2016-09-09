import items
import world


class Player:
    def __init__(self):
        self.inventory = [items.stick(),                       
                          items.bread(),
                          items.rock()
                          ]
#This says where the player starts (in space)
        self.x = 1
        self.y = 2
        self.health = 100  #This is the players health
        self.victory = False  #This is how you win
        self.gold = 20

    def isAlive(self):
        return self.health > 0

#This prints the inventory
    def printInventory(self):
        print("Inventory: ")
        for item in self.inventory:
            print('* ' + str(item))
        

#This tells the user whether they can heal or not
    def heal(self):
        consumables = [item for item in self.inventory
                       if isinstance(item, items.Consumable)]
        if not consumables:
            print("You dont have any healing items")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose an item to heal your wounds: ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                toEat = consumables[int(choice) - 1]
                self.health = max(100, self.health + toEat.healingValue)
                self.inventory.remove(toEat)
                print("Current Health: {}".format(self.health))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try another")
                

#This picks which weapon in the inventory is the strongest
    def strongest(self):
        maxDamage = 0
        bestWeapon = None
        for item in self.inventory:
            try:
                if item.damage > maxDamage:
                    bestWeapon = item
                    maxDamage = item.damage
            except AttributeError:
                pass

        return bestWeapon

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
#Allows player to move North, South, East, or West
    def moveNorth(self):
        self.move(dx=0, dy=-1)

    def moveSouth(self):
        self.move(dx=0, dy=1)

    def moveEast(self):
        self.move(dx=1, dy=0)

    def moveWest(self):
        self.move(dx=-1, dy=0)


#action that enables a player to attack
    def attack(self):
        bestWeapon = self.strongest()
        room = world.tileAt(self.x, self.y)
        enemy = room.enemy
        print("You use your {} to hit the {}.".format(bestWeapon.name, enemy.name))
        enemy.health -= bestWeapon.damage
#Determines whether to diplay enemies current health or their defeat
        if not enemy.isAlive():
            print("You defeated the {}!".format(enemy.name))
        else:
            print("The {} has {} health remaining".format(enemy.name, enemy.health))

    def trade(self):
        room = world.tileAt(self.x, self.y)
        room.checkifTrade(self)
