from src.monster.monster import Monster

class EaterOfFoes(Monster):
    def __init__(self, level:int=1, cur_hp:int=None):
        super().__init__(
            name="EATER OF FOES",
            level=level,
            faction="DEMON",
            cur_hp=cur_hp,
            base_hp=46
        )

class Shark(Monster):
    def __init__(self, level:int=1, cur_hp:int=None):
        super().__init__(
            name="SHARK",
            level=level,
            faction="WATER",
            cur_hp=cur_hp,
            base_hp=12
        )

class Sparrow(Monster):
    def __init__(self, level:int=1, cur_hp:int=None):
        super().__init__(
            name="SPARROW",
            level=level,
            faction="AIR",
            cur_hp=cur_hp,
            base_hp=10
        )