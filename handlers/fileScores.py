# Retrieves the scores via the points file
def retrieveScores():
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

    sorted_scores = formatScores(scores)

    return sorted_scores

# Sorts the scores via lambda
def formatScores(scores):
    sorted_scores = sorted(scores, key=lambda us: us[0], reverse=True)

    return sorted_scores
