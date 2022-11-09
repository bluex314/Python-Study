# https://leetcode.com/problems/valid-anagram/

# using hash table count
def isAnagram(s, t):
    if len(s) == len(t):
        sd = {}
        td = {}
        for i in range(len(s)):
            if s[i] in sd:
                sd[s[i]] += 1
            else:
                sd[s[i]] = 1
            if t[i] in td:
                td[t[i]] += 1
            else:
                td[t[i]] = 1
        for ch in t:
            if ch in td or ch in sd:
                if td[ch] != sd[ch]:
                    return False
        return True
    return False



if __name__ == '__main__':
    s, t = 'anagram', 'nagaram'
    ans = isAnagram(s, t)
    print(ans)