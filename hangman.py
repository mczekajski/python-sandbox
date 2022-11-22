import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print('Psst, the solution is ' + chosen_word)

display = []
for _ in range(len(chosen_word)):
    display += "_"

end_of_game = False
lives = 5

while not end_of_game:
    guess = input('Guess a letter: ').lower()

    if guess not in chosen_word:
        lives -= 1
        if lives:
            print("Wrong! You have only {lives} lives left.".format(lives=lives))
            continue
        else:
            end_of_game = True
            print("You lose!")
            break

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")

# for l in chosen_word:
#     display[index](l if l == letter else "_")
#     print("Right" if l == letter else "Wrong")

