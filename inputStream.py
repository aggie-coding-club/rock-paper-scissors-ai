from rpsOutcome import*

# create a list of tuples with our game data (include game outcome as the third index in the tuple)
# automatically stop after best of 5 is over
def openInputStream():
    list = []
    p1wins = 0
    p2wins = 0
    
    while (p1wins < 3 and p2wins < 3):
        
        # Asking user to enter their input, and splitting into two lowercase strings
        string = input("Enter Turn: ")
        strs = string.split(" ")
        str1 = strs[0].lower()
        str2 = strs[1].lower()


        # Checking if first string is invalid, then turning it into lowercase r, p , and s
        if (str1 == "rock"):
            str1 = "r"
        elif (str1 == "paper"):
            str1 = "p"
        elif (str1 == "scissors"):
            str1 = "s"
        elif (str1 != "r" and str1 != "p" and str1 != "s"):
            print("Retry Input")
            continue

        # Checking if second string is invalid, then turning it into lowercase r, p , and s
        if (str2 == "rock"):
            str2 = "r"
        elif (str2 == "paper"):
            str2 = "p"
        elif (str2 == "scissors"):
            str2 = "s"
        elif (str2 != "r" and str2 != "p" and str2 != "s"):
            print("Invalid input, Retry input")
            continue




        #Creating tuple of match, and adding it to the main list
        
        win = rpsOutcome(str1, str2)
        
        match = (str1, str2, win)
        if (win == 1):
            p1wins += 1
        elif (win == 2):
            p2wins += 1
        list.append(match)
    return list
