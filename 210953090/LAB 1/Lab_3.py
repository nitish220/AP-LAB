input_string = input("Enter the  String: \n")

l1 = input_string.split(" ")

odd_length_strings = []
first_last = []

for i in l1:
    if len(i) >= 2:
        if i[0] == i[-1]:
            first_last.append(i)
    if len(i)%2 == 1:
        odd_length_strings.append(i)

print("Number of strings with same first and last letters : " , len(first_last))
print(first_last)
print("\nStrings with odd length", odd_length_strings)
