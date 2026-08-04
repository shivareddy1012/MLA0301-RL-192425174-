import numpy as np

# States
states = ["Start", "Middle", "Winning", "Losing"]

# Actions
actions = ["Attack", "Defend"]

# Transition probabilities
transition = {
    ("Start", "Attack"): [0.8, 0.2, 0.0, 0.0],
    ("Start", "Defend"): [0.5, 0.5, 0.0, 0.0],

    ("Middle", "Attack"): [0.0, 0.2, 0.7, 0.1],
    ("Middle", "Defend"): [0.0, 0.6, 0.2, 0.2]
}

# Rewards
reward = {
    "Winning": 100,
    "Losing": -100,
    "Middle": 10,
    "Start": 0
}

gamma = 0.9

value = {s: 0 for s in states}

for i in range(10):
    new_value = value.copy()

    for state in ["Start", "Middle"]:
        best = -999

        for action in actions:

            probs = transition[(state, action)]

            total = 0

            for j in range(len(states)):
                next_state = states[j]
                total += probs[j] * (
                    reward[next_state] + gamma * value[next_state]
                )

            if total > best:
                best = total

        new_value[state] = best

    value = new_value

print("Optimal State Values")

for s in states:
    print(s, ":", round(value[s], 2))
