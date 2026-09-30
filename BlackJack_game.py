import random
# I have almost done everything but i could not implement the 1 / 11 ace card switch
# Date: 19/08/2026
# Author : Can Ekiz

def card_dealing():
       
    cards = [11 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 10]

    player_cards = random.choices(cards , k = 2)
    print(f"Here is your hand with you're cards {player_cards}") # But here it is not like that due to using "choices" command which give us multiple integers inside a list


    dealer_hand = [] #Since using "choice" for the inital hand of the dealer we get an integer not a list so we reshape the code to append the chosen int to a empty list
    dealers_initial_card = dealer_hand.append(random.choice(cards))
    print(f"Here is the dealers hand {dealer_hand}")

        # Up until this point we have dealt the initial hands, from this point onward we have to choose to deal new hands and check them at the same time
    player_score = 0
    continue_or_not = "y"
    while continue_or_not == "y":
            
        continue_or_not = input("Would you like to hit or stand, type 'y' to hit 'n' to stand?: ")
        if continue_or_not == "y":   
            player_cards.append(random.choice(cards))
            print(f"This is you're hand {player_cards}")
        player_score = score_calculations(player_cards)

        if player_score > 21:
            print("You went above 21 , You Lose")
            return 

    dealer_hand.append(random.choice(cards))
    print(f"This is the dealers hand {dealer_hand}")
    dealer_score = score_calculations(dealer_hand)

    while dealer_score < 17:
        dealer_hand.append(random.choice(cards))
        dealer_score = score_calculations(dealer_hand)
        print(dealer_hand)
   
    if dealer_score > 21:
        print("The dealer went above 21 , You Win!")
        return
    return player_score , dealer_score



def Blackjack(): 

    play_or_not = input("Would you like to play a game of 21 it yes type 'y' if not 'n': ")
    print("Welcome dear player quick heads up withing you're hand the ace card can bee seen as '11' \nunless you pass 21 it will stay like that in the case of you passing it the'11' will act as a '1' ")
    if play_or_not == 'y':
        result = card_dealing()
        if result is None:
            return
        score_player , score_dealer = result
        win_or_not(score_player , score_dealer)
    else:
        print("Thank you for coming maybe next time ;) ")
    
        
def score_calculations(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        score -= 10
    return score
        
    
       


def win_or_not(score1 , score2):
    print(f"This is youre final score {score1}")
    print(f"This is the dealers final score {score2}")
    max_score = 21
    calc_score1 = max_score - score1
    calc_score2 = max_score - score2
    if calc_score1 < calc_score2:
        print("You Win!")
    elif calc_score1 == calc_score2:
        print("It is a tie")
    else:
        print("You Lose")     
    
Blackjack()