import csv
from turtle import back, width
from rpsOutcome import*
from inputStream import*
from dataStoring import*
import tkinter as tk

p1_move = ""
p2_move = ""
turns = []
p1wins = 0
p2wins = 0
num = 1

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
        enterTurn()

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

def resetTurn():
    global btn_p1_paper
    global btn_p2_paper
    global btn_p1_rock
    global btn_p2_rock
    global btn_p1_scissors
    global btn_p2_scissors
    global btn_input
    global lbl_turn_number
    global text_continue
    global btn_yes
    global btn_no
    
    btn_p1_paper.grid_forget()
    btn_p2_paper.grid_forget()
    btn_p1_rock.grid_forget()
    btn_p2_rock.grid_forget()
    btn_p1_scissors.grid_forget()
    btn_p2_scissors.grid_forget()
    btn_input.grid_forget()
    lbl_turn_number.grid_forget()
    

    text_continue = tk.Label(text="Would you like to continue?", font= 25)
    text_continue.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)
    btn_yes = tk.Button(text="Yes",font= 25, foreground="black", background="white")
    btn_yes.bind("<Button-1>", openRPSinput)
    btn_yes.grid(row=1, column=0, sticky="nsew", padx=15, pady=15)
    btn_no = tk.Button(text="No", font= 25, foreground="black", background="white")
    btn_no.bind("<Button-1>", closeWindow)
    btn_no.grid(row=1, column=2, sticky="nsew", padx=15, pady=15)




def enterTurn():
    global turns
    global p1wins
    global p2wins
    global p1_move
    global p2_move
    global num
    global str_location
        
        
    win = rpsOutcome(p1_move, p2_move)
    
    match = (p1_move, p2_move, win)
    if (win == 1):
        p1wins += 1
    elif (win == 2):
        p2wins += 1
    turns.append(match)

    if(p1wins >= 3 or p2wins >= 3):
        save(turns, num, str_location)
        num += 1
        turns = []
        p1wins = 0
        p2wins = 0
        resetTurn()
    else:
        increaseTurn()
    
def openRPSinput(event):
    global window
    global btn_p1_paper
    global btn_p2_paper
    global btn_p1_rock
    global btn_p2_rock
    global btn_p1_scissors
    global btn_p2_scissors
    global btn_input
    global lbl_turn_number

    global entry_location
    global btn_location
    global lbl_location_txt
    global str_location
    
    global btn_yes
    global btn_no
    global text_continue
    try:
        str_location = entry_location.get()
        btn_location.grid_remove()
        entry_location.grid_remove()
        lbl_location_txt.grid_remove()
    except:
        1
    try:
        btn_yes.grid_remove()
        btn_no.grid_remove()
        text_continue.grid_remove()
    except:
        1

    btn_p1_rock = tk.Button(master=window, text="Rock", foreground="black", background="white", font= 25)
    btn_p1_rock.bind("<Button-1>", p1_rock)
    btn_p1_rock.grid(row=0, column=0, sticky="nsew", padx=15, pady=15)

    btn_input = tk.Button(master=window, text="Go!", foreground="black", background="white", font= 25)
    btn_input.bind("<Button-1>", inputGo)
    btn_input.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)

    btn_p2_rock = tk.Button(master=window, text="Rock", foreground="black", background="white", font= 25)
    btn_p2_rock.bind("<Button-1>", p2_rock)
    btn_p2_rock.grid(row=0, column=2, sticky="nsew", padx=15, pady=15)



    btn_p1_paper = tk.Button(master=window, text="Paper", foreground="black", background="white", font= 25)
    btn_p1_paper.bind("<Button-1>", p1_paper)
    btn_p1_paper.grid(row=1, column=0, sticky="nsew", padx=15, pady=15)

    lbl_turn_number = tk.Label(master=window, text="Turn 1", font= 25)
    lbl_turn_number.grid(row=1, column=1)

    btn_p2_paper = tk.Button(master=window, text="Paper", foreground="black", background="white", font= 25)
    btn_p2_paper.bind("<Button-1>", p2_paper)
    btn_p2_paper.grid(row=1, column=2, sticky="nsew", padx=15, pady=15)



    btn_p1_scissors = tk.Button(master=window, text="Scissors", foreground="black", background="white", font= 25)
    btn_p1_scissors.bind("<Button-1>", p1_scissors)
    btn_p1_scissors.grid(row=2, column=0, sticky="nsew", padx=15, pady=15)

    lbl_value = tk.Label(master=window)
    lbl_value.grid(row=2, column=1)

    btn_p2_scissors = tk.Button(master=window, text="Scissors", foreground="black", background="white", font= 25)
    btn_p2_scissors.bind("<Button-1>", p2_scissors)
    btn_p2_scissors.grid(row=2, column=2, sticky="nsew", padx=15, pady=15)

def closeWindow(event):
    window.destroy()

window = tk.Tk()

window.rowconfigure([0, 1, 2], minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

lbl_location_txt = tk.Label(text="Enter Location:", font= 25)
lbl_location_txt.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)
entry_location = tk.Entry(font= 25, foreground="black", background="white")
entry_location.grid(row=1, column=1, sticky="nsew", padx=15, pady=15)
btn_location = tk.Button(text="Enter", font= 25, foreground="black", background="white")
btn_location.bind("<Button-1>", openRPSinput)
btn_location.grid(row=1, column=2, sticky="nsew", padx=15, pady=15)

window.mainloop()