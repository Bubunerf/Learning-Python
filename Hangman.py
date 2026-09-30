import random

word_list = ["apple", "pear", "unpleseant", "happy", "capybara"]

# To do 1) Creat an empty string called placholder with the same number of blanks as the chosen word

chosen_word = random.choice(word_list)

place_holder = ""
lenght_of_word = len(chosen_word)  
# To do 2) Add _ for the number of letters in the word so apple should be printed with _ _ _ _ _
for display in range(lenght_of_word):
    place_holder += "_"

number_of_lives = 6
print(f"You have {number_of_lives} lives in total, use them wisely!")
print(place_holder)

Check = set()
Length_of_Check = len(Check)
while place_holder != chosen_word and number_of_lives > 0:
    guess = input("Please guess a letter\n").lower()
    final = ""
    word_num = 0
    Is_Found = False
    for letter in range(lenght_of_word):  
        if guess == chosen_word[word_num]: 
            final += guess   
            Is_Found = True
            for correct_guess in Check:
                if guess == correct_guess:
                    print(f"You have already guessed {guess}")

            Check.add(guess)

        else:
            final += place_holder[word_num]    
        word_num += 1
    
    
    if Is_Found == False:
        number_of_lives -= 1
        print(f"You have guessed {guess}, that is not in the word you lose one life\n Lives remeaning {number_of_lives}/6")    

    if number_of_lives == 0:
        print("You lose")

    place_holder = final

    print(Check)    

    print(place_holder)

if "_" not in place_holder:
    print("You Win!")


# Teachers solution for to do 3
# for letter in chosen_word:
#   if letter == guess:
#       print("Right")
#   else:
#       print("Wrong")