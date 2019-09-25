

secret_word = "juniper"
guess = ""
guess_count = 0
guess_limit = 3
out_of_gesses = False

print("What is your favorite vendor?")

while guess != secret_word and not(out_of_gesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count = guess_count + 1
    else:
        out_of_gesses = True

print(guess_count)

if out_of_gesses:
    print("Out of guesses, You lose!")
else:
    print("You win!")





