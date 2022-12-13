import math


def subtract1():
    num1 = int(input("What's your first number? "))
    num2 = int(input("What's your second number? "))
    answer = num1 - num2
    print("The answer is:", answer)

def multiply1():
    num1 = int(input("What is your first number? "))
    num2 = int(input("What is your second number? "))
    answer = num1 * num2
    print("The answer is:", answer)
    
def divide1():
    num1 = int(input("What's your first number? "))
    num2 = int(input("What's your second number? "))
    answer = num1 / num2
    print("The answer is:", answer)

def volume1 ():
    radius = int(input("What is the cylinder's radius? "))
    depth = int(input("what is the cylinder's depth? "))
    volume = round(depth * math.pi * radius ** 2, 3)
    print("The cylinder's volume is:", volume, "rounded to 3 decimal places.")