# Don't delete any of the given code.

def scoresIncreasing(scoresList):
  # insert your logic here
    correct=False
    for x in range(len(scoresList)-1):
        if scoresList[x+1]>=scoresList[x]:
            correct=True
        else:
            return False
    return correct
