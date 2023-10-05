import random

list_of_words = ["recitation", "valuation", "testimony", "renegade", "stipulation", "revere"]
lives = 6
word = random.choice(list_of_words)
print(word)
display = []
for i in range(len(word)):
    display += "_"
print(display)
game_end = False
while not game_end:
    g_letter = input("GUESS THE LETTER:")
    for position in range(len(word)):
        letter = word[position]
        if letter == g_letter:
            display[position] = g_letter
    print(display)
    if g_letter not in word:
        lives -= 1
        if lives == 0:
            game_end = True
            print("YOU LOOSE")
            print("THE WORD WAS", word)
    if "_" not in display:
        game_end = True
        print("YOU WIN!!\n The word is", word)
