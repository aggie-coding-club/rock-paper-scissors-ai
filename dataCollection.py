import csv

# create a list of tuples with our game data (include game outcome as the third index in the tuple)
# automatically stop after best of 5 is over
def openInputStream():
    string = input("Enter Turn: ")
    list = []
    return list

# saves a list formatted from above into a .csv
# num is the current game number for file naming
def closeInputStream(list, num, location = ""):
    outputFile = open("fileName.csv", 'w')


    outputFile.close()

# saves all games onto the end of allData
# each game ends with an empty line
# num is number of games
def compoundFiles(num):
    mainFile = open("allData.csv", 'a')


    mainFile.close()

#returns 1 if p1 wins, 2 if p1 loses, and 0 if tie
def rpsOutcome(p1, p2):
    return 0



currGame = 0