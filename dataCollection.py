import csv
from rpsOutcome import*
from inputStream import*
from dataStoring import*
import tkinter as tk


# write code that will on run openInputStream
# save input after each game
# prompt user to stop after each openInputStream
# on stop saveAll



window = tk.Tk()
greeting = tk.Label(text="Rock Paper Scissors!")
greeting.pack()
window.mainloop()


location = input("Enter Date and Location: ")
gameNumber = 1
cont = 'y'
while(not(cont == 'N' or cont == 'n' or cont == "No" or cont == "no")):
    game = openInputStream()
    save(game, gameNumber, location)
    cont = input("Would you like to continue? ")
    while(cont == "DELETE"): 
        deleteGame(int(input("Which game number? ")), location)
        cont = input("Would you like to continue? ")
    if(cont == 'N' or cont == 'n' or cont == "No" or cont == "no"): break
    gameNumber += 1
