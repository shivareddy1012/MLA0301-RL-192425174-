returns = {
    "Room1":[5,6,7],
    "Room2":[4,5,6],
    "Room3":[9,8,10]
}

print("Monte Carlo State Values\n")

for room in returns:

    value = sum(returns[room]) / len(returns[room])

    print(room,"=",round(value,2))
