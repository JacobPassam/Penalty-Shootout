from handlers import config
from interface import textFormat


class Scores:

    def __init__(self):
        self.scores = {
            "player_score": 0,
            "keeper_score": 0
        }

    # Adds to a users score
    def add_score(self, user):
        self.scores[user] += 1

    # Retrieves the score of a user.
    def get_score(self, user):
        return self.scores[user]

    # Calculates the winner of the round via the self.scores settings.
    def get_winner(self):
        if self.scores["keeper_score"] > self.scores["player_score"]:
            return "keeper", self.scores["keeper_score"]-self.scores["player_score"]
        elif self.scores["keeper_score"] < self.scores["player_score"]:
            return "player", self.scores["player_score"]-self.scores["keeper_score"]
        elif self.scores["keeper_score"] == self.scores["player_score"]:
            return "draw", 0

    # Calculates the impossibility (used under notification setting)
    def calculate_impossibility(self):
        config_obj = config.Config()
        config_obj.load_config()
        result = config_obj.get_config("Notifications")[0]
        rounds = int(config_obj.get_config("Rounds")[0])
        if result == "true":
            if (self.scores["keeper_score"]/2)-int(self.scores["keeper_score"]/2) == 0:
                if self.scores["keeper_score"] >= ((rounds/2) + 1):
                    textFormat.tip_message("It is now impossible for you to win; the odds are against you!")
            else:
                if self.scores["keeper_score"] > rounds/2:
                    textFormat.tip_message("It is now impossible for you to win; the odds are against you!")
        else:
            return
