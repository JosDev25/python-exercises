##Source: https://pynative.com/python-basic-exercise-for-beginners/

# Write a Python code to remove characters from a string from 0 to n and return a new string.
# For Example:

# remove_chars("PYnative", 4) so output must be tive. Here, 
# you need to remove the first four characters from a string.
# remove_chars("PYnative", 2) so output must be native. 
# Here, you need to remove the first two characters from a string.
# Note: n must be less than the length of the string

word=input("Enter your word: ")

number=int(input("Enter number to remove characters: "))

def remove_chars(word, number):
    return (word[number:])

print(remove_chars(word, number))