from art import logo, vs
from game_data import data
import random

print(logo)
score = 0
still_going = True


def change_position(q_a, q_b):
    while q_a == q_b:
        q_a = q_b


while still_going:
    question_a = random.randint(0, len(data) - 1)
    question_b = random.randint(0, len(data) - 1)

    data_a = data[question_a]
    data_b = data[question_b]
    print(f"Compare A: {data_a['name']}, a {data_a['description']}, "
          f"from {data_a['country']}")
    print(vs)
    print(f"Against B: {data_b['name']}, a {data_b['description']}, "
          f"from {data_b['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == "a":
        if data_a['follower_count'] > data_b['follower_count']:
            score += 1
            print(f"You're right! Current score {score}")
            change_position(question_a, question_b)
        else:
            still_going = False
            print(f"Sorry that's wrong. Final score: {score}")
    else:
        if data_b['follower_count'] > data_a['follower_count']:
            score += 1
            print(f"You're right! Current score {score}")
            change_position(question_a, question_b)
        else:
            still_going = False
            print(f"Sorry that's wrong. Final score: {score}")
