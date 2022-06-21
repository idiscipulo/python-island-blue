import src.monster as monsters

class Player:
    def __init__(self):
        self.monster_list = [
            monsters.EaterOfFoes(1),
            monsters.Sparrow(1),
            monsters.Shark(3)
        ]

        self.active_monsters = []
        self.update_active_monsters()

    def update_active_monsters(self):
        new_monsters = [x for x in self.monster_list if x.cur_hp > 0][:3]

        if self.active_monsters != new_monsters:
            self.active_monsters = new_monsters
            for monster in self.active_monsters:
                monster.begin()