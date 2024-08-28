class Item:
    def __init__(self, name, discription):
        self.name = name
        self.discription = discription
        self.points = points

    def use_item(self,player):
        player.health += self.points
        self.points = 0

