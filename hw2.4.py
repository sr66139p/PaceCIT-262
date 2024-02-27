#         ________________________________________________
#________|                                               |_______
#\       |     Advanced Coding in Python CIT -262        |      /
# \      |                                               |     /
# /      |_______________________________________________|     \
#/__________)                                        (__________\

def difference(n):#.................................Creates new funtion difference
    if n>17:#.......................................Checks if n is greater than n
        print(2*(n-17))#............................Prints twice the positive difference
    else:
        print(17-n)#................................Prints the difference

difference(int(input("Please enter a number: ")))#..Asks user for input and passes it to difference