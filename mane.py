import random

def mane_function():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    print(num1, " + ", num2, " = ")
    user_answer = int(input("Your answer: "))
    actual_answer = num1 + num2