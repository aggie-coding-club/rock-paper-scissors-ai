import csv
from rpsOutcome import*
from inputStream import*
from dataStoring import*


# write code that will on run openInputStream
# save input after each game
# prompt user to stop after each openInputStream
# on stop saveAll



location = input("Enter Date and Location: ")
gameNumber = 1

while(True):
    game = openInputStream()
    save(game, gameNumber, location)
    cont = input("Would you like to continue? ")
    if(cont == 'N' or cont == 'n'): break
    gameNumber += 1
