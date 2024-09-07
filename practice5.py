import random

def check_input(n):
    if not isinstance(n, int) or n < 1 or n > 3:
        raise ValueError("Invalid input. Please enter a number between 1 and 3.")

def get_user_move(n):
    while True:
        try:
            move = int(input(f"Your turn. How many stones do you want to take? (1-3, {n} left): "))
            check_input(move)
            return move
        except ValueError as e:
            print(e)

def get_computer_move(n):
    if n <= 3:
        return n
    else:
        return random.choice([1, 2, 3])

def play_game():
    n = random.randint(4, 30)
    print(f"Let's play a game of Nim with {n} stones!")

    while n > 0:
        print(f"\n{n} stones left.")
        user_move = get_user_move(n)
        n -= user_move
        print(f"You took {user_move} stones.")

        if n > 0:
            computer_move = get_computer_move(n)
            n -= computer_move
            print(f"Computer took {computer_move} stones.")

    if n == 0:
        print("Computer wins!")
    else:
        print("You win!")

if __name__ == "__main__":
    play_game()