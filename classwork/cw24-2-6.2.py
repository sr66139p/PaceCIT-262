numbers = [1,2,3,4,5,6,7,8,9]   #Defines the numbers list

def check():
    for i in numbers:
        if numbers[i] % 2 == 0:
            numbers.pop(i)
    
check()
print(numbers)