import csv
from turtle import width
from rpsOutcome import*
from inputStream import*
from dataStoring import*
import tkinter as tk


# write code that will on run openInputStream
# save input after each game
# prompt user to stop after each openInputStream
# on stop saveAll





location = "STOP" # input("Enter Date and Location: ")
gameNumber = 1
cont = 'y'
if(location == 'STOP'):
    cont = 'n'

while(not(cont == 'N' or cont == 'n' or cont == "No" or cont == "no")):
    game = openInputStream()
    save(game, gameNumber, location)
    cont = input("Would you like to continue? ")
    while(cont == "DELETE"): 
        deleteGame(int(input("Which game number? ")), location)
        cont = input("Would you like to continue? ")
    gameNumber += 1
