import random

def mane_function():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    print(num1, " + ", num2, " = ")
    user_answer = int(input("Your answer: "))
def test_function():
    num3 = random.randint(25, 50)
    num4 = random.randint(1, 25)
    print(num3, " - ", num4, " = ")
    user_answer = int(input("Your answer: "))
    actual_answer = num3 - num4
    answers = (user_answer, actual_answer)
    return answers