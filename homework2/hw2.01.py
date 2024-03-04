#              ,---------------------------,
#              |  /---------------------\  |
#              | |                       | |
#              | |    Advanced Coding    | |
#              | |       in Python       | |
#              | |        CIT-262        | |
#              | |                       | |
#              |  \_____________________/  |
#              |___________________________|
#            ,---\_____     []     _______/------,
#          /         /______________\           /|
#        /___________________________________ /  | ___
#        |                                   |   |    )
#        |  _ _ _                 [-------]  |   |   (
#        |  o o o                 [-------]  |  /    _)_
#        |__________________________________ |/     / / /
#    /-------------------------------------/|      (___/
#  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def name(f, l):                      #Creates function called name that has two name inputs  
    print(l + " " + f)               #Prints the inputs in reverse order with a space in between

name(str(input("Please enter your first name: ")), str(input("Please enter your last name: "))) #Asks user for name and passes it to name()