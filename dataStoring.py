import csv

# saves a list formatted from above into the main .csv
# num is the current game number for file naming
# each game ends with an empty line
# each game starts with the file name it came from without the csv alone on a line
def save(list, num, location = ""):
    outputFile = open("fileName.csv", 'a')


    outputFile.close()

# delete specific RPS game from mainData
# mark as deleted by replacing the header line with DELETED_ + whatever the old header was
def delete(num, location):
    outputFile = open("fileName.csv", 'a')


    outputFile.close()
    return False


