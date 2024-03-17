from random import randrange                        #Imports randrange function
guess = randrange(9) + 1                            #Generates a random int from 1 to 9
correct = False                                     #Creates a variable for guess truth
if int(input("Guess my number: ")) == guess:        #Checks if user guess is correct
    print("Correct!")                               #Tells the user they're correct if they are
else:
    while correct != True:                          #Repetes following code until user is correct
        if int(input("Guess again: ")) == guess:    #Checks if user's subsequent guesses are correct
            correct = True                          #If guess is correct it sets the value to true
    print("Correct!")                               #Informs the user they're correct