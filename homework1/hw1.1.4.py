hours = int(input("Enter Hours:"))                      #Asks the user for the number of hours
rate = int(input("Enter Rate:"))                        #Asks the user for the hourly rate
if (hours>40):                                          #Checks if more than 40 hours were worked
    pay = (40 * rate) + ((hours - 40) * (1.5 * rate))   #Calculates payment with adjusted rate
else:
    pay = hours * rate                                  #Calculates payment with base rate
print("Pay: " + str(pay))                               #Tells the user the calculated pay