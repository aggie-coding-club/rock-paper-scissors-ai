# Functions to be used for RPS logic and data collection


#returns 1 if p1 wins, 2 if p2 wins, and 0 if tie
def rpsOutcome(p1, p2):
    
    if(p1 == 'r'):
        if(p2 == 'r'):
            return 0
        elif(p2 == 'p'):
            return 2
        else:
            return 1
        
    elif(p1 == 'p'):
        if(p2 == 'r'):
            return 1
        elif(p2 == 'p'):
            return 0
        else:
            return 2
        
    else:
        if(p2 == 'r'):
            return 2
        elif(p2 == 'p'):
            return 1
        else:
            return 0