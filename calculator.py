nextOperation = True


def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def isFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

while nextOperation:
    print("Select the operation:")
    print("1.Add")
    print("2.Substract")
    print("3.Multiplication")
    print("4.Divide")
    operationUserInput = input("Enter choice (1/2/3/4): ")
    if isInt(operationUserInput):
        operation = int(operationUserInput)
        if not (operation >= 1 or operation <= 4):
            print("Doesn't support operation")
            continue
    else:
        print("Wrong input operation, please enter 1/2/3/4")
        continue
    
    user_first_num = input("Enter first number: ")
    if isFloat(user_first_num):
        first_num = float(user_first_num)
    else:
        print("Incorrect input, please enter a number")
        continue

    user_second_num = input("Enter second number: ")
    if isFloat(user_second_num):
        second_num = float(user_second_num)
        if (second_num == 0 and operation == 4):
            print("It's impossible to divide by 0")
            continue
    else:
        print("Incorrect input, please enter a number")
        continue

    if operation == 1:
        print(first_num, "+", second_num, "=", (first_num + second_num))
    elif operation == 2:
        print(first_num, "-", second_num, "=", (first_num - second_num))
    elif operation == 3:
        print(first_num, "*", second_num, "=", (first_num * second_num))
    elif operation == 4:
        print(first_num, "/", second_num, "=", (first_num / second_num))
    else:
        print("Wrong input, try again", operation)

    nextOperation = input("Let's do next calculation? (yes/no): ") == "yes"
