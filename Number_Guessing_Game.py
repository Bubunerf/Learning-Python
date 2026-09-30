import random
def number_guessing_game():
    print("Welcome to the Number guessing game!\nI'm thinking of a number between 1 and 100") 
    difficulty = input("Chose a difficulty. Type 'easy' or 'hard' ").lower()
    num_of_lives = lives(difficulty)
    if num_of_lives != None:
        print(f"Number of lives: {num_of_lives}")  
        random_num(num_of_lives)
    else:
        print("Please choose a valid difficulty next time playing")

def lives(chosen_difficulty):
    lives = 0
    if chosen_difficulty == "easy":
        lives = 10
    elif chosen_difficulty == "hard":
        lives = 5
    else:
        return
    return lives

def random_num(num_of_player_lives):
    num_to_be_guessed  = random.randint(1 , 100)
    guess = 0
    while guess != num_to_be_guessed: 
        guess = int(input("Make a guess: "))
        if num_of_player_lives > 0:   
            if guess < num_to_be_guessed:
                print("Guess Higher")
                num_of_player_lives -= 1  
                print(f"You have {num_of_player_lives} remaining")
            elif guess > num_to_be_guessed:
                print("Guess Lower")
                num_of_player_lives -= 1
                print(f"You have {num_of_player_lives} remaining")
            else:
                print(f"You got it the correct answer was {num_to_be_guessed}")        
        else:
            print("You have run out of lives retry the game")        

number_guessing_game()

