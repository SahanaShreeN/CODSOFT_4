import random

def get_user_choice():
    user_choice = input("Rock, paper, scissors? ")
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again.")
        user_choice = input("Rock, paper, scissors? ")
    return user_choice

def get_computer_choice():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "user"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "user"
    elif user_choice == "paper" and computer_choice == "rock":
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print("You chose: ", user_choice)
    print("The computer chose: ", computer_choice)
    if winner == "user":
        print("You win!")
    elif winner == "computer":
        print("You lose.")
    else:
        print("Tie game.")

def play_again():
    play_again = input("Do you want to play again? (y/n) ")
    while play_again not in ["y", "n"]:
        print("Invalid choice. Try again.")
        play_again = input("Do you want to play again? (y/n) ")
    return play_again == "y"

def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        display_result(user_choice, computer_choice, winner)

        if not play_again():
            break

    print("Final score:")
    print("You:", user_score)
    print("Computer:", computer_score)

if __name__ == "__main__":
    main()
