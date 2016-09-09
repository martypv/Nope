#Makes enemy class an object

class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects")

    def __str__(self):
        return self.name

    def isAlive(self):
        return self.health > 0

class goblin(Enemy):
    def __init__(self):
        self.name = "Goblin"
        self.health = 10
        self.damage = 2

class skeleton(Enemy):
    def __init__(self):
        self.name = "Skeleton"
        self.health = 20
        self.damage = 4

class wizard(Enemy):
    def __init__(self):
        self.name = "Wizard"
        self.health = 40
        self.damage = 15
