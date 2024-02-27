# ____________________
#/                    \
#! Advanced Coding in !
#!  Python CIT - 262  !
#\____________________/
#         !  !
#         !  !
#         L_ !
#        / _)!
#       / /__L
# _____/ (____)
#        (____)
# _____  (____)
#      \_(____)
#         !  !
#         !  !
#         \__/   

# Prompts the user for a filename, splits the file string using . as a separator, and 
# prints the extension, which is the text after the last dot
print("The file extension is: " + repr(((input("Enter a filename: ")).split("."))[-1]))