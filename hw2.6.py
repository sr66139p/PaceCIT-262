def li4(li):
    c = 0                                           #Declares variable to keep track of number of 4s
    for i in li:                                    #Goes through each element of the list
        if li[i] == 4:                              #Checks if the elemet is a 4
            c += 1                                  #If 4 is found, adds 1 to the count
    return c                                        #Returns the number of 4s counted

list1 = [0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0]
print(li4(list1))                                   #Prints the result of li4 with a list passed to it