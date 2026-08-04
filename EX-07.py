cost = [
    [0, 4, 8],
    [4, 0, 2],
    [8, 2, 0]
]

minimum = 999

route = ()

for i in range(3):
    for j in range(3):
        if i != j:
            if cost[i][j] < minimum:
                minimum = cost[i][j]
                route = (i, j)

print("Optimal Route :", route)
print("Minimum Cost :", minimum)
