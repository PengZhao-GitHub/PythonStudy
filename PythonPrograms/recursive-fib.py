
#global numFibCalls

def fib(n):
    """Assumes n int >= tes0
       returns Fibonacci of n"""
    global numFibCalls
    numFibCalls += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def testFib(n):
    global numFibCalls
    numFibCalls = 0
    for i in range(n+1):
        print('fib of', i, '=', fib(i))
        print('fib called', numFibCalls, 'times.')


        


