history_numbers = []
history_operations = []
operations =['+','-','*','/']



while True:
    try:
        solution = float(input("Choose the first number "))
        break
    except ValueError:
        print("oops! That was no a valid number")

history_numbers.append(str(solution))

while True:
    while True:  
        op = input("Choose the operation ")
        if op in operations:
            history_operations.append(op)
            break
        else:
            print("oops! That was no a valid operation")
    while True:
        try:
            nxt = float(input("Choose the next number "))
            break
        except ValueError:
            print("oops! That was no a valid number")

    history_numbers.append(str(nxt))

    if op == '+':
        solution += nxt
    elif op == '-':
        solution -= nxt
    elif op == '*':
        solution *= nxt
    else:
        solution /= nxt

    print("the result is",solution)

    if input("Would you like to finish? ") == "yes":
        break

print(history_numbers)
print(history_operations)