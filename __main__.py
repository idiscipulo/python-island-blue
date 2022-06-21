import curses
import sys
from time import time, sleep

from src.scenes import Town
from src.scenes import Battle

from src.player import Player

def draw_border(scr):
    width = 112
    height = 28

    scr.addstr(0, 0, f"■——————————————————————————————————————————————————————————————————————————————————————————————————————————————■")
    for y in range(height - 1):
        scr.addstr(y + 1, 0, f"|{'':110}|")
    scr.addstr(25, 0, f"■——————————————————————————————————————————————————————————————————————————————————————————————————————————————■")
    scr.addstr(27, 0, f"■——————————————————————————————————————————————————————————————————————————————————————————————————————————————■")

def main(scr):
    curses.curs_set(False)
    scr.nodelay(True)

    cur_state = "TOWN"
    states = {
        "TOWN": Town(),
        "BATTLE": Battle(
            player1=Player(),
            player2=Player()
        )
    }

    while True:
        s_time = time()

        scr.clear()

        draw_border(scr)

        key = scr.getch()
        if key == 27:
            break
        
        change = states[cur_state].update(key)
        if change is not None:
            cur_state = change
            states[cur_state].switch_to()

        states[cur_state].draw(scr)

        scr.refresh()

        delay = max(0, 0.12 - (time() - s_time))
        sleep(delay)
 
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "dev":
            print("[INFO] Generating new monster_list from source")

            from dev_tools.monster_factory import generate_monster_list_from_json
            generate_monster_list_from_json(
                src="include/monster_list.json",
                dest="src/monster/monster_list.py"
            )

    print("[INFO] Starting game...")
    curses.wrapper(main)

    print("[INFO] Game exited succesfully...")