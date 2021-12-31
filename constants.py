__isDebug = False

if __isDebug:
    url = "http://localhost:8000"
else:
    url = "https://find-matches.herokuapp.com"
    
__level = 0
def getLevel():
    global __level
    return __level

def setLevel(l):
    global __level
    __level = l


def getScore():
    f = open("currentScore.txt", "r")
    score = f.read()
    f.close()
    return int(score)

def setScore(l):
    f = open("currentScore.txt", "w")
    f.write(f"{str(l)}")
    f.close()
