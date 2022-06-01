import json

def generate_monster_list_from_metadata(src:str, dest:str):
    with open(src, "rb") as file:
        data = json.load(file)

    with open(dest, "w+") as file:
        file.write("from src.monster.monster import Monster")

        for monster in data["monsters"]:
            file.write(f"""\n\nclass {monster['name'].capitalize()}(Monster):
    def __init__(self, level:int=1, cur_hp:int=None, max_hp:int=None):
        super().__init__(
            name="{monster['name'].upper()}",
            level=level,
            faction="{monster['faction']}",
            cur_hp=cur_hp,
            max_hp=max_hp,
            base_hp={monster['base_hp']},
            hp_scale={monster['hp_scale']}
        )""")

if __name__ == "__main__":
    generate_monster_list_from_metadata(
        src="include/monster_list.json",
        dest="src/monster/monster_list.py"
    )