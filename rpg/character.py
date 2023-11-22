class Character:
    def __init__(self, name:str, strength:int, agility:int, vitality:int):
        self.name = name
        self.stregth = strength
        self.agility = agility
        self.vitality = vitality
        self.HAND_LEFT:int = 0
        self.HAND_RIGHT:int = 0
    
    def attack(self):
        return self.strength
    
    def defend(self, attack:int) -> int:
        pass