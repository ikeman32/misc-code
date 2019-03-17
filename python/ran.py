import datetime

def random():
    #Variables
    num = 0
    lower = 0
    upper = 0
    seed = .000001 * datetime.datetime.now().microsecond
    
    #Set upper and lower with defaults
    try:
        lower = int(input('Input the lower bound number. Default is 1: '))
    except:
        lower = 1
        
    try:
        upper = int(input('Input the upper bound number. Default is 10: '))
    except:
        upper = 10
    
    #Generate random number  
    num = int(seed * upper) + lower
    
    #Make sure random number does not go out of bounds
    if num > upper:
        num = upper
        print(num)
    elif num < lower:
        num = lower
        print(num)
    else:
        print(num)

random()

