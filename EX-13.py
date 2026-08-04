actions = {
    "Move Forward": 2,
    "Turn Left": 3,
    "Turn Right": 4,
    "Park": 10
}

print("Rewards\n")

for action in actions:
    print(action, ":", actions[action])

best = max(actions, key=actions.get)

print("\nOptimal Action :", best)
print("Reward :", actions[best])
