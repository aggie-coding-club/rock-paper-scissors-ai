import csv
from token import NUMBER

# saves a list formatted from above into the main .csv
# num is the current game number for file naming
# each game ends with an empty line
# each game starts with the file name it came from without the csv alone on a line
def save(list, num, location = ""):
    with open('allRPSData.csv', 'a') as outputFile:
        outputCSV = csv.writer(outputFile)
        outputCSV.writerow([f'{location}_Game_{num}'])
        
        
        outputCSV.writerows(list)

        outputCSV.writerow('')

    



        outputFile.close()

# delete specific RPS game from mainData
# mark as deleted by replacing the header line with DELETED_ + whatever the old header was
def delete(num, location):
    outputFile = open("allRPSData.csv", 'r+')
    deleteCSVthing = csv.reader(outputFile)
    writeCVS = csv.writer(outputFile)
    
    for row in deleteCSVthing:
        print(row)
        if row == [f'{location}_Game{num}']:
            row = 'DELETED_' + location + '_Game{}'.format(num)
            writeCVS.writerow([row])

    
    

    outputFile.close()
    
