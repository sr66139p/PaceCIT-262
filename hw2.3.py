#         ________________________________________________
#________|                                               |_______
#\       |     Advanced Coding in Python CIT -262        |      /
# \      |                                               |     /
# /      |_______________________________________________|     \
#/__________)                                        (__________\

color_list = ["Red","Green","White" ,"Black"]                                   #Creates a list of colors

def fl(li):                                                                     #Creates a new function that expects one list
    print("The first color is: " + li[0] +", and the last color is: " + li[-1]) #Prints the list elements

fl(color_list)                                                                  #Passes the earlier list to the function