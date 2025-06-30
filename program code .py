### Rock-paper-scissor-game-stax
import random
from collections import deque, Counter

OPTIONS = ["rock", "paper", "scissors"]
recent_moves = deque(maxlen=5)

def get_user_choice():
    while True:
        choice = input("Enter rock, paper, scissors (or quit to exit): ").lower().strip()
        if choice in OPTIONS + ["quit", "q"]:
            return choice
        print("Invalid input. Try again.")

def predict_user_move():
    if len(recent_moves) < 2:
        return random.choice(OPTIONS)
    seq = list(recent_moves)
    next_counts = Counter()
    for i in range(len(seq)-2):
        pair = (seq[i], seq[i+1])
        next_counts[(pair, seq[i+2])] += 1
    last_pair = tuple(seq[-2:])
    candidates = {follow: cnt for (pair, follow), cnt in next_counts.items() if pair == last_pair}
    if not candidates:
        return random.choice(OPTIONS)
    predicted = max(candidates, key=candidates.get)
    return {"rock": "paper", "paper": "scissors", "scissors": "rock"}[predicted]

def get_computer_choice():
    return predict_user_move()

def determine_winner(user, comp):
    if user == comp:
        return "tie"
    wins = {("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")}
    return "user" if (user, comp) in wins else "computer"

def main():
    print("Smart Rock-Paper-Scissors! (type 'quit' to exit)")
    user_score = comp_score = 0
    while True:
        user = get_user_choice()
        if user in ("quit", "q"):
            break
        comp = get_computer_choice()
        print(f"You chose {user}, computer chose {comp}.")
        result = determine_winner(user, comp)
        recent_moves.append(user)
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            user_score += 1
            print("You win this round!")
        else:
            comp_score += 1
            print("Computer wins this round!")
        print(f"Score → You: {user_score}, Computer: {comp_score}\n")
    print("Final Score:", f"You {user_score} — Computer {comp_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
