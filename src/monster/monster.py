class Monster:
    def __init__(self, name:str, level:int, faction:str, cur_hp:int, base_hp:int,):
        self.name = name
        self.level = level
        self.faction = faction
        self.cur_hp = cur_hp
        self.base_hp = base_hp

        self.max_hp = max(1,(level * base_hp))

        if self.cur_hp is None:
            self.cur_hp = self.max_hp

        self.tu = 0

    def begin(self):
        self.tu = 30
        
    def draw_for_battle(self, scr, y:int=0, x:int=0):
        name_str = self.name[:20]
        faction_str = self.faction

        scr.addstr(y, x, "+——————————————————————+") 
        scr.addstr(y + 1, x, f"| {name_str:^20} |")
        scr.addstr(y + 2, x, "+——————————————————————+")
        scr.addstr(y + 3, x, f"| HP :                 |")
        self.draw_health_bar(scr, y + 3, x + 7)
        scr.addstr(y + 4, x, f"+———————[{faction_str:^5}]————————+")

    def draw_health_bar(self, scr, y:int=0, x:int=0):
        hp_scale = self.cur_hp / self.max_hp
        hp_bar_len = max(1, int(hp_scale * 15))
        hp_str = f"{self.cur_hp:>3}/{self.max_hp:>3}"

        scr.addstr(y, x, "□□□□□□□□□□□□□□□")
        scr.addstr(y, x, f"{'':■<{hp_bar_len}}")
        scr.addstr(y, x + 3, f" {hp_str} ")

      