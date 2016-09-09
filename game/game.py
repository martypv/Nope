from collections import OrderedDict
from player import Player
import world

def play():
    print("Cave Adventure!")
    player = Player()
    while player.isAlive() and not player.victory:
        room = world.tileAt(player.x, player.y)
        print(room.introText())
        room.modifyPlayer(player)
        chooseAction(room, player)


def chooseAction(room, player):
    action = None
    while not action:
        availableActions = getavailableActions(room, player)
        actionInput = input("Action: ")
        action = availableActions.get(actionInput)
        if action:
            action()
        else:
            print("Invalid action")


def getavailableActions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if player.inventory:
        actionAdder(actions, 'i', player.printInventory, "Inventory")
    if isinstance (room, world.traderTile):
        actionAdder(actions, 't', player.trade, "Trade")
    if isinstance (room, world.enemyTile) and room.enemy.isAlive():
        actionAdder(actions, 'a', player.attack, "Attack")
    else:
        if world.tileAt(room.x, room.y - 1):
            actionAdder(actions, 'n', player.moveNorth, "Go North")
        if world.tileAt(room.x, room.y + 1):
            actionAdder(actions, 's', player.moveSouth, "Go South")
        if world.tileAt(room.x + 1, room.y):
            actionAdder(actions, 'e', player.moveEast, "Go East")
        if world.tileAt(room.x - 1, room.y):
            actionAdder(actions, 'w', player.moveWest, "Go West")
    if player.health < 100:
        actionAdder(actions, 'h', player.heal, "Heal")

    return actions

def actionAdder(actionDict, hotkey, action, name):
    actionDict[hotkey.lower()] = action
    actionDict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))



play()
