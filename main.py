import random

choices = ["snake", "water", "gun"]
win_map = {"snake": "water", "water": "gun", "gun": "snake"}

def get_result(You, AI):
    if You == AI:
        return "Draw"
    elif win_map[You] == AI:
        return "You win"
    else:
        return "AI wins"

score = {"You": 0, "AI": 0, "Draws": 0}

for _ in range(5):
    You = input("Choose snake, water, or gun: ").lower()
    if You not in choices:
        print("Invalid choice")
        continue
    AI = random.choice(choices)
    result = get_result(You, AI)
    print(f"You chose {You}, AI chose {AI} → {result}")
    if result == "You win":
        score["You"] += 1
    elif result == "AI wins":
        score["AI"] += 1
    else:
        score["Draws"] += 1

print(f"Final Score → You: {score['You']}, AI: {score['AI']}, Draws: {score['Draws']}")
