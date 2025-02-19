##Source: https://pynative.com/python-basic-exercise-for-beginners/

##Given two integer numbers, write a
#Python code to return their product only
#if the product is equal to or lower than 1000. Otherwise, return their sum.


number1=int(input("Enter number1: "))
number2=int(input("Enter number2: "))

def result(number1, number2):
    #check the condition
    product=number1*number2
    sum=number1+number2
    
    if(product<=1000):
     return product
    else:
     return sum
     

print(result(number1,number2))

