"""
CODSOFT - Python Programming Internship
Task 4: Rock-Paper-Scissors Game

The user plays against the computer across multiple rounds.
Tracks the score, shows results each round, and asks the user
whether to play again after each round.
"""

import random

CHOICES = ["rock", "paper", "scissors"]

BEATS = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}


def get_user_choice():
    """Ask the user for rock, paper, or scissors (accepts short forms)."""
    shortcuts = {"r": "rock", "p": "paper", "s": "scissors"}
    while True:
        choice = input("Choose rock, paper, or scissors (r/p/s): ").strip().lower()
        if choice in CHOICES:
            return choice
        if choice in shortcuts:
            return shortcuts[choice]
        print("Invalid choice. Please try again.")


def get_computer_choice():
    return random.choice(CHOICES)


def determine_winner(user, computer):
    """Return 'user', 'computer', or 'tie'."""
    if user == computer:
        return "tie"
    if BEATS[user] == computer:
        return "user"
    return "computer"


def main():
    print("========== ROCK-PAPER-SCISSORS ==========")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!\n")
        elif winner == "user":
            print("You win this round!\n")
            user_score += 1
        else:
            print("Computer wins this round!\n")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

        again = input("Play another round? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\n========== FINAL SCORE ==========")
    print(f"You: {user_score}  |  Computer: {computer_score}")

    if user_score > computer_score:
        print("Congratulations, you won overall!")
    elif user_score < computer_score:
        print("Computer won overall. Better luck next time!")
    else:
        print("Overall, it's a tie!")


if __name__ == "__main__":
    main()
