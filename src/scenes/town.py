class Town:
    def __init__(self):
        pass
 
    def update(self, key):
        if key == ord("q"):
            return "GUN_SHOP"
        elif key == ord("w"):
            return "BATTLE"
        else:
            return None

    def draw(self, scr):
        scr.addstr(1, 2, "press [q] -> Gun Shop")
        scr.addstr(2, 2, "press [w] -> Battle")
        scr.addstr(26, 2, "[Esc] QUIT")