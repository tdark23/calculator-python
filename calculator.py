def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculation():
    # enter the first number

    num1 = float(input("Enter your first number : "))

    # Print the operation symbols

    for op in operations:
        print(op)

    should_continue = True

    while should_continue:

        # Make the user select the operation symbol and keep it in a variable

        selected_symbol = input("Pick an operation ? ")

        # Enter the second number

        num2 = float(input("Enter the next number : "))

        # Select the right function in the dictionnary based on the operationsymbol thee user selected

        calculation_function = operations[selected_symbol]

        def process(pos1, pos2):
            return calculation_function(pos1, pos2)

        # call the calculation function and keep the resultin the answer variable
            
        answer = process(num1, num2)

        print(f"{num1} {selected_symbol} {num2} = {answer}")

        if input(f"type 'y' to continue calculating with {answer} or 'n' if you want to stop there : ") == "y":
            num1 = answer
        else:
            should_continue = False
            # Recursion : recall the function, making the calculation restart over and over and over ...
            calculation()

calculation()
