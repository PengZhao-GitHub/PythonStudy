
def isPalindrome(s):
    """Assumes s is a str
        Return True if letters in s from a palindrome; False
        otherwise. Non-letters and capitalization are ignored."""

    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuwxyz':
                letters += c
        return letters

    def isPal(s):
        print(' isPal called with', s)
        if len(s) <= 1:
            print(' About to return True from base case')
            return True
        else:
            teanswer = s[0] == s[-1] and isPal(s[1:-1])
            print(' About to return', answer, 'for', s)
            return answer


    return isPal(toChars(s))


def testIsPalindrome():
    print('Try dogGod')
    print(isPalindrome('dogGod'))
    print('Try doGood')
    print(isPalindrome('doGood'))


