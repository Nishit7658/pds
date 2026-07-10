import random

choice = int(input("Enter the choice (1) for rock (2) for paper (3) for scissor :: "))
print()

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

if choice == 1:
    print("""You chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif choice == 2:
    print("""You chose:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    
elif choice == 3:
    print("""You chose:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("Choose the right option.")

computer_choice = random.randint(1, 3)

print("Computer chose:")
print(game_images[computer_choice - 1])

if choice == computer_choice:
    print("It's a draw!")

elif choice == 1 and computer_choice == 3:
    print("You win!")

elif choice == 2 and computer_choice == 1:
    print("You win!")

elif choice == 3 and computer_choice == 2:
    print("You win!")

else:
    print("Computer wins!")


