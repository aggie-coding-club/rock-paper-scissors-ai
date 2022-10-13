import csv
from token import NUMBER

# saves a list formatted from above into the main .csv
# num is the current game number for file naming
# each game ends with an empty line
# each game starts with the file name it came from without the csv alone on a line
def save(list, num, location = ""):
    with open('fileName.csv', 'a') as outputFile:
        outputCSV = csv.writer(outputFile)
        outputCSV.writerow([location + ' Game {}'.format(num)])
        
        
        outputCSV.writerows(list)

        outputCSV.writerow('')

    



        outputFile.close()

# delete specific RPS game from mainData
# mark as deleted by replacing the header line with DELETED_ + whatever the old header was
def delete(num, location):
    outputFile = open("fileName.csv", 'r+')
    deleteCSVthing = csv.reader(outputFile)
    writeCVS = csv.writer(outputFile)
    
    for row in deleteCSVthing:
        print(row)
        if row == [location + ' Game{}'.format(num)]:
            row = 'DELETED_' + location + ' Game{}'.format(num)
            writeCVS.writerow([row])

    
    

    outputFile.close()
    

u = [('r', 'p', 'p'), ('r', 'p', 'p'), ('r', 'p', 'p')]
save(u, 2, location='cry')

delete(1, 'dev')