import curses
from time import time, sleep

from town import Town
from battle import Battle

def main(scr):
    curses.curs_set(False)
    scr.nodelay(True)

    cur_state = "TOWN"
    states = {
        "TOWN": Town(),
        "BATTLE": Battle()
    }

    while True:
        s_time = time()

        scr.clear()

        key = scr.getch()
        if key == 27:
            break
        
        change = states[cur_state].update(key)
        if change is not None:
            cur_state = change

        states[cur_state].draw(scr)

        scr.refresh()

        delay = max(0, 0.2 - (time() - s_time))
        sleep(delay)
 
if __name__ == "__main__":
    curses.wrapper(main)