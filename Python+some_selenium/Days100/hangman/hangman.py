import random
import hangman_words as hw, hangman.hangman_art as ha
def check_letter(letter, word, stages):
    idx, cnt = [], 0
    for i in word:
        if i == letter:
            idx.append(cnt)
        cnt += 1
    if idx:
        print("Right\n")
        print(stages[-1])
    else:
        print("Wrong\n")
        stages.pop(-1)
        print(stages[-1])
    return idx

def choose_word(lst):
    return lst[int(random.randint(0, len(lst)-1))]

def replace(word):
    display = []
    for i in range(len(word)):
        display.append("_")
    return display

def replace_blank(display, idx, letter):
    for i in idx:
        display[i] = letter
    return display

print(ha.logo)
stages = ha.stages
word_list = hw.word_list
chosen_word = choose_word(word_list)
display = replace(chosen_word)
print(f" ".join(display))
win, gone = False, False
while not win or not gone:

    guess = input("Guess a letter: ").lower()
    while guess in display:
        print(f" ".join(display))
        guess = input("Already guest -> Guess a new letter: ").lower()

    display = replace_blank(display, check_letter(guess, chosen_word, stages), guess)
    print(f" ".join(display))
    if "_" not in display:
        win = True
        print("You WIN!!")
    if len(stages) == 1:
        print("You Lose!!")
        gone = True
        break



