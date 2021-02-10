from handlers.config import Config as configHandler
from handlers.points import Points
from handlers import points_data
from handlers import menu
from interface import text_format
import random

OPTIONS = ["left", "centre", "right"]


def generate_keeper_option():
    return OPTIONS[random.randint(0, len(OPTIONS) - 1)]


def play(config):
    # Retrieves configuration values
    rounds = config.retrieve_config("Rounds")
    save_scores = config.retrieve_config("SaveScores")

    # Prints out welcome message
    print("Welcome to the game! Please make sure you've read the instructions so you know what to do.")

    # Starts points client
    points_client = Points(config)

    # Loops through each round.
    for i in range(int(rounds)):
        # Display messages
        response = menu.create_string_menu("GAME - ROUND: " + (str(i + 1)), OPTIONS, False)
        keeper_option = generate_keeper_option()

        # Prints out winner response for the certain round and adds score to winner.
        if response == keeper_option:
            print("The keeper caught the ball - you failed.")
            points_client.add_score("keeper")
        else:
            print("Well done, you scored!")
            points_client.add_score("player")

        # Calculates game impossibility (only sends if enabled notifications)
        points_client.calculate_impossibility()

    # Retrieves winner and difference score.
    winner, difference_score = points_client.get_winner()

    text_format.send_separator_message("OVERALL RESULTS")
    # Displays difference and who lost/won.
    if winner == "keeper":
        print("Oh no! You've lost by " + str(difference_score) + " point(s)!")
    elif winner == "player":
        print("Well done! You've won by " + str(difference_score) + " point(s)!")
    else:
        print("Congratulations, it was a draw!")
    print("FINAL RESULTS: (Player -> Keeper)\n" + (str(points_client.get_score("player")) + " <-> " +
                                                   str(points_client.get_score("keeper"))).center(18))
    # Saves the scores if enabled.
    if save_scores:
        points_data.save_score(points_client.get_score('player'), points_client.get_score('keeper'))
    return
