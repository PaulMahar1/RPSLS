
'''
Create a game of rock, paper, scissors, lizard, spock.
Import random.
Ask the user to choose rock, paper, scissors, lizard, or spock.
Assign the computers choice randomly.
Set win conditions.
Tell the user if they win or lose
Ask the user if they want to play again
'''
import random

def game():

    choices = ["rock" , "paper" , "scissors" , "lizard" , "spock"]
    pc_hand = random.choice(choices)

    while True:
        player_hand = input("\nChoose Rock, Paper, Scissors, Lizard, or Spock: ").lower()
        if player_hand in choices:
            break
        else:
            print("\nInvalid choice. Please choose from Rock, Paper, Scissors, Lizard, or Spock.")

    print(f"\nYou chose {player_hand.capitalize()}!")
    input("\nPress enter to see what the PC chose.")
    print(f"\nThe PC chose {pc_hand.capitalize()}")
    print(" ")

    if player_hand == "rock" and pc_hand == "scissors":
        print(f"Congrats! {player_hand.capitalize()} smashes {pc_hand.capitalize()} and you win! Not sure what you have against scissors but congrats anyway!")
    elif player_hand == "rock" and pc_hand == "lizard":
        print(f"Congrats! {player_hand.capitalize()} smashes {pc_hand.capitalize()}...It is not a pretty sight, but you still win!")
    elif player_hand == "rock" and pc_hand == "paper":
        print(f"Womp womp... Your {player_hand.capitalize()} was covered by {pc_hand.capitalize()}. Pesky paper always ruining the good rocks.")
    elif player_hand == "rock" and pc_hand == "spock":
        print(f"You lose! {pc_hand.capitalize()} disintegrated your {player_hand.capitalize()}. Sucks to suck. You can get a new rock, but he will probably disintegrate it as well.")
    
    elif player_hand == "paper" and pc_hand == "rock":
        print(f"Hooray! Your {player_hand.capitalize()} covers the {pc_hand.capitalize()}! You win, until there is a gust of wind...")
    elif player_hand == "paper" and pc_hand == "scissors":
        print(f"Sorry, {pc_hand.capitalize()} cuts your {player_hand.capitalize()}. Not even into a cool origami swan or anything, just worthless pieces. You lose!")
    elif player_hand == "paper" and pc_hand == "lizard":
        print(f"Too bad! {pc_hand.capitalize()} eats your {player_hand.capitalize()}. You lost, but the Lizard has a full tummy at least!")
    elif player_hand == "paper" and pc_hand == "spock":
        print(f"You win! Your {player_hand.capitalize()} disproves {pc_hand.capitalize()}. He cries as he is erased from time itself. Good job!")

    elif player_hand == "scissors" and pc_hand == "rock":
        print(f"You lost! {pc_hand.capitalize()} smashes your {player_hand.capitalize()}. Git gud!")
    elif player_hand == "scissors" and pc_hand == "paper":
        print(f"Great! {player_hand.capitalize()} cuts {pc_hand.capitalize()}. Ez win!")
    elif player_hand == "scissors" and pc_hand == "lizard":
        print(f"Victory! Your {player_hand.capitalize()} decapitate the {pc_hand.capitalize()}. You'll really do anything to win, wont you? You win... I guess!")
    elif player_hand == "scissors" and pc_hand == "spock":
        print(f"Sorry, {pc_hand.capitalize()} smashes your {player_hand.capitalize()}. Not very Spock-like is you ask me but oh well, you lost!")

    elif player_hand == "lizard" and pc_hand == "rock":
        print(f"You lost! {pc_hand.capitalize()} crushes your {player_hand.capitalize()}. Poor little fella...Try again, AVENGE HIM!")
    elif player_hand == "lizard" and pc_hand == "paper":
        print(f"You win! Your {player_hand.capitalize()} eats {pc_hand.capitalize()}. I can't image is tastes great but congratulations!!")
    elif player_hand == "lizard" and pc_hand == "scissors":
        print(f"Too bad! The {pc_hand.capitalize()} decapitate your {player_hand.capitalize()} as you watch in horror. You lost, but the Lizard lost more!")
    elif player_hand == "lizard" and pc_hand == "spock":
        print(f"Congratulations! Your {player_hand.capitalize()} poisons {pc_hand.capitalize()}. You laugh as he suffers. You win!")

    elif player_hand == "spock" and pc_hand == "rock":
        print(f"Congratulations! {player_hand.capitalize()} vaporizes {pc_hand.capitalize()}. You defeated your opponent!")
    elif player_hand == "spock" and pc_hand == "paper":
        print(f"Too bad! {pc_hand.capitalize()} disproves {player_hand.capitalize()} and he fades into obscurity. You certainly lost!")
    elif player_hand == "spock" and pc_hand == "scissors":
        print(f"You win! {player_hand.capitalize()} smashes the {pc_hand.capitalize()} with little to no effort. Well done!")
    elif player_hand == "spock" and pc_hand == "lizard":
        print(f"Unlucky! The {pc_hand.capitalize()} poisons {player_hand.capitalize()} and he dies a slow painful death. You lost!")

    print("")

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

while True:
    game()
    if not play_again():
        print("Thanks for playing!")
        break