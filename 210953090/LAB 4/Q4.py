import time
x=input("Enter your name :")
if int(time.strftime("%H")) < 12:
    print("Good Morning ",x)
if int(time.strftime("%H")) > 12 and  int(time.strftime("%H")) < 18 :
    print("Good Evenig ",x)
if int(time.strftime("%H")) > 18 and  int(time.strftime("%H")) < 24 :
    print("Good Night ",x)