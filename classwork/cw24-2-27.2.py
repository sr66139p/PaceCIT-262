def fizzbuzz():
    x = 0                                   #Declares variable to start counting from       
    while x <= 50:                          #Repetes inside code until we pass 50
        x += 1                              #Counts up by 1
        if (x % 3 == 0) and (x % 5 == 0):   #Checks if the current number is a factor of 3 and 5
            print("fizzbuzz")
        elif (x % 3 == 0):                  #Checks if the current number is a factor of 3
            print("fizz")
        elif (x % 5 == 0):                  #Checks if the current number is a factor of 5
            print("buzz")
        else:
            print(x)

fizzbuzz()