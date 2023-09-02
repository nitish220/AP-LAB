n = input("Enter Number: ")
armstrong = 0

for digit in n:
    armstrong += int(digit) **3
    
if(armstrong == int(n)):
    print(" Armstrong Number!")
else:
    print("Not an Armstrong Number!")
