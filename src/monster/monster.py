class Monster:
    def __init__(self, name:str, level:int, faction:str, cur_hp:int, max_hp:int, base_hp:int, hp_scale:int):
        self.name = name
        self.level = level
        self.faction = faction
        self.cur_hp = cur_hp
        self.max_hp = max_hp
        self.base_hp = base_hp
        self.hp_scale = hp_scale

        if self.max_hp is None:
            adj_level = max(0, self.level - 1)
            self.max_hp = self.base_hp + (adj_level * self.hp_scale)
        if self.cur_hp is None:
            self.cur_hp = self.max_hp