#Asks user for 3 numbers
st = int(input("Please enter a number: "))
nd = int(input("Please enter another number: "))
rd = int(input("Please enter a third: "))

def comp(f,s,t):
    su = f + s + t      #Computes the sum
    if st == nd ==rd:   #Checks if all 3 numbers are equal
        return(3 * su)  #If they are it returns 3x the sum
    else:
        return(su)      #Otherwise it hust returns the sum

print(comp(st,nd,rd))