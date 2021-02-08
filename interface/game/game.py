from handlers import config
from handlers import fileScores
from handlers import scores as temp_scores
from handlers import menu
from handlers import config as configHandler
from interface import textFormat
import random

PLAYER_OPTIONS = ["left", "centre", "right"]


# Generates random option in PLAYER_OPTIONS
def get_random_option():
    return PLAYER_OPTIONS[random.randint(0, len(PLAYER_OPTIONS) - 1)]


# Activates the game
def play(config_obj: configHandler):
    # Temp score ready
    temp_scores_obj = temp_scores.Scores()

    # Sets configuration options as variables.
    rounds = int(config_obj.get_config("Rounds")[0])
    save_scores = config_obj.get_config("SaveScores")[0]

    # Loops through each round
    for i in range(rounds):
        # Creates option menu
        chosen_option = menu.create_word_menu("GAME", "Choose your option", PLAYER_OPTIONS, False)
        if chosen_option != "menu":
            computer_option = get_random_option()
            # Prints out who won
            if computer_option == chosen_option:
                temp_scores_obj.add_score("keeper_score")
                print("Oh no! The keeper caught the ball.")
            else:
                temp_scores_obj.add_score("player_score")
                print("Well done, you scored!")

            # Sends impossibility notification
            temp_scores_obj.calculate_impossibility(config_obj)
        else:
            return

    player_score = temp_scores_obj.get_score("player_score")
    keeper_score = temp_scores_obj.get_score("keeper_score")

    # Saves the score if set to do so
    if save_scores == "true":
        result = fileScores.save_scores(player_score, keeper_score)
        if result:
            print("[SAVE] Saved score")
        else:
            print("[SAVE] Error saving score")

    winner, difference = temp_scores_obj.get_winner()
    textFormat.send_separator_message("RESULTS")

    # Shows the overall winner
    if winner == "keeper":
        print("[END] Oh no! You lost by " + str(difference) + " point(s)!")
    elif winner == "player":
        print("[END] Well done! You won by " + str(difference) + " point(s)!")
    elif winner == "draw":
        print("[END] It was a draw!")

    print("[END] Final Score (Player -> Keeper): \n" + (str(player_score) + " <-> " + str(keeper_score)).center(18))

    # Returns back to menu
    return
