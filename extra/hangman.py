import random

print()
print("Welcome To The Hangman Game !!")
print(r"""
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
print(chosen_word)
guess = input("Guess a letter :: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")

