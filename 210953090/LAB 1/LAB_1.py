list1=[1,2,3,4,5,6,7,8,9]
list2=[10,11,12,13,14,15,16,17,18,19]
listnew=[]
x=len(list1)
y=len(list2)
for i in list1:
    if i%2 != 0:
        listnew.append(i)
        
for i in list2:
    if i%2==0:
        listnew.append(i)
        
print(listnew)
        
         
