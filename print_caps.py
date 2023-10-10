#Q7 print_caps.py create decorator

def allcaps(func):
    def wrapper():
        result = func()
        if result:
            return result.upper()
        else:
            return result  # Return the original result if it's an empty string or None
    return wrapper
