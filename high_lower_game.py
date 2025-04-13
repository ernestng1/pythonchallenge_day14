from game_data import data
from art import logo, vs
import random

game_score = 0
person_A = ""

def game(score, personA):
    print(logo)
    if score > 0:
        print(f"You're right! Current score {score}")
    if personA == "":
        personA = random.choice(data)
    print(f"Compare A: {personA['name']}, a {personA['description']}, from {personA['country']}.")
    print(vs)
    personB = random.choice(data)
    while personB == personA:
        personB = random.choice(data)
    print(f"Against B: {personB['name']}, a {personB['description']}, from {personB['country']}.")
    user_input = input("Who has more followers? Type 'A' or 'B': ")
    if user_input == "A" and personA['follower_count'] > personB['follower_count']:
        score += 1
        print("\n" * 20)
        game(score, personA)
    elif user_input == "B" and personB['follower_count'] > personA['follower_count']:
        score += 1
        print("\n" * 20)
        game(score, personB)
    else:
        print("\n" * 20)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")

game(game_score, person_A)

