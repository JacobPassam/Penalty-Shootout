from handlers import config
from handlers import fileScores
from handlers import scores as temp_scores
from handlers import menu
from interface import textFormat
from interface import menu as menu_interface
import random

PLAYER_OPTIONS = ["left", "centre", "right"]

def get_random_option():
    return PLAYER_OPTIONS[random.randint(0, len(PLAYER_OPTIONS)-1)]

def play():
    config_obj = config.Config()
    config_obj.load_config()

    temp_scores_obj = temp_scores.Scores()

    rounds = int(config_obj.get_config("Rounds")[0])
    notifications = config_obj.get_config("Notifications")[0]
    save_scores = config_obj.get_config("SaveScores")[0]
    sent_notification = False

    for i in range(rounds):
        chosen_option = menu.create_word_menu("GAME", "Choose your option", PLAYER_OPTIONS, False)
        if chosen_option != "menu":
            computer_option = get_random_option()

            if computer_option == chosen_option:
                temp_scores_obj.add_score("keeper_score")
                print("Oh no! The keeper caught the ball.")
            else:
                temp_scores_obj.add_score("player_score")
                print("Well done, you scored!")

            if notifications == "true" and sent_notification == False:
                temp_scores_obj.calculate_impossibility()
                sent_notification = True
        else:
            return

    player_score = temp_scores_obj.get_score("player_score")
    keeper_score = temp_scores_obj.get_score("keeper_score")

    if save_scores == "true":
        result = fileScores.save_scores(player_score, keeper_score)
        if result:
            print("[SAVE] Saved score")
        else:
            print("[SAVE] Error saving score")

    winner, difference = temp_scores_obj.get_winner()
    textFormat.send_separator_message("RESULTS")

    if winner == "keeper":
        print("[END] Oh no! You lost by " + str(difference) + " point(s)!")
    elif winner == "player":
        print("[END] Well done! You won by " + str(difference) + " point(s)!")
    elif winner == "draw":
        print("[END] It was a draw!")

    print("[END] Final Score (Player -> Keeper): \n" + (str(player_score) + " <-> " + str(keeper_score)).center(18))

    menu_interface.send_menu()
