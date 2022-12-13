num1 = float(input("What's the first number? "))
num2 = float(input("What's the second? "))
operators = input("What operation to conduct? ")

if (operators == "+"):
    answer = num1 + num2
    print("The answer is", answer)

elif (operators == "-"):
    answer = num1 - num2
    print("The answer is", answer)
    
elif (operators == "*"):
    answer = num1 * num2
    print("The answer is", answer)

elif (operators == "/"):
    answer = num1 / num2
    print("The answer is", answer)

elif (operators == "%"):
    answer = num1 % num2
    print("The answer is", answer)
    
elif (operators == "**"):
    answer = num1 ** num2
    print("The answer is", answer)

else:
    print("Unknown operator or no operator given")