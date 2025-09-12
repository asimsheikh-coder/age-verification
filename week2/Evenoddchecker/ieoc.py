number = int(input("Enter a number:")) #5
number = number+1 #6
for i in range(number): #0-5
    # print(i, number)
    if i % 2 == 0: #6 divide by 2, if remainder is 0
        print ("The given number is Even", i)
    else:
        print ("The number is odd", i)