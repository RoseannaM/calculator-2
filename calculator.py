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
    result = None
    operators = {"+": add, "-": subtract, "*": multiply, "/": divide, "pow" : power, "mod" : mod, "square" : square, "cube" : cube}

    if userinput == "q":
            print("You have decided to quit")
            break

    #ensure operator exists
    elif list(operators.keys()).count(operator) > 0:
        num1 = float(tokens[1])
        num2 = float(tokens[2]) if len(tokens) == 3 else None
        
        if len(tokens) > 2:
            result = operators[operator](num1, num2)
        #handle case for square and cube 
        else:
            result = operators[operator](num1)

        print(result)
        
    else:
        print("please provide two numbers")

    