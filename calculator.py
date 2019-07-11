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
    operators = {"+": add, "-": subtract, "*": multiply,"/": divide}

    if userinput == "q":
            print("You have decided to quit")
            break

    elif operator:
        num1 = float(tokens[1])
        num2 = float(tokens[2])

        result = operators[operator](num1, num2) 

        
    else:
        print("please provide two numbers") 

    print(result)