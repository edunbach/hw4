#Q2 merge.py definition merge_list

def merge_list(a, b):
    if not (isinstance(a, list) and isinstance(b, list)):
        raise TypeError("Make sure a and b are in proper list format")
        
    for n in a+b:
        if not isinstance(n, int):
            raise TypeError("Make sure lists only have whole numbers")

    x, y = 0, 0
    combined = []

    combined.extend(a[x:])
    combined.extend(b[y:])
    

    i = 0
    while i < len(combined) - 1:
        if combined[i] > combined[i+1]:
            combined[i], combined[i+1] = combined[i+1], combined[i]
            i = 0
        else:
            i += 1
    return combined 


