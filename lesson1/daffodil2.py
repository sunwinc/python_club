while True:
    x1 = input("please enter a number x1=")
    x2 = input("please enter a number x2=")
    quit = ('q','Q')
    if x1 in quit or x2 in quit:
        break
    else:
        try:
            x1, x2 = int(x1), int(x2)
        except:
            print("please enter only numbers")
            continue
    if x1>x2:
        x1,x2=x2,x1
        pass
    for n in range(x1,x2):
        i=n/100
        j=n/10%10
        k=n%10
        if i*100+j*10+k==i**3+j**3+k**3:
            print(n)
        pass