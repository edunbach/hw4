#Q3 sorted.py reverse_sort_dictionary()

def sort_dictionary(dictionary):
    if not isinstance(dictionary, dict):
        raise TypeError("Check that input is in dictionary format {'name': (###-###-####, age),'name': (###-###-####, age), 'name': (###-###-####, age)")

    newList = sorted(dictionary.items(), key=lambda x: x[0], reverse = True)

    result = [(name, data[0]) for name, data in newList]
    return result

