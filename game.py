import random

# Snake Water Gun Game

choices = {"s": 1, "w": -1, "g": 0}
reverse = {1: "Snake", -1: "Water", 0: "Gun"}

computer = random.choice([1, -1, 0])
you_input = input("Enter your choice (s/w/g): ").lower()

if you_input not in choices:
    print("Invalid input! Please choose s, w or g.")
    exit()

you = choices[you_input]

print(f"You chose {reverse[you]}")
print(f"Computer chose {reverse[computer]}")

# Game Logic
if computer == you:
    print("It's a Draw!")

elif (you == 1 and computer == -1) or \
     (you == -1 and computer == 0) or \
     (you == 0 and computer == 1):
    print("You Win!")

else:
    print("You Lose!")