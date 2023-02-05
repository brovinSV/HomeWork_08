import random

def test_function():
    num3 = random.randint(25, 50)
    num4 = random.randint(1, 25)
    print(num3, " - ", num4, " = ")
    user_answer = int(input("Your answer: "))
    actual_answer = num3 - num4
    answers = (user_answer, actual_answer)
    return answers