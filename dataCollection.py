import csv

# create a list of tuples with our game data (include game outcome as the third index in the tuple)
# automatically stop after best of 5 is over
def openInputStream():
    string = input("Enter Turn: ")
    list = []

    return list

# saves a list formatted from above into a .csv
# num is the current game number for file naming
def save(list, num, location = ""):
    outputFile = open("fileName.csv", 'w')


    outputFile.close()

# saves all games onto the end of allData
# each game ends with an empty line
# each game starts with the file name it came from without the csv alone on a line
# num is number of games
def saveAll(num):
    mainFile = open("allData.csv", 'a')


    mainFile.close()

# delete specific RPS game from mainData
def delete(num, location):
    return False

# delete all files up in location
def deleteFiles(num, location):
    return False

#returns 1 if p1 wins, 2 if p2 wins, and 0 if tie
def rpsOutcome(p1, p2):
    return 0


# write code that will on run openInputStream
# save input after each game
# prompt user to stop after each openInputStream
# on stop saveAll
# after saving to main file, delete extra csv files created
