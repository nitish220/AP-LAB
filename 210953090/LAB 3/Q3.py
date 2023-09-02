def fun():
    a,b,c,d,e = 1,2,3,4,5
    str = "hi"
print("Total local variables are: ",  fun.__code__.co_nlocals)
