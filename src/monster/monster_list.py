from src.monster.monster import Monster

class Sparrow(Monster):
    def __init__(self, level:int=1, cur_hp:int=None, max_hp:int=None):
        super().__init__(
            name="SPARROW",
            level=level,
            faction="AIR",
            cur_hp=cur_hp,
            max_hp=max_hp,
            base_hp=10,
            hp_scale=1
        )

class Shark(Monster):
    def __init__(self, level:int=1, cur_hp:int=None, max_hp:int=None):
        super().__init__(
            name="SHARK",
            level=level,
            faction="WATER",
            cur_hp=cur_hp,
            max_hp=max_hp,
            base_hp=12,
            hp_scale=1
        )