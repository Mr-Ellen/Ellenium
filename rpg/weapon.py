class Weapon:
    def __init__(self, name:str, attack:int, defense:int):
        self.name = name
        self.attack = attack
        self.defense = defense
    
    def __str__(self) -> str:
        return f"{self.name} [{self.attack}/{self.defense}]"
    
    @property.getter
    def attack(self) -> int:
        return self.attack
    
    @property.getter
    def defense(self) -> int:
        return self.defense