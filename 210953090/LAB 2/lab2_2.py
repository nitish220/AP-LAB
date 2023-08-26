list1 = []
list2 = []
for i in range(2):
    x = int(input("Enter 'i' = "))
    list1.append(x)
for i in range(2):
    x = int(input("Enter 'i' = "))
    list2.append(x)

print(list1)
print(list2)
m = {1: list1, 2: list2}
print(m)

list3 = []
list4 = []
for i in range(2):
    x = int(input("Enter 'i' = "))
    list3.append(x)
for i in range(2):
    x = int(input("Enter 'i' = "))
    list4.append(x)
print(list3)
print(list4)
x = {1: list3, 2: list4}
print(x)

result = {}

for i in range(1, 3):  # Start the loop from 1 to 2
    for j in range(2):
        print(m[i][j] + x[i][j], end='\t')
    print(end="\n")
