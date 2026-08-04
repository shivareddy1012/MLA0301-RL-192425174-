algorithms = {
    "DQN": 18,
    "DDQN": 14,
    "Dueling DQN": 12,
    "PER": 10
}

print("Average Vehicle Waiting Time\n")

for algo in algorithms:
    print(algo, ":", algorithms[algo], "seconds")

best = min(algorithms, key=algorithms.get)

print("\nBest Algorithm :", best)
print("Minimum Waiting Time :", algorithms[best], "seconds")
