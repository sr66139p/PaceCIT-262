import time                                                             #Imports time library

def countdown(i):                                                       #Defines a new function
    print(i)                                                            #Prints where we are in the countdown
    time.sleep(1)                                                       #Pauses for 1 second
    if (i>1):                                                           #Checks if the countdown is done
        countdown(i-1)                                                  #Runs countdown function again if it isn't done

countdown(int(input("Please enter an integer to count down from: ")))   #Asks user for input and passes it to countdown as an int