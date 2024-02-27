vowels = "aeiouAEIOU"                           #Lists all English Vowels 

def isvowel(x):
    if x in vowels:                             #Checks if the input strinng matches any of the vowels
        print(str(x) + " is a vowel.")          #If it does, it tells you
    else:
        print(str(x) + " is not a vowel.")      #If it doesn't, it tells you

isvowel(str(input("Please enter a letter: ")))  #Asks user for a vowel and passes it to the function