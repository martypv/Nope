import random
import enemies
import player
import npc


class mapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def introText(self):
        raise NotImplementedError("Create a subclass instead")

    def modifyPlayer(self, player):
        pass


class startTile(mapTile):
    def introText(self):
        return """
    You awake in a dark dank cave. There are multiple paths that you can take.
                            The decision is yours.
        """

class traderTile(mapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

#Exchanges gold value for item and swaps it to opposite inventory
    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            userInput = input("Choose an item or press Q to exit: ")
            if userInput in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(userInput)
                    toSwap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, toSwap)
                except ValueError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("You dont have enough Gold!")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    def checkifTrade(self, player):
        while True:
            print("Would you like to Buy(B), Sell(S), or Quit(Q)?")
            userInput = input()
            if userInput in ['Q', 'q']:
                return
            elif userInput in ['B', 'b']:
                print("Here's what's available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif userInput in ['S', 's']:
                print("Here's what's available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def introText(self):
        return """
        There's a small, frail, old man curled up into a ball in the corner.
        When he sees you he looks excited and displays his many wares
        """

class findgoldTile(mapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.goldClaimed = False
        super().__init__(x,y)

    def modifyPlayer(self, player):
        if not self.goldClaimed:
            self.goldClaimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def introText(self):
        if self.goldClaimed:
            return """
            This part of the cave is now empty
            """
        else:
            return """
            You found some Gold!
            """

class emptyTile(mapTile):
    def introText(self):
        return """
        This part of the cave is empty. There is nothing of interest.
        """


class victoryTile(mapTile):
    def modifyPlayer(self, player):
        player.victory = True
        
    def introText(self):
        return """
        You win!
        """
    
class enemyTile(mapTile):
    def __init__(self, x, y):
        rate = random.random()
        if rate < 0.60:
            self.enemy = enemies.goblin()
            self.aliveText = '''
            A Goblin slinks towards you
            '''
            self.deadText = '''
            A Goblin corpse lays at your feet
            '''
        elif rate < 0.80:
            self.enemy = enemies.skeleton()
            self.aliveText = '''
            A Skeleton shambles toward you
            '''
            self.deadText = '''
            A pile of shattered bones lay at your feet
            '''
        else:
            self.enemy = enemies.wizard()
            self.aliveText = '''
            In a puff of etherial smoke, a mighty Wizard appears!
            '''
            self.deadText = '''
            You freeze the Wizard... He shatters
            '''

        super().__init__(x, y)

    def introText(self):
        text = self.aliveText if self.enemy.isAlive() else self.deadText
        return text

    def modifyPlayer(self, player):
        if self.enemy.isAlive():  #if the enemy is alive it will deal its damage to the players health
            player.health = player.health - self.enemy.damage
            print("The enemy hits you for {}. You have {} health remaining!".
                  format(self.enemy.damage, player.health))

#this is the world map. it works like a grid
worldMap = [
    [None,findgoldTile(1,0),None,victoryTile(3,0),None],
    [None,enemyTile(1,1),None,findgoldTile(3,1),enemyTile(4,1)],
    [enemyTile(0,2),startTile(1,2),traderTile(2,2),enemyTile(3,2),None],
    [None,enemyTile(1,3),None,enemyTile(3,3),None],
    [None,emptyTile(1,4),enemyTile(2,4),emptyTile(3,4),None],
    [None,enemyTile(1,5),None,emptyTile(3,5),enemyTile(4,5)],
    [enemyTile(0,6),emptyTile(1,6),None,enemyTile(3,6),None]
]

def tileAt(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return worldMap[y][x]
    except IndexError:
        return None
