import items



class nonplayerCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")


    def __str__(self):
        return self.name




class Trader(nonplayerCharacter):
    def __init__(self):
        self.name = "Shoppekeep"
        self.gold = 1000
        self.inventory = [items.frSpll(),
                          items.lngSword(),
                          items.dagger(),
                          items.brknSwrd(),
                          items.healPotion(),
                          items.healPotion(),
                          items.bread(),
                          items.bread(),
                          items.bread()]
        
