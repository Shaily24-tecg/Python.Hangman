import tkinter as tk
import random

# ----------- Words from file ----------- #
with open("words.txt", "r") as file:
    words = [line.strip().lower() for line in file]

word = random.choice(words)
guessed_word = ["_"] * len(word)
chances = 6

# ----------- Window ----------- #
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x400")
root.configure(bg="#1e1e2f")  # dark theme

# ----------- Labels ----------- #
word_label = tk.Label(root, text=" ".join(guessed_word),
 font=("Arial", 24),
 bg="#1e1e2f",
 fg="white"
)
word_label.pack(pady=20)

info_label = tk.Label(root, text=f"Chances: {chances}",
 font=("Arial", 14),
 bg="#1e1e2f",
 fg="blue"
 )
info_label.pack()

entry = tk.Entry(root,
 font=("Arial", 14),
 bg="#2e2e3e",
 fg="white",
 insertbackground="white") # cursor color
entry.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14),
bg="#1e1e2f",
fg="yellow")
result_label.pack()

# ----------- Function ----------- #
def check_guess():
    global chances

    guess = entry.get().lower()
    entry.delete(0, tk.END)

    # input check
    if len(guess) != 1 or not guess.isalpha():
        result_label.config(text="Enter one letter!")
        return

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        result_label.config(text="Correct",fg="green")
    else:
        chances -= 1
        result_label.config(text="Wrong",fg="red")

    word_label.config(text=" ".join(guessed_word))
    info_label.config(text=f"Chances: {chances}")

    if "_" not in guessed_word:
        result_label.config(text="You Win!",fg="green")
        entry.config(state="disabled")
    elif chances == 0:
        result_label.config(text=f"You Lose! Word was {word}",fg="red")
        entry.config(state="disabled")

# ----------- Button ----------- #
btn = tk.Button(root,
 text="Guess",
 font=("Arial", 14),
 bg="#00994d",
 fg="black",
 command=check_guess,
 activebackground="#007a3d",
 padx=10,
 pady=5)
btn.pack(pady=10)

# ----------- Run ----------- #
root.mainloop()