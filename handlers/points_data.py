# Retrieves all the formatted scores. and appends to an array.
def retrieve_scores():
    file = open('files/points.txt', "r")
    finished = False

    scores = []

    while not finished:
        line = file.readline()
        if not line == "":
            split = line.split(",")
            scores.append([split[0], split[1]])
        else:
            finished = True

    sorted_scores = format_scores(scores)

    return sorted_scores


# Returns formatted scores via lambda.
def format_scores(scores):
    sorted_scores = sorted(scores, key=lambda us: us[0], reverse=True)
    return sorted_scores


# Saves a score set to the file.
def save_score(player_score, keeper_score):
    try:
        file = open('files/points.txt', "a")
        file.write(str(player_score) + "," + str(keeper_score) + ",\n")
        file.close()
        return True
    except:
        return False