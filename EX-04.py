gamma = 0.9

reward = [-1, -1, 10]

value = [0, 0, 0]

for i in range(10):
    value[2] = reward[2]
    value[1] = reward[1] + gamma * value[2]
    value[0] = reward[0] + gamma * value[1]

print("Optimal State Values")

for i in range(3):
    print("State", i, "=", round(value[i], 2))
