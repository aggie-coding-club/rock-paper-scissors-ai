import csv
from token import NUMBER
import os

# saves a list formatted from above into the main .csv
# num is the current game number for file naming
# each game ends with an empty line
# each game starts with the file name it came from without the csv alone on a line
def save(list, num, location = ""):
    with open('allRPSData.csv', 'a', newline='', encoding='utf-8') as outputFile:
        outputCSV = csv.writer(outputFile)
        outputCSV.writerow([f'{location}_Game_{num}'])
        outputCSV.writerows(list)
        outputCSV.writerow('')
        outputFile.close()

# delete specific RPS game from mainData
# mark as deleted by replacing the header line with DELETED_ + whatever the old header was
def deleteGame(num, location):
    RPSdata = open("allRPSData.csv", 'r', newline='', encoding='utf-8')
    tempFile = open('allRPSDataTemp.csv', 'w', newline='', encoding='utf-8')
    RPSreader = csv.reader(RPSdata, delimiter=',')
    RPSwriter = csv.writer(tempFile, delimiter=',')
    
    for row in RPSreader:
        
        if len(row) != 0 and row[0] == f'{location}_Game_{num}':
            row[0] = "DELETED_" + row[0]
        RPSwriter.writerow(row)
        
    RPSdata.close()
    tempFile.close()
    os.remove("allRPSData.csv")
    os.rename("allRPSDataTemp.csv", "allRPSData.csv")

    
