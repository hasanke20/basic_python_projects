import random
import  hangman_stages
stages = hangman_stages.stages
text = hangman_stages.hangman_text
word_list = ["bilgisayar", "kütüphane", "macera", "pencere", "sandalye","televizyon", "şemsiye", "hastane", "portakal", "çikolata","astronomi", "psikoloji", "dinozor", "helikopter", "matematik","edebiyat", "felsefe", "mimari", "okyanus", "astronot"]
answer=  random.choice(word_list)
lifes = 6
print(text)
print(answer + "\nWelcome, to the where people died because of their friends's mistake. ")
lenght = len(answer)
word = ["_"] * lenght
print(f"{word} The word has {lenght} characters.")
while "_" in word:
    checking = word.copy()
    letter = input("\nEnter a letter:").lower()
    for number in range(lenght):
        if letter == answer[number]:
            word[number]= answer[number]
    if checking == word:
        print("Wrong Answer.")
        if lifes >0:
            lifes -= 1
            print(f"You have {lifes} life left.")
    if lifes == 0:
        print(f"You are out of life, Goodbye. The word was {answer}.")
        break
    if "".join(word) == answer:
        print("\n" + "".join(word))
        print("Congratulations, you have won!")
        break
    print("".join(word))
    print(stages[lifes])