from interface import text_format
from handlers.config import Config as configHandler

class Points:

    def __init__(self, config: configHandler):
        self.config = config
        self.scores = {
            "player": 0,
            "keeper": 0
        }

    # Retrieves the score for the player
    def get_score(self, player):
        return self.scores[player]

    # Adds a score to a player (+1)
    def add_score(self, player):
        self.scores[player] += 1

    # Calculates the winner of the round via the self.scores settings.
    def get_winner(self):
        if self.scores["keeper"] > self.scores["player"]:
            return "keeper", self.scores["keeper"]-self.scores["player"]
        elif self.scores["keeper"] < self.scores["player"]:
            return "player", self.scores["player"]-self.scores["keeper"]
        elif self.scores["keeper"] == self.scores["player"]:
            return "draw", 0

    # Calculates the impossibility (used under notification setting)
    def calculate_impossibility(self):
        result = self.config.retrieve_config("Notifications")
        rounds = int(self.config.retrieve_config("Rounds"))
        if result:
            if (self.scores["keeper"]/2)-int(self.scores["keeper"]/2) == 0:
                if self.scores["keeper"] >= ((rounds/2) + 1):
                    text_format.tip_message("It is now impossible for you to win; the odds are against you!")
            else:
                if self.scores["keeper"] > rounds/2:
                    text_format.tip_message("It is now impossible for you to win; the odds are against you!")
        else:
            return
