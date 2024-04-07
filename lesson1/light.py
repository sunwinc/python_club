n = int(input("How many light: "))
k = int(input("How many people: "))

lights = [False]*n

print(lights)

for i in range(1, k+1):
    for j in range(1, n+1):
        if (j%i == 0):
            lights[j-1] = not lights[j-1]
    print(lights)

for i in range(0, n):
    if lights[i]:
        print(i+1,end=" ")
print()