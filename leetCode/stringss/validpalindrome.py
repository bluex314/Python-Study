# https://leetcode.com/problems/valid-palindrome/

def is_palindrome(s):
    l = 0
    r = len(s)-1
    while l <= r:
        if not isalnumer(s[l]):
            l += 1
            continue
        if not isalnumer(s[r]):
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

def isalnumer(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

if __name__ == '__main__':
    s = 'A man, a plan, a canal: Panama'
    ans = is_palindrome(s)
    print(ans)