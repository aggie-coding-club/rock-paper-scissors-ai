import csv
from turtle import back, width
from rpsOutcome import*
from inputStream import*
from dataStoring import*
import tkinter as tk

p1_move = ""
p2_move = ""

def p1_rock(event):
    global p1_move 
    global btn_p1_rock
    global btn_p1_paper
    global btn_p1_scissors
    
    p1_move = "r"

    btn_p1_rock["foreground"] = "white"
    btn_p1_rock["background"] = "black"
    
    btn_p1_paper["foreground"] = "black"
    btn_p1_paper["background"] = "white"
    
    btn_p1_scissors["foreground"] = "black"
    btn_p1_scissors["background"] = "white"

def p2_rock(event):
    global p2_move 
    global btn_p2_rock
    global btn_p2_paper
    global btn_p2_scissors

    p2_move = "r"
    
    btn_p2_rock["foreground"] = "white"
    btn_p2_rock["background"] = "black"
    
    btn_p2_paper["foreground"] = "black"
    btn_p2_paper["background"] = "white"
    
    btn_p2_scissors["foreground"] = "black"
    btn_p2_scissors["background"] = "white"

def p1_paper(event):
    global p1_move 
    global btn_p1_rock
    global btn_p1_paper
    global btn_p1_scissors

    p1_move = "p"

    btn_p1_rock["foreground"] = "black"
    btn_p1_rock["background"] = "white"
    
    btn_p1_paper["foreground"] = "white"
    btn_p1_paper["background"] = "black"
    
    btn_p1_scissors["foreground"] = "black"
    btn_p1_scissors["background"] = "white"

def p2_paper(event):
    global p2_move 
    global btn_p2_rock
    global btn_p2_paper
    global btn_p2_scissors

    p2_move = "p"
    
    btn_p2_rock["foreground"] = "black"
    btn_p2_rock["background"] = "white"
    
    btn_p2_paper["foreground"] = "white"
    btn_p2_paper["background"] = "black"
    
    btn_p2_scissors["foreground"] = "black"
    btn_p2_scissors["background"] = "white"

def p1_scissors(event):
    global p1_move 
    global btn_p1_rock
    global btn_p1_paper
    global btn_p1_scissors

    p1_move = "s"

    btn_p1_rock["foreground"] = "black"
    btn_p1_rock["background"] = "white"
    
    btn_p1_paper["foreground"] = "black"
    btn_p1_paper["background"] = "white"
    
    btn_p1_scissors["foreground"] = "white"
    btn_p1_scissors["background"] = "black"

def p2_scissors(event):
    global p2_move 
    global btn_p2_rock
    global btn_p2_paper
    global btn_p2_scissors

    p2_move = "s"
    
    btn_p2_rock["foreground"] = "black"
    btn_p2_rock["background"] = "white"
    
    btn_p2_paper["foreground"] = "black"
    btn_p2_paper["background"] = "white"
    
    btn_p2_scissors["foreground"] = "white"
    btn_p2_scissors["background"] = "black"

def inputGo(event):
    global p1_move
    global p2_move
    global btn_p2_rock
    global btn_p2_paper
    global btn_p2_scissors
    global btn_p1_rock
    global btn_p1_paper
    global btn_p1_scissors
    if(p1_move != "" and p2_move != ""):
        

        # DO STUFF

        increaseTurn()

        btn_p1_rock["foreground"] = "black"
        btn_p1_rock["background"] = "white"
        
        btn_p1_paper["foreground"] = "black"
        btn_p1_paper["background"] = "white"
        
        btn_p1_scissors["foreground"] = "black"
        btn_p1_scissors["background"] = "white"

        btn_p2_rock["foreground"] = "black"
        btn_p2_rock["background"] = "white"
        
        btn_p2_paper["foreground"] = "black"
        btn_p2_paper["background"] = "white"
        
        btn_p2_scissors["foreground"] = "black"
        btn_p2_scissors["background"] = "white"

        p1_move = ""
        p2_move = ""

def increaseTurn():
    global lbl_turn_number
    value = int(lbl_turn_number["text"][5:])
    lbl_turn_number["text"] = f"Turn {value + 1}"

window = tk.Tk()

window.rowconfigure([0, 1, 2], minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_p1_rock = tk.Button(master=window, text="Rock", foreground="black", background="white")
btn_p1_rock.bind("<Button-1>", p1_rock)
btn_p1_rock.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)

btn_input = tk.Button(master=window, text="Go!", foreground="black", background="white")
btn_input.bind("<Button-1>", inputGo)
btn_input.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)

btn_p2_rock = tk.Button(master=window, text="Rock", foreground="black", background="white")
btn_p2_rock.bind("<Button-1>", p2_rock)
btn_p2_rock.grid(row=0, column=2, sticky="nsew", padx=15, pady=15)



btn_p1_paper = tk.Button(master=window, text="Paper", foreground="black", background="white")
btn_p1_paper.bind("<Button-1>", p1_paper)
btn_p1_paper.grid(row=1, column=0, sticky="nsew", padx=15, pady=15)

lbl_turn_number = tk.Label(master=window, text="Turn 1")
lbl_turn_number.grid(row=1, column=1)

btn_p2_paper = tk.Button(master=window, text="Paper", foreground="black", background="white")
btn_p2_paper.bind("<Button-1>", p2_paper)
btn_p2_paper.grid(row=1, column=2, sticky="nsew", padx=15, pady=15)



btn_p1_scissors = tk.Button(master=window, text="Scissors", foreground="black", background="white")
btn_p1_scissors.bind("<Button-1>", p1_scissors)
btn_p1_scissors.grid(row=2, column=0, sticky="nsew", padx=15, pady=15)

lbl_value = tk.Label(master=window)
lbl_value.grid(row=2, column=1)

btn_p2_scissors = tk.Button(master=window, text="Scissors", foreground="black", background="white")
btn_p2_scissors.bind("<Button-1>", p2_scissors)
btn_p2_scissors.grid(row=2, column=2, sticky="nsew", padx=15, pady=15)

window.mainloop()