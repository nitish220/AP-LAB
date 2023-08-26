def low(x):
    low=0
    for i in x:
        if i.islower():
            low=low+1
    return low

def high(x):
    high=0
    for i in x:
        if i.isupper():
            high=high+1
    return high


x=input("String :")
print("Lower Case :",low(x))
print("Upper Case:",high(x))
