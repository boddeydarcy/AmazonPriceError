import responses
import time
import random

urlDict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F",
           6: "G", 7: "H", 8: "I", 9: "J", 10: "K", 11: "L",
           12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R",
           18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X",
           24: "Y", 25: "Z",
           26: "0", 27: "1", 28: "2", 29: "3", 30: "4", 31: "5",
           32: "6", 33: "7", 34: "8", 35: "9"}

brandList = ["Titleist", "Callaway", "TaylorMade", "Mizuno"]


def createUniqueURL():
    # this is to make sure that the program doesn't get blocked by Amazon
    url = ""
    index = []
    for i in range(2):
        randomIndex = random.randint(0, 12)
        index.append(randomIndex)

    print(index)

    for i in range(13):
        if i in index:
            randomNum = random.randint(0, 35)
            url += urlDict[randomNum].lower()
        else:
            randomNum = random.randint(0, 35)
            url += urlDict[randomNum]
    print(url)


createUniqueURL()