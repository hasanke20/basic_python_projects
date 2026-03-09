import art
def operations(number1, number2, operation):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        pass
    return number1 / number2
print(art.calculator)
continue_with_f_number = True
start_from_zero = True
while start_from_zero:
    f_number = int(input("What is the first number?"))
    continue_with_f_number = True
    while continue_with_f_number:
        operation = input("+\n-\n*\n/\nPick an operation:")
        s_number = int(input("What is the second number?"))
        result = operations(f_number, s_number, operation)
        print(f"{f_number} {operation} {s_number} = {result}")
        wanna_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation or type 'q' to quit: ")
        if wanna_continue == 'n':
            continue_with_f_number = False
        elif wanna_continue == 'y':
            f_number = result
        elif wanna_continue == 'q':
            start_from_zero = False
            continue_with_f_number = False