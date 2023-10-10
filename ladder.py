#Q1 ladder.py steps function

def my_steps(x):
    if x < 1 or x > 25:
        raise ValueError("The input must be an ingteger between 1 and 25")
    
    output = [0] * (x+1)

    if x == 1:
        output[1] = 1

    if x == 2:
        output[2] = 2
    elif:
        for i in range (1, x+1):
            output[i] = output[i-1] + output[i-2]
        
        
    return output[x]

