#Basic maths quiz game

import random

def generate_question():
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    operator=random.choice(['+','-','*',"/",'%'])

    if operator=="+":
        answer=num1 + num2
    elif operator=="-":
        answer=num1 - num2
    elif operator=="*":
        answer=num1 * num2
    else:
        answer = num1 % num2
    return f"{num1} {operator} {num2} ",answer

def math_quiz():
    round=int(input("Enter Number of Question you be played "))
    score=0
    print("\n--- Welcome to the Math Quiz Game! ---")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(round):
        question,correct_answer=generate_question()
        print(f"Question {i+1} : {question}")
        user_answer=int(input("Your answer : "))

        if  correct_answer==user_answer:
            print("Correct!")
            score+=1
        else:
            print(f"Wrong! The Correct answer {correct_answer}")
    print("\n--- Game Over! ---")
    print(f"Your final score is: {score}/{round}")
    if score == round:
        print("Congratulations! You got all the questions correct.")
    elif score >= round // 2:
        print("Good job! You did well.")
    else:
        print("Keep practicing! You can do better next time.")

math_quiz()
