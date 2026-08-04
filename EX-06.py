import gymnasium as gym
import numpy as np
import random

env = gym.make("FrozenLake-v1", is_slippery=False)

q_table = np.zeros((env.observation_space.n, env.action_space.n))

alpha = 0.8
gamma = 0.95
epsilon = 0.1

episodes = 1000

for episode in range(episodes):

    state, info = env.reset()
    done = False

    while not done:

        if random.uniform(0,1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state])

        next_state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated

        q_table[state][action] = q_table[state][action] + alpha * (
            reward + gamma * np.max(q_table[next_state]) - q_table[state][action]
        )

        state = next_state

print("Learned Q-Table")
print(q_table)
