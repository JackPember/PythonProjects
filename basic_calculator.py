import os
operations = ["+", "-", "*", "/"]

def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2

calc = {"+": add,
        "-": sub,
        "*": mul,
        "/": div,
       }

def calculate(first, second, op):
        operation = calc[op]
        result = operation(first, second)
        return result

            
def getFirstNumber():
        try:
            firstNum = float(input("Enter the first number: "))
        except ValueError:
            print("Please enter a number!")
        return firstNum

def getOperation():
    print("+\n-\n*\n/")
    valid_op = False
    while valid_op != True:
        operator = str(input("Pick the operation to perform "))
        if operator not in operations:
            print("Please pick a valid operator!")
        if operator in operations:
            valid_op = True
    return operator

def getSecondNumber():
    try:
        secondNum = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter a number!")
    return secondNum

def main():
    while True:
            firstNumber = getFirstNumber()
            operator = getOperation()
            if operator == "/":    
                while True:
                        secondNumber = getSecondNumber()
                        if secondNumber == 0.0:
                            print("You can't divide by zero, enter a different number!")
                        else:
                            break
            else:
                secondNumber = getSecondNumber()
            result = calculate(firstNumber, secondNumber, operator)
            print(f"{firstNumber} {operator} {secondNumber} = {result}")
            while True:
                next_calc = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, or 'x' to exit: ")
                if next_calc == "y":
                    firstNumber = result
                    print(f"Continuing calculation with {firstNumber} as the first number")
                    operator = getOperation()
                    if operator == "/":    
                        while True:
                            secondNumber = getSecondNumber()
                            if secondNumber == 0.0:
                                print("You can't divide by zero, enter a different number!")
                            else:
                                break
                    else:
                        secondNumber = getSecondNumber()
                    result = calculate(firstNumber, secondNumber, operator)
                    print(f"{firstNumber} {operator} {secondNumber} = {result}")
                elif next_calc == "n":
                    break
                elif next_calc == "x":
                    os._exit(0)
                else:
                    print("please enter either 'y' or 'n' to continue calculation, or 'x' to exit.")
            

if __name__ == "__main__":
    main()
