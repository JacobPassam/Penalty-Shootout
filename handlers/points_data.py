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


def format_scores(scores):
    sorted_scores = sorted(scores, key=lambda us: us[0], reverse=True)
    return sorted_scores


def save_score(self):
    try:
        file = open('files/points.txt', "a")
        file.write(str(self.scores["player"]) + "," + str(self.scores["keeper"]) + ",\n")
        file.close()
        return True
    except:
        return False