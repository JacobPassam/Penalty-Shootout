from handlers import config
from interface import textFormat


class Scores:

    def __init__(self):
        self.player_score = 0
        self.keeper_score = 0

    # Adds to a users score
    def add_score(self, user):
        self[user] += 1

    # Retrieves the score of a user.
    def get_score(self, user):
        return self[user]

    # Calculates the impossibility (used under notification setting)
    def __calculate_impossibility(self):
        config_obj = config.Config()
        config_obj.load_config()
        result = config_obj.get_config("notifications")
        rounds = int(config_obj.get_config("rounds"))
        if result == "true":
            if (self.keeper_score/2)-int(self.keeper_score/2) == 0:
                if self.keeper_score >= ((rounds/2) + 1):
                    textFormat.tip_message("It is now impossible for you to win; the odds are against you!")
            else:
                if self.keeper_score > rounds/2:
                    textFormat.tip_message("It is now impossible for you to win; the odds are against you!")
        else:
            return
