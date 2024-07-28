import random

def get_computer_choice():
    """Randomly select the computer's choice."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "win"
    else:
        return "lose"

def play_round():
    """Play a single round of Rock, Paper, Scissors."""
    choices = ['rock', 'paper', 'scissors']

    user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return None, None

    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")

    return result, computer_choice

def main():
    """Main function to run the game."""
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        result, computer_choice = play_round()

        if result:
            if result == "win":
                user_score += 1
            elif result == "lose":
                computer_score += 1

        print(f"\nScore: You {user_score} - {computer_score} Computer")

        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
