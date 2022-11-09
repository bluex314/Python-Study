# https://leetcode.com/problems/longest-palindromic-substring/

# n ** 2
def longestPalindrome(str):
    res = ""
    resLen = 0

    for i in range(len(str)):
        # odd length
        l, r = i, i
        res, resLen = check(l, r, str, res, resLen)

        # even length
        l, r = i, i + 1
        res, resLen = check(l, r, str, res, resLen)

    return res


def check(l, r, str, res, resLen):
    while l >= 0 and r < len(str) and str[l] == str[r]:
        if (r - l + 1) > resLen:
            res = str[l:r + 1]
            resLen = r - l + 1
        l -= 1
        r += 1
    return res, resLen



if __name__ == '__main__':
    str = 'krbabad'
    ans = longestPalindrome(str)
    print(ans)