def bigodd(x, y, z):
    a = []
    bigest = 0

    if x % 2 != 0:
        a.append(x)
    if y % 2 != 0:
        a.append(y)
    if z % 2 != 0:
        a.append(z)

    if len(a) != 0:
        print(a)
        bigest = a[0]
        print(len(a))
        for i in range(len(a)):
            if bigest < a[i]:
                bigest = a[i]
        print('the biggest odd is ', bigest)
    else:
        print('No odd')


    
