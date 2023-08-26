def uppercase(x):
    list1=x.split(" ")
    str=""
    for i in range(len(list1)):
        str=str+list1[i][0].upper()+list1[i][1:]+" "
    return str
    
