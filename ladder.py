#Q1 ladder.py steps function

def my_steps(x):
    if x < 1 or x > 25:
        raise ValueError("The input must be an ingteger between 1 and 25")
    
        output = [0] * (x+1)

        output[1] = 1
        output[2] = 2

        for i in range (3, x+1):
            output[i] = output[i-1] + output[i-2]

        return output[x]


