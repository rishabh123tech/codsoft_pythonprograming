import random

c = ["rock", "paper", "scissors"]
s = {"player": 0, "computer": 0, "tie": 0}

print("Rock-Paper-Scissors Game")
print("Type rock, paper, or scissors. Type q to quit.\n")

while True:
    u = input("Your choice: ").strip().lower()
    if u == "q":
        break
    if u not in c:
        print("Invalid input. Try again.")
        continue

    comp = random.choice(c)
    print(f"Computer chose {comp}")

    if u == comp:
        r = "tie"
        print("It's a tie!")
    elif (u == "rock" and comp == "scissors") or \
         (u == "paper" and comp == "rock") or \
         (u == "scissors" and comp == "paper"):
        r = "player"
        print("You win ")
    else:
        r = "computer"
        print("Computer wins ")

    s[r] += 1
    print(f"Score - You: {s['player']}  Computer: {s['computer']}  Ties: {s['tie']}\n")

print("Thanks for playing!")
