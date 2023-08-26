def mul(list1,n):
    result=1
    for i in list1:
        result=result*i
    return result
    
x =int(input("Enter the range of the list"))
list1=[]
for i in range(x):
    y =int(input("Enter value"))
    list1.append(y)
    
print(mul(list1,x))
