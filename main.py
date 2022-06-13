import random

while True:
    user_action = input("Enter a choice(rock, paper, scissors): ")
    possible_actions = ["r", "p", "s"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "r":
        if computer_action == "s":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "p":
        if computer_action == "r":
            print("Papers cover rock! You win!")
        else:
            print("Scissors cut paper! You lose.")
    elif user_action == "s":
        if computer_action == "p":
            print("Scissors cut paper! You win!")
        else:
            print("Rock smashes scissor! You lose.")
    else:
        print("That's not a valid play. Check your spelling!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break