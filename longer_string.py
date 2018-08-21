#Question 2

#A function that can accept two strings as input and print the string with maximum length  in console.
#If two strings have the same length, then the function should print all strings line by line.

#include tests

#===================================================================================

#Answer

def andela(s1,s2):
    len1 = len(s1)
    len2 = len(s2)

    if len1>len2: #check the condition and print string with the maximum length
        print(s1)
    elif len2>len1: #check the condition and print string with the maximum length
        print(s2)
    else:          #if they happen to have the same length,then
        print(s1)  #print the strings line by line
        print(s2)

andela(input("Enter a sentence: "), input("Enter a sentence: ")) #get the string usings the input