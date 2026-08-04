import numpy as np
import random

rooms = 5
actions = ["Left", "Right"]

Q = np.zeros((rooms, 2))

alpha = 0.1
gamma = 0.9
epsilon = 0.2

episodes = 500

for episode in range(episodes):

    state = 0

    while state != 4:

        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, 1)
        else:
            action = np.argmax(Q[state])

        if action == 0:
            next_state = max(0, state - 1)
        else:
            next_state = min(4, state + 1)

        reward = 10 if next_state == 4 else -1

        Q[state][action] += alpha * (
            reward +
            gamma * np.max(Q[next_state]) -
            Q[state][action]
        )

        state = next_state

print("Q Table")
print(Q)
