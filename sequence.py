n = int(input("Enter the length of the sequence: ")) # Do not change this line


a = 1
b = 0
c = 0
d = 0

for i in range (n):
        #Since the sequence always starts with the integer 1, so we're printing 1 here and making the a variable into a 2.
    if a == 1:
        print(a)
        b = a
        a = b + b
        #Since the sequence always has the integer 2 in the second place, we're printing 2 here and making the a variable into a 3 by making the b and c variables into 2 and 1 respectively.
    elif a == 2:
        print(a)
        c = b
        b = a
        a = b + c
    else:
        print(a)
        d = c
        c = b
        b = a
        a = b + c + d
