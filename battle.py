class Monster:
    def __init__(self, name:str="", tags:list=[], cur_hp:int="", max_hp:int=""):
        self.name = name
        self.tags = tags
        self.cur_hp = cur_hp
        self.max_hp = max_hp

    def from_string(self, data:str):
        data_split = data.split("|")
        name = data_split[0]
        tags = data_split[1]
        tags = tags.split(",")
        cur_hp = int(data_split[2])
        max_hp = int(data_split[3])

        self.__init__(name, tags, cur_hp, max_hp)

        return self

class Player:
    def __init__(self):
        self.monster_list = [
            Monster().from_string("Test1|TYPE_EARTH|10|10"),
            Monster().from_string("Test2|TYPE_FIRE|10|10"),
            Monster().from_string("Test3|TYPE_WATER|10|10")
        ]

        self.active_monsters = [x for x in self.monster_list if x.cur_hp > 0][:3]

    def update_active_monsters(self):
        self.active_monsters = [x for x in self.monster_list if x.cur_hp > 0][:3]

class Battle:
    def __init__(self):
        self.player1 = Player()
        
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

            screen_tag = [x.replace("TYPE_", "") for x in monster.tags if "TYPE_" in x][0]

            scr.addstr(0, (y * 26), "+——————————————————————+") 
            scr.addstr(1, (y * 26), f"| {screen_name:^20} |")
            scr.addstr(2, (y * 26), "+——————————————————————+")
            scr.addstr(3, (y * 26), f"| HP : {screen_hp:^15} |")
            scr.addstr(4, (y * 26), f"+———————[{screen_tag:^5}]————————+")


        # footer
        scr.addstr("\n[Esc] QUIT")