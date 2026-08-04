algorithms = {
    "PPO": 96,
    "TRPO": 91
}

print("Humanoid Robot Stability\n")

for algo in algorithms:
    print(algo, "Stability Score =", algorithms[algo])

best = max(algorithms, key=algorithms.get)

print("\nBest Algorithm :", best)
print("Highest Stability Score :", algorithms[best])
