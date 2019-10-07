# -*- coding: utf-8 -*-

def bigodd():
    num = []
    a = []
    bigest = 0

    i = 10
    while i !=0:
        data = int(input('请输入整数： '))
        num.append(int(data))
        i = i -1

    for j in range(len(num)):
        if num[j] %2 != 0:
            a.append(num[j])

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


    
