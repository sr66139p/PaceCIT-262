num = [1,2,3,4,5,6,7,8,9]           #defines list of numbers

def parity(li):                     #defines function that has 1 parameter
    liodd = []                      #creates a list to hold odd numbers
    i = -1                          #creates a number to keep track of position
    while i +1 < len(li):           #checks each element of the list
        i += 1                      #counts up by one
        if (li[i] % 2 == 1):        #checks if the number is odd
            liodd.append(li[i])     #if it is odd, adds it to the new list
    return(liodd)                   #returns the list

print(parity(num))                  #prints the returned list