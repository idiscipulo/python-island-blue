from ..player import Player

class Battle:
    def __init__(self, player1:Player, player2:Player):
        self.player1 = player1
        self.player2 = player2
        
    def update(self, key):
        self.player1.update_active_monsters()
        
        if key == ord("q"):
            return "GUN_SHOP"
        elif key == ord("w"):
            return "BATTLE"
        else:
            return None

    def draw(self, scr):
        # player1
        for y, monster in enumerate(self.player1.active_monsters):
            screen_name = monster.name[:20]
            screen_hp = f"{monster.cur_hp:>3}/{monster.max_hp:>3}"
            screen_faction = monster.faction

            scr.addstr(0, (y * 26), "+——————————————————————+") 
            scr.addstr(1, (y * 26), f"| {screen_name:^20} |")
            scr.addstr(2, (y * 26), "+——————————————————————+")
            scr.addstr(3, (y * 26), f"| HP : {screen_hp:^15} |")
            scr.addstr(4, (y * 26), f"+———————[{screen_faction:^5}]————————+")


        # footer
        scr.addstr("\n[Esc] QUIT")