from ..player import Player

class Battle:
    def __init__(self, player1:Player, player2:Player):
        self.player1 = player1
        self.player2 = player2

        self.active_monsters = []
        self.cur_monster = None

        self.turn = "PLAYER_1"
    
    def switch_to(self):
        self.update(None)

    def update(self, key):
        if key == ord(" "):
            self.active_monsters[0].tu += 200

        self.player1.update_active_monsters()
        self.player2.update_active_monsters()

        self.active_monsters = self.player1.active_monsters + self.player2.active_monsters
        self.active_monsters.sort(key=lambda x: x.tu)

        self.cur_monster = self.active_monsters[0]

        val = self.cur_monster.tu
        for i in range(len(self.active_monsters)):
            self.active_monsters[i].tu -= val
            self.active_monsters[i].selected = False

        if self.cur_monster in self.player1.active_monsters:
            self.turn = "PLAYER_1"
        else:
            self.cur_monster.selected = True
            self.turn = "PLAYER_2"

    def draw(self, scr):
        if self.turn == "PLAYER_1":
            self.cur_monster.draw_for_battle(scr, 15, 2)

            self.draw_move_box(scr, 16, 27)

        elif self.turn == "PLAYER_2":
            # draw player1
            x = 2
            y = 15
            for dx, monster in enumerate(self.player1.active_monsters):
                monster.draw_for_battle(scr, y, x + (dx * 28))

        # player2
        x = 27
        y = 2
        for dx, monster in enumerate(self.player2.active_monsters):
            monster.draw_for_battle(scr, y, x + (dx * 28))

        # other option
        self.draw_other_option(scr, 16, 70)

        # tu's
        self.draw_tu(scr, 1, 2)

        # footer
        scr.addstr(26, 2, "[Esc] QUIT")

    def draw_move_box(self, scr, y:int=0, x:int=0):
        scr.addstr(y, x, "————————————————————————————————————————————————————————————————————————————————■")
        for dy in range(6):
            scr.addstr(y + dy + 1, x + 80, "|")
        scr.addstr(y + 7, x, "————————————————————————————————————————————————————————————————————————————————■")

    def draw_other_option(scr, y:int=0, x:int=0):
        scr.addstr(y, x,     "■—————————————■")
        scr.addstr(y + 1, x, "|  [S] Swap   |")
        scr.addstr(y, x,     "■—————————————■")


    def draw_tu(self, scr, y:int=0, x:int=0):
        scr.addstr(y, x, "■——————————————————————■")
        for dy in range(12):
            scr.addstr(y + dy + 1, x, "|                      |")
        scr.addstr(y + dy + 2, x, "■——————————————————————■")

        for dy, monster in enumerate(self.active_monsters):
            scr.addstr(y + 1 + (dy * 2), x + 2, f"[{monster.tu:>3}] {monster.name:<14}")
            monster.draw_health_bar(scr, y + 2 + (dy * 2), x + 5)