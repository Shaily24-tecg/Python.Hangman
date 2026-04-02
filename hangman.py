import tkinter as tk
import random

# ----------- Words from file ----------- #
with open("words.txt", "r") as file:
    word_list = file.read().splitlines()

# ----------- Root Window ----------- #
root = tk.Tk()
root.title("Hangman Game")
root.geometry("600x400")
root.resizable(False, False)

# ----------- Colors ----------- #
BG_COLOR = "pink"
BTN_COLOR = "blue"
BTN_TEXT_COLOR = "white"
LABEL_COLOR = "purple"

# ----------- Frames ----------- #
home_page = tk.Frame(root, width=600, height=400, bg=BG_COLOR)
category_page = tk.Frame(root, width=600, height=400, bg=BG_COLOR)
game_page = tk.Frame(root, width=600, height=400, bg=BG_COLOR)
result_page = tk.Frame(root, width=600, height=400, bg=BG_COLOR)

for frame in (home_page, category_page, game_page, result_page):
    frame.grid(row=0, column=0, sticky="nsew")

# ----------- Variables for Game ----------- #
word = ""
guessed_word = []
chances = 6

# ----------- Functions ----------- #
def show_frame(frame):
    frame.tkraise()

def start_game(category=None):
    global word, guessed_word, chances
    word = random.choice(word_list).lower()
    guessed_word = ["_" for _ in word]
    chances = 6
    word_label.config(text=" ".join(guessed_word))
    info_label.config(text=f"Chances: {chances}")
    result_label.config(text="")
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.focus()
    show_frame(game_page)

def end_game(win):
    entry.config(state="disabled")
    if win:
        result_text.config(text="You Win! 🎉", fg="green")
    else:
        result_text.config(text=f"You Lose! Word was {word} 😢", fg="red")
    show_frame(result_page)

def check_guess():
    global chances
    guess = entry.get().lower().strip()
    entry.delete(0, tk.END)

    # Only process single letter guess
    if len(guess) != 1 or not guess.isalpha():
        result_label.config(text="Enter one letter!", fg="red")
        return

    if guess in guessed_word:  # Prevent repeating same correct guess
        result_label.config(text="Letter already guessed!", fg="orange")
        return

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
        result_label.config(text="Correct!", fg="green")
    else:
        chances -= 1
        result_label.config(text="Wrong!", fg="red")

    word_label.config(text=" ".join(guessed_word))
    info_label.config(text=f"Chances: {chances}")

    # Check win/lose
    if "_" not in guessed_word:
        end_game(True)
    elif chances == 0:
        end_game(False)

# ----------- Home Page ----------- #
home_container = tk.Frame(home_page, bg=BG_COLOR)
home_container.place(relx=0.5, rely=0.5, anchor='center')

tk.Label(home_container, text="Welcome To Hangman Game", font=("Arial", 32),
         fg=LABEL_COLOR, bg=BG_COLOR).pack(pady=10)
tk.Button(home_container, text="Start", font=("Arial", 18),
          bg=BTN_COLOR, fg=BTN_TEXT_COLOR,
          command=lambda: show_frame(category_page)).pack(pady=10)

# ----------- Category Page ----------- #
category_container = tk.Frame(category_page, bg=BG_COLOR)
category_container.place(relx=0.5, rely=0.5, anchor='center')

tk.Label(category_container, text="Select Category", font=("Arial", 28),
         fg=LABEL_COLOR, bg=BG_COLOR).pack(pady=10)
tk.Button(category_container, text="Fruits", font=("Arial", 16),
          bg=BTN_COLOR, fg=BTN_TEXT_COLOR,
          command=lambda: start_game("Fruits")).pack(pady=5)
tk.Button(category_container, text="Vegetables", font=("Arial", 16),
          bg=BTN_COLOR, fg=BTN_TEXT_COLOR,
          command=lambda: start_game("Vegetables")).pack(pady=5)
tk.Button(category_container, text="Countries", font=("Arial", 16),
          bg=BTN_COLOR, fg=BTN_TEXT_COLOR,
          command=lambda: start_game("Countries")).pack(pady=5)

# ----------- Game Page ----------- #
game_container = tk.Frame(game_page, bg=BG_COLOR)
game_container.place(relx=0.5, rely=0.5, anchor='center')

word_label = tk.Label(game_container, text="", font=("Arial", 28),
                      fg=LABEL_COLOR, bg=BG_COLOR)
word_label.pack(pady=10)

info_label = tk.Label(game_container, text="", font=("Arial", 14),
                      fg=LABEL_COLOR, bg=BG_COLOR)
info_label.pack(pady=5)

entry = tk.Entry(game_container, font=("Arial", 14),
                 bg="orange", fg="white", insertbackground="white")
entry.pack(pady=10)
entry.bind("<Return>", lambda event: check_guess())  # Enter key works once

btn = tk.Button(game_container, text="Guess", font=("Arial", 14),
                bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=check_guess)
btn.pack(pady=10)

result_label = tk.Label(game_container, text="", font=("Arial", 14),
                        fg="red", bg=BG_COLOR)
result_label.pack(pady=5)

# ----------- Result Page ----------- #
result_container = tk.Frame(result_page, bg=BG_COLOR)
result_container.place(relx=0.5, rely=0.5, anchor='center')

result_text = tk.Label(result_container, text="", font=("Segoe UI Emoji", 28),
                       fg=LABEL_COLOR, bg=BG_COLOR)
result_text.pack(pady=10)

tk.Button(result_container, text="Play Again", font=("Arial", 16),
          bg=BTN_COLOR, fg=BTN_TEXT_COLOR,
          command=lambda: show_frame(home_page)).pack(pady=10)

# ----------- Start ----------- #
show_frame(home_page)
root.mainloop()
