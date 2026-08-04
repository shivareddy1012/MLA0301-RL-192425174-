states = ["Loading", "Moving", "Delivery"]

actions = {
    "Loading": "Move",
    "Moving": "Deliver",
    "Delivery": "Finish"
}

rewards = {
    "Loading": -2,
    "Moving": 5,
    "Delivery": 20
}

print("Warehouse Robot Policy\n")

for state in states:
    print(state, "->", actions[state])

print("\nRewards")

for state in rewards:
    print(state, ":", rewards[state])
