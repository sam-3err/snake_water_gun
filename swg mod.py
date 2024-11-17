import random

def play_game():
    print("Let's play Gun vs Snake vs Water")
    team = ["Gun", "Snake", "Water"]
    user = input("Enter your choice (Gun, Snake, Water): ")
    if user not in team:
        print("Invalid choice! Please choose between 'Gun', 'Snake', or 'Water'.")
        return False  

    computer = random.choice(team)
    print("Opponent choice is:", computer)

   
    if user == computer:
        print("Draw, Try again!")
    elif user == "Gun" and computer == "Snake":
        print("You win!")
    elif user == "Snake" and computer == "Water":
        print("You win!")
    elif user == "Water" and computer == "Gun":
        print("You win!")
    else:
        print("You lose!")
    
    return True 

def main():
    while True:
        if not play_game():
            print("Please try again with a valid choice.")
            continue  
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again == "no":
            print("Thanks for playing! Goodbye.")
            break
        elif play_again != "yes":
            print("Invalid input! Exiting the game.")
            break  
if __name__ == "__main__":
    main()
