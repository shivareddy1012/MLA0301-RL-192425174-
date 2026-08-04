import random

ads = ["Ad A", "Ad B", "Ad C"]

rewards = [5, 8, 6]

epsilon = 0.2

for i in range(10):

    if random.random() < epsilon:
        choice = random.randint(0, 2)
        print("Exploration ->", ads[choice])

    else:
        best = rewards.index(max(rewards))
        print("Exploitation ->", ads[best])

print("\nBest Advertisement =", ads[rewards.index(max(rewards))])
