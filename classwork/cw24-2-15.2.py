def factorial(i):                                                       #Defines factorial function     
    j = int(i)                                                          #Sets j equal to i
    i -= 1                                                              #i  counts down by 1
    if (i>=1):                                                          #Checks if base case was reached
        j *= factorial(i)                                               #Multiplies j by factorial of itself -1
    return j                                                            #reurns the factorial

print(factorial(int(input("Please enter an integer to factorial: "))))  #Prints results of user int factorial