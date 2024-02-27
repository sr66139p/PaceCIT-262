n1 = int(input("Enter a number:"))                                      #Asks the user for a number
n2 = int(input("Enter another number:"))                                #Asks the user for another number

if (n1==n2):                                                            #Checks if the numbers are the same
    print("Numbers match!")                                             #Tells the user if the numbers are the same
elif (n1+n1>10):                                                        #Checks if the numbers add up to a number greater than 10
    print("These numbers add up to a number that is greater than 10.")  #Tells the user if the check is true
else:
    print("Sum: " + str(n1+n2))                                         #Tells the user the sum of the numbers