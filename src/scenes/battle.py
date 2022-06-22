import curses

from src.player import Player
from src.buttons import BattleSwapButton
from src.buttons import BattlePotionButton

class Battle:
    def __init__(self, player1:Player, player2:Player):
        self.player1 = player1
        self.player2 = player2

        self.active_monsters = []
        self.cur_monster = None

        self.turn = "PLAYER_1"

        self.swap_button = BattleSwapButton()
        self.potion_button = BattlePotionButton()

        self.color_list = [
            curses.color_pair(1),
            curses.color_pair(2),
            curses.color_pair(3),
            curses.color_pair(4),
            curses.color_pair(5),
            curses.color_pair(6)
        ]
        

    def switch_to(self):
        self.update(None)

    def update(self, key):
        if key == ord(" "):
            self.cur_monster.tu += 200
            self.cur_monster.cur_hp -= 5

        for monster in self.active_monsters:
            if monster.cur_hp <= 0:
                temp_color = monster.color
                self.color_list.append(temp_color)
                monster.color = None

        self.player1.update_active_monsters()
        self.player2.update_active_monsters()

        self.active_monsters = self.player1.active_monsters + self.player2.active_monsters
        self.active_monsters.sort(key=lambda x: x.tu)

        for monster in self.active_monsters:
            if monster.color is None:
                monster.color = self.color_list.pop(0)

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
            x = 6
            y = 15
            for dx, monster in enumerate(self.player1.active_monsters):
                monster.draw_for_battle(scr, y, x + (dx * 28))

        # player2
        x = 27
        y = 2
        for dx, monster in enumerate(self.player2.active_monsters):
            monster.draw_for_battle(scr, y, x + (dx * 28))

        # other options
        x = 92
        y = 16
        self.swap_button.draw(scr, y, x)

        y += 4
        self.potion_button.draw(scr, y, x)

        # tu's
        self.draw_tu(scr, 1, 2)

        # footer
        scr.addstr(26, 2, "[Esc] QUIT")

    def draw_move_box(self, scr, y:int=0, x:int=0):
        scr.addstr(y, x, "———————————————————————————————————————————————————————————————■")
        for dy in range(6):
            scr.addstr(y + dy + 1, x + 63, "|")
        scr.addstr(y + 7, x, "———————————————————————————————————————————————————————————————■")

    def draw_other_option(self, scr, y:int=0, x:int=0):
        self.swap_button.draw(scr, y, x)

        y += 4
        # self.potion_button.draw(scr, y, x)

    def draw_tu(self, scr, y:int=0, x:int=0):
        scr.addstr(y, x, "■——————————————————————■")
        for dy in range(12):
            scr.addstr(y + dy + 1, x, "|                      |")
        scr.addstr(y + dy + 2, x, "■——————————————————————■")

        x += 2
        y += 1
        for dy, monster in enumerate(self.active_monsters):
            monster.draw_tu(scr, y + (dy * 2), x)

            # scr.addstr(y + 1 + (dy * 2), x + 2, f"[{monster.tu:>3}] {monster.name:<14}")
            # monster.draw_health_bar(scr, y + 2 + (dy * 2), x + 5)