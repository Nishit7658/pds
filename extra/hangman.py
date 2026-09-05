import random

print()
print("Welcome To The Hangman Game !!")
print("""
 _   _      _      _   _    ____   __  __    _    _   _
| | | |    / \    | \ | |  / ___| |  \/  |  / \  | \ | |
| |_| |   / _ \   |  \| | | |  _  | |\/| | / _ \ |  \| |
|  _  |  / ___ \  | |\  | | |_| | | |  | |/ ___ \| |\  |
|_| |_| /_/   \_\ |_| \_|  \____| |_|  |_/_/   \_\_| \_|
                                                        
""")


word_list = [
    "apple", "banana", "orange", "grape", "mango",
    "table", "chair", "window", "door", "house",
    "school", "college", "teacher", "student", "book", 
    "pencil", "notebook", "computer", "keyboard", "mouse",
    "phone", "camera", "bottle", "glass", "plate",
    "river", "mountain", "forest", "ocean", "desert",
    "cloud", "rain", "storm", "summer", "winter",
    "friend", "family", "parent", "brother", "sister",
    "doctor", "engineer", "artist", "driver", "farmer",
    "music", "movie", "game", "football", "cricket",
    "coffee", "tea", "pizza", "burger", "chocolate",
    "happy", "sad", "angry", "brave", "kind",
    "flower", "garden", "animal", "bird", "tiger",
    "lion", "elephant", "horse", "rabbit", "butterfly",
    "train", "car", "bicycle", "airplane", "ship",
    "clock", "watch", "bag", "wallet", "mirror",
    "sun", "moon", "star", "planet", "space",
    "energy", "future", "dream", "success", "freedom",
    "language", "science", "history", "culture", "nature"
]

def get_random_word(word_bank):
    return random.choice(word_bank)


chosen_word = get_random_word(word_list)

print()

print()

life = 6

print("Word to guess:: ")

print()

for i in range(len(chosen_word)):
    print("_", end=" ")

word_guess = []

for i in range(len(chosen_word)):
    word_guess.append("_")

guessed_letters = []

hangman = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """
]

while life > 0:

    print()

    print(" ".join(word_guess))

    print()

    print("Lives left ::", life)

    print()

    guess = input("Guess a letter :: ").lower()

    if len(guess) != 1:
        print("Please enter ONE letter.")
        continue

    if not guess.isalpha():
        print("Please enter a letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:

        for letter in range(len(chosen_word)):

            if chosen_word[letter] == guess:
                word_guess[letter] = guess

        print("Correct Guess !!")

    else:

        life -= 1

        print("Wrong Guess !!")

        print(hangman[6 - life])

    if "_" not in word_guess:

        print()

        print(" ".join(word_guess))

        print()

        print("You Win !!")

        print("The word was ::", chosen_word)

        break

else:

    print()

    print(hangman[5])

    print()

    print("You Lose !!")

    print("The word was ::", chosen_word)



# def get_random_word(word_bank):
#     return random.choice(word_bank)

# chosen_word = get_random_word(word_list)       
# print(chosen_word)

# print()
# print()


# count = 1
# life = 6

# print("Word to guess:: ")
# print()

# for i in range(len(chosen_word)):
#     print("_", end = " ")

# word_guess = []

# for i in range(len(chosen_word)):
#     word_guess.append("_")

# while life > 0:

#     display = ""
#     print()
#     guess = input("Guess a letter :: ").lower()

#     for letter in range(len(chosen_word)):
#         if chosen_word[letter] == guess:
#             word_guess[letter] = guess
#             display += chosen_word[letter]
        
#             # print(letter)
#             # for guess in chosen_word:
#             #     if letter == guess:
#             #         print(letter)
#             #     else:
#             #         print("_")
#         else:
#             display += "_"
    
#     print(" ".join(word_guess))

# #     Start

# # Lives = 6

# # While lives > 0

# #     1. Show the current word
# #        Example:
# #        Word to guess: a_____

# #     2. Ask the user for ONE letter
# #        Guess a letter:

# #     3. Check if the letter is in the hidden word.

# #         If YES
# #             Reveal all matching letters.
# #             Example:
# #             a__l_

# #             If the whole word is revealed
# #                 You Win
# #                 Stop

# #         If NO
# #             Lose one life.
# #             Show the next Hangman picture.

# #     4. Show how many lives are left.

# # Repeat