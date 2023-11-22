class Character:
    def __init__(self, name:str, strength:int, agility:int, vitality:int):
        self.name = name
        self.stregth = strength
        self.agility = agility
        self.vitality = vitality
        self.HAND_LEFT:int = 2
        self.HAND_RIGHT:int = 1
    
    def attack(self):
        return self.strength
    
    def defend(self, attack:int) -> int:
        pass

    def is_alive(self) -> bool:
        if self.vitality > 0:
            return True
        else:
            return False
    
    def take_weapon(self, weapon:Weapon|None, hand:int) -> bool:
        pass

    def __str__(self) -> str:
        return f"{self.name} [{self.vitality}] ({}/{})"