#makes all weapon classes objects and sets the "Weapon" parameter for other weapon objects

class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name
class dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "Its a small knife. Very well made."
        self.damage = 10
        self.value = 20

class lngSword(Weapon):
    def __init__(self):
        self.name = "Long Sword"
        self.description = "A strong and impressive sword"
        self.damage = 15
        self.value = 30

class frSpll(Weapon):
    def __init__(self):
        self.name = "Fire Spell"
        self.description = "A powerful spell that summons fire"
        self.damage = 25
        self.value = 50
        
class stick(Weapon):
    def __init__(self):
        self.name = "Stick"
        self.description = "Well. It's a stick"
        self.damage = 1
        self.value = 1

class rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "Well... It's definitely not a stick"
        self.damage = 5
        self.value = 5
class brknSwrd(Weapon):
    def __init__(self):
        self.name = "Broken Sword"
        self.description = "Its a step up from a rock that's for sure"
        self.damage = 8
        self.value = 16
        
#makes all consumable classes objects and sets "Consumables" parameter

class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} Health)".format(self.name, self.healingValue)


class bread(Consumable):
    def __init__(self):
        self.name = "Hunk of Bread"
        self.description = "A small piece of bread you probably just found"
        self.healingValue = 10
        self.value = 5

class healPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.description = "A vial of red liquid with restorative properties"
        self.healingValue = 30
        self.value = 10

