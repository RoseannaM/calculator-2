"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    # read input
    userinput = input()
    tokens = userinput.split(" ")
    operator = tokens[0]
    if userinput == "q":
            print("You have decided to quit")
            break

    num1 = int(tokens[1])
    num2 = int(tokens[2])

    result = 0

    operators = {"+": add(num1,num2), "-": subtract(num1,num2)}
    
    for op, fun in operators:
        print(op)
        result = op(float(num1), float(num2))

    # if operator == "+":
    #     result = add(float(num1), float(num2))
    # elif operator == "-":

    #     result = subtract(float(num1), float(num2))

    # elif operator == "-":
    #     result = subtract(float(num1), float(num2))
    
    else:
        print("please provide two numbers") 

    print(result)
        # multiply(float, float) → float
        
        # divide(float, float) → float
        
        # square(float) → float
        
        # cube(float) → float
        
        # power(float, float) → float
        
        # mod(float, float) → float
        
    # tokenize input
    # if the first token is "q":
    #     quit
    # else:
    #     decide which math function to call based on first token
