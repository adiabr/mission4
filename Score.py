from Utils import SCORE_FILE_NAME

def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    score = 0
    try:
        file = open(SCORE_FILE_NAME,"r+")
        score = file.read()
        if not score:
            score = 0
        score = int(score) + points_of_winning
        file.seek(0)
        file.write(str(score))
        file.truncate()
    except FileExistsError as e:
        print(f"Error {e.args}")
        file = open(SCORE_FILE_NAME, "w")
        file.write(str(points_of_winning))
    except FileNotFoundError as e:
        print(f"Error {e.args}")
        file = open(SCORE_FILE_NAME, "w")
        file.write(str(points_of_winning))
    finally:
        if not ERROR and file:
            file.close()