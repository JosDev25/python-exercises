##Source: https://pynative.com/python-basic-exercise-for-beginners/

# Write a Python code to accept a string from the 
# user and display characters present at an even
# index number



initalText= input("Enter the text: ")
longitud=len(initalText)

print("Original String is", initalText)

#iterate 0 to longitud in two steps
for i in range (0, longitud, 2):
    print(initalText[i])

