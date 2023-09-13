def union(set_1, set_2):
    set_final = set_1 | set_2
    return set_final

def intersection(set_1, set_2):
    set_final = set_1 & set_2
    return set_final

def diference(set_1, set_2):
    set_final = set_1 - set_2
    return set_final

def void_word(element_1,element_2):
    if(element_1=="#" and element_2=="#"):
        return "#"
    elif(element_1=="#" and element_2!="#"):
        return element_2
    elif(element_1!="#" and element_2=="#"):
        return element_1
    else:
        return element_1+element_2