def ptgraph1(n):
    for i in range(1, n+1):
        # print(" "*(2*n-2*i), end="")
        for j in range(0, i):
            print("* ", end="")
        print()

