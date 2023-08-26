def unq(list1):
    list2=[]
    list2=set(list1)
    return list2

list1=[]
x =int(input("Enter the range of the list"))
for i in range(x):
    y =int(input("Enter value"))
    list1.append(y)
print(unq(list1))    
