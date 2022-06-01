from cards.card import Card

def option_go_around():
    return "You succesfully go around this test."

class Card_Test(Card):
    def __init__(self):
        super().__init__(
            name = "Test Card",
            text = "A card to test out the structure and dynamic functions."
        )

        self.options = [
            {
                "text": "go around",
                "func": option_go_around
            }
        ]