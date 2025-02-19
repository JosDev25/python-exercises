##Source: https://pynative.com/python-basic-exercise-for-beginners/

# Write a Python code to iterate the first 10 numbers,
# and in each iteration, print the sum of the current
# and previous number.

for i in range(0, 10):
    if i == 0:
        previousNumber = 0
    else:
        previousNumber = i - 1

    print("Current Number: ", i)
    print("Previous Number: ", previousNumber)

    sum = i + previousNumber
    print("Sum: ", sum)
