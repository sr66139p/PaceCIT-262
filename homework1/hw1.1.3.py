name = input("Enter your name:")                #Asks the user for their name
if  (name == "Computer" or name == "computer"): #Checks if the name is computer
    print("Hey, that's my name!")               #Replies with "Hey, that's my name!" if the previous condition is met
else:                                           #Executes the next line if the previous condition isn't met
    print("Hello " + name)                      #Greets the user with their name