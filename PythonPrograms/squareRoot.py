
c = input('please enter a number')
x = float(c)

epsilon = 0.01
step = epsilon**3
numGuesses = 0
ans = 0.0

while abs(x- ans**2) >= epsilon and ans**2 <= x:
    ans += step
    """print(ans)"""
    numGuesses += 1

print('numGuesses =', numGuesses)

if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of', x, ans)
else:
    print(ans, ' is close to squre root of', x)

