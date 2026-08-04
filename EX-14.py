algorithms = {
    "A2C": 15,
    "A3C": 11
}

print("Smart Elevator Scheduling\n")

for algo in algorithms:
    print(algo, "Waiting Time =", algorithms[algo], "seconds")

best = min(algorithms, key=algorithms.get)

print("\nBest Algorithm :", best)
print("Minimum Waiting Time :", algorithms[best], "seconds")
