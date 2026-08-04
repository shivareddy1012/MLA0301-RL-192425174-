import numpy as np

q = np.zeros((4,4))

reward = 10

alpha = 0.5
gamma = 0.9

state = 0
action = 1
next_state = 1

q[state][action] = q[state][action] + alpha * (
reward + gamma * np.max(q[next_state]) - q[state][action]
)

print("Updated Q Table\n")

print(q)
