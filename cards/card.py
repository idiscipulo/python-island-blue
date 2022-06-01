class Card:
    def __init__(self, name:str, text:str):
        self.name = name
        self.text = text
        self.options = []
        self.result = ""

        self.state = "OPTION" # RESULT

    def update(self, key):
        option_keys = ["q", "w", "e"]

        if self.state == "OPTION":
            for ind, val in enumerate(self.options):
                if key == ord(option_keys[ind]):
                    self.result = val["result"]
                    self.state = "RESULT"

    def draw(self, scr):
        # name
        scr.addstr(0, 0, self.name)
        scr.addstr(1, 0, "-----")
        
        if self.state == "OPTION":
            # text
            text_len = 30
            text_list = []
            t_text = self.text
            while len(t_text) > text_len:
                split_ind = t_text.find(" ", text_len)
                text_list.append(t_text[:split_ind])
                t_text = t_text[split_ind + 1:]
            text_list.append(t_text)

            for ind, val in enumerate(text_list):
                scr.addstr(2 + ind, 0, val)

            scr.addstr(3 + ind, 0, "-----")

            # options
            option_keys = ["q", "w", "e"]
            for ind, val in enumerate(self.options):
                scr.addstr(5 + ind, 0, f"press [{option_keys[ind]}] -> {val['text']}")

        elif self.state == "RESULT":
            scr.addstr(2, 0, self.result)

