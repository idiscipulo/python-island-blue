from ..player import Player

class Battle:
    def __init__(self, player1:Player, player2:Player):
        self.player1 = player1
        self.player2 = player2

        self.active_monsters = []
        
    def update(self, key):
        self.player1.update_active_monsters()
        self.player2.update_active_monsters()

        self.active_monsters = self.player1.active_monsters + self.player2.active_monsters

        if key == ord("q"):
            return "GUN_SHOP"
        elif key == ord("w"):
            return "BATTLE"
        else:
            return None

    def draw(self, scr):
        # player1
        x = 2
        y = 15
        self.draw_player1_monster_zone(scr, y, x)

        x += 2
        y += 1
        self.draw_monster_slots(scr, y, x)

        for dx, monster in enumerate(self.player1.active_monsters):
            monster.draw_for_battle(scr, y, x + (dx * 26))

        # player2
        x = 29
        y = 2
        self.draw_monster_slots(scr, y, x)

        for dx, monster in enumerate(self.player2.active_monsters):
            monster.draw_for_battle(scr, y, x + (dx * 26))

        # tu's
        self.draw_tu(scr, 1, 2)

    def draw_tu(self, scr, y:int=0, x:int=0):
        scr.addstr(y, x, "+——————————————————————+")
        for dy in range(12):
            scr.addstr(y + dy + 1, x, "|                      |")
        scr.addstr(y + dy + 2, x, "+——————————————————————+")

        for dy, monster in enumerate(self.active_monsters):
            scr.addstr(y + 1 + (dy * 2), x + 2, f"[{monster.tu:>3}] {monster.name:<14}")
            monster.draw_health_bar(scr, y + 2 + (dy * 2), x + 5)

        # footer
        scr.addstr(26, 2, "[Esc] QUIT")
        
    def draw_player1_monster_zone(self, scr, y:int=0, x:int=0):
        scr.addstr(y, x,      "+——————————————————————————————————————————————————————————————————————————————+") 
        scr.addstr(y + 1, x, f"|                                                                              |")
        scr.addstr(y + 2, x, f"|                                                                              |")
        scr.addstr(y + 3, x, f"|                                                                              |")
        scr.addstr(y + 4, x, f"|                                                                              |")
        scr.addstr(y + 5, x, f"|                                                                              |")
        scr.addstr(y + 6, x, f"+——————————————————————————————————————————————————————————————————————————————+")

    def draw_monster_slots(self, scr, y:int=0, x:int=0):
        for dx in range(3):
            act_x = x + (dx * 26)
            scr.addstr(y, act_x,      "+— — — — — — — — — — — + ") 
            scr.addstr(y + 1, act_x, f"|                      |")
            scr.addstr(y + 2, act_x, f"|                      |")
            scr.addstr(y + 3, act_x, f"|                      |")
            scr.addstr(y + 4, act_x, f"+— — — — — — — — — — — + ")