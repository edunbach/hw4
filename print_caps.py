#Q7 print_caps.py create decorator

def allcaps(func):
    def wrapper(): #wrapper inside allcaps as decorator
        result = func() 
        return result.upper() #returns all uppercase of message
    return wrapper
