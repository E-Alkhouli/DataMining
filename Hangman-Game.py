import random

# كلمات عن الخوارزميات المعروفة
words = ["bubble", "merge", "sort", "search", "stack",
         "queue", "graph", "tree", "array", "hash"]

# مراحل رسمة الشنق
hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# اختيار كلمة عشوائية
word = random.choice(words)

# إظهار الكلمة بشرطات
hidden_word = ["_"] * len(word)
tries = 6  # عدد المحاولات المتاحة
guessed_letters = set()  # الحروف التي تم إدخالها

print("="*40)
print("  Welcome to Hangman Game (Algorithms Edition)  ")
print("="*40)
print("Guess the algorithm-related word before you lose all tries.\n")
print(hangman_stages[0])  # عرض أول رسمة
print("Word:", " ".join(hidden_word))
print("-"*40)

while tries > 0:
    guess = input("Enter a letter: ").lower()

    # تحقق من الإدخال
    if not guess.isalpha() or len(guess) != 1:
        print("⚠ Please enter a single letter.")
        continue

    # تحقق إذا الحرف مكرر
    if guess in guessed_letters:
        print("⚠ You already guessed that letter. Try another one.")
        continue

    guessed_letters.add(guess)  # أضف الحرف لقائمة المحاولات السابقة

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
        print("\n Correct!")
    else:
        tries -= 1
        print("\n Wrong! Tries left:", tries)

    # عرض الرسمة حسب عدد المحاولات الخاطئة
    stage_index = 6 - tries
    print(hangman_stages[stage_index])
    print("Word:", " ".join(hidden_word))
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print("-"*40)

    if "_" not in hidden_word:
        print(" You Win! The word was:", word)
        break

if "_" in hidden_word:
    print(" Game Over! The word was:", word)
