from handlers import fileScores
from interface import textFormat
from interface import menu

# Sends the scores that have been sorted in a nice formatted way.
def send():
    sorted_scores = fileScores.retrieve_scores()

    textFormat.send_separator_message("SCORES DATA")
    print("Listed from your highest to lowest score")
    print("PLAYER <--> KEEPER")

    for i in range(len(sorted_scores)):
        print((sorted_scores[i][0] + " <-> " + sorted_scores[i][1]).center(18))

    menu.send_menu()
    return