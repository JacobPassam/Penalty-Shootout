from handlers import points_data
from interface import text_format
from handlers import menu


OPTIONS = ["descending", "ascending"]


def send():
    # Selection menu on how they want the scores listed.
    response = menu.create_int_menu("SCORES DATA: How do you want to view the data?", OPTIONS, True)
    if not response: return

    selected_choice = OPTIONS[response-1]

    # Sends sorted scores.
    sorted_scores = points_data.retrieve_scores(selected_choice)

    text_format.send_separator_message("SCORES DATA")
    print("Listed in " + selected_choice + " order.")
    print("PLAYER <--> KEEPER")

    # Prints out in format PLAYER SCORE <-> KEEPER SCORE.
    for i in range(len(sorted_scores)):
        print((sorted_scores[i][0] + " <-> " + sorted_scores[i][1]).center(18))
    return
