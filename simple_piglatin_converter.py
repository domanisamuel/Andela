#Question 4

# Write a program that will take a word and output the pig latin version of the word  by following the following rules: 
#1. If the word starts with a consonant or group of consonants, move all letters  before the first vowel to the end of the word then add "ay".
#Example​: 
# will -> illway 
# dog -> ogday 
# category -> ategorycay 
# chatter -> atterchay 
# trash -> ashtra
#2. If the word starts with a vowel, simply add "way" to the end of the word.
# Example​:  andela - andelaway
# electrician - electricianway 

#include tests

#===================================================================================

#Answer

user_input = input("Enter word: ") #get the word to be converted from the input

#first condition
vowels = ['a','e','i','o','u']
def translate(user_input):
    first = user_input[0]
    #second condition
    if first in vowels:    #If the word starts with a vowel, simply add "way" to the end of the word.
        user_input = user_input.lower()
        user_input += "way"
        return user_input
    else:
        user_input = user_input.lower()
    #third conditon
        for letter in user_input:
            if letter in vowels:
                index_value = user_input.index(letter)
                break
   #forth condition     (If the word starts with a consonant or group of consonants, move all letters  before the first vowel to the end of the word then add "ay".)
        user_input = user_input[index_value:] + user_input[:index_value] + "ay"
        return user_input

print(translate(user_input))  #output the converted word