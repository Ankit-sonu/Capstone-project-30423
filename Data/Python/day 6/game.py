class Character:
    def __init__(self, name): self.name = name

class Hero(Character):
    def ability(self): return "Heal"

class Villain(Character):
    def ability(self): return "Destroy"

class NPC(Character):
    def ability(self): return "Help"

h = Hero("Leo")
v = Villain("Max")
n = NPC("Bob")
print(h.ability(), v.ability(), n.ability())
