def lic(li):
    s = ""                                          #Declares string to be added to
    for i in li:                                    #Goes through each element of the list
        s += str(li[i])                             #Concatonates each element to the string
    return s                                        #Returns the string

list1 = [0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0]     #Sample list
print(lic(list1))                                   #Prints the result of lic with a list passed to it