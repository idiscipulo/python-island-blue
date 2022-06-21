class MonsterToken:
    def __init__(self, monster):
        self.monster = monster
        self.tu = 30
        self.hover = False

    def set_monster(self, monster):
        self.monster = monster

    def draw_health_bar(self, scr, y:int=0, x:int=0):
        hp_scale = self.monster.cur_hp / self.monster.max_hp
        hp_bar_len = max(1, int(hp_scale * 15))
        hp_str = f"{self.monster.cur_hp:>3}/{self.monster.max_hp:>3}"

        scr.addstr(y, x, "□□□□□□□□□□□□□□□")
        scr.addstr(y, x, f"{'':■<{hp_bar_len}}")
        scr.addstr(y, x + 3, f" {hp_str} ")

    def draw(self, scr, y:int=0, x:int=0):
        name_str = self.monster.name[:20]
        faction_str = self.monster.faction

        scr.addstr(y, x, "■——————————————————————■") 
        scr.addstr(y + 1, x, f"| {name_str:^20} |")
        scr.addstr(y + 2, x, "■——————————————————————■")
        scr.addstr(y + 3, x, f"| HP :                 |")
        self.draw_health_bar(scr, y + 3, x + 7)
        scr.addstr(y + 4, x, f"■———————[{faction_str:^5}]————————■")