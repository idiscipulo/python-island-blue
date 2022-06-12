import json

def generate_monster_list_from_json(src:str, dest:str):
    with open(src, "rb") as file:
        data = json.load(file)

    with open(dest, "w+") as file:
        file.write("from src.monster.monster import Monster")

        data["monsters"].sort(key=lambda x: x["name"])

        for monster in data["monsters"]:
            name_split = monster["name"].split(" ")
            CLASS_NAME = "".join([x.capitalize() for x in name_split])
            NAME = monster["name"].upper()
            FACTION = monster["faction"]
            BASE_HP = monster["base_hp"]
            HP_SCALE = monster["hp_scale"]

            file.write(f"""\n\nclass {CLASS_NAME}(Monster):
    def __init__(self, level:int=1, cur_hp:int=None):
        super().__init__(
            name="{NAME}",
            level=level,
            faction="{FACTION}",
            cur_hp=cur_hp,
            base_hp={BASE_HP}
        )""")

if __name__ == "__main__":
    generate_monster_list_from_json(
        src="include/monster_list.json",
        dest="src/monster/monster_list.py"
    )