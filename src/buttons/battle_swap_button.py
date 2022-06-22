from src.buttons import Button

class BattleSwapButton(Button):
    def draw(self, scr, y:int=0, x:int=0):
        if self.selected:
            self.tick = not self.tick
            if self.tick:
                for i in range(18):
                    scr.addstr(y, x + i, ".")
                    scr.addstr(y + 4, x + i, ".")

                for i in range(4):
                    scr.addstr(y + i, x, ".")
                    scr.addstr(y + i, x + 17, ".")
        
        x += 1
        scr.addstr(y + 1, x,     "■—————————————■")
        scr.addstr(y + 2, x, "|  [S] Swap   |")
        scr.addstr(y + 3, x, "■—————————————■")
