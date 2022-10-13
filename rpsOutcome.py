# Functions to be used for RPS logic and data collection


#returns 1 if p1 wins, 2 if p2 wins, and 0 if tie
def rpsOutcome(p1, p2):
    
    if(p1 is 'r' or  p1 is 'R'):
        if(p2 is 'r' or p2 is 'R'):
            return 0
        elif(p2 is 'p' or p2 is 'P'):
            return 1
        else:
            return 2
        
    elif(p1 is 'p' or  p1 is 'P'):
        if(p2 is 'r' or p2 is 'R'):
            return 1
        elif(p2 is 'p' or p2 is 'P'):
            return 0
        else:
            return 2
        
    else:
        if(p2 is 'r' or p2 is 'R'):
            return 2
        elif(p2 is 'p' or p2 is 'P'):
            return 1
        else:
            return 0