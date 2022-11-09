# https://leetcode.com/problems/minimum-window-substring/description/


def min_sub_string(s, t):
    s_hash = {}
    t_hash = {}
    min_window_string = s

    s_len = len(s)
    t_len = len(t)

    for i in range(t_len):
        t_hash[t[i]] = 1 + t_hash.get(t[i], 0)

    # checking for matching sub-string in first window
    if t_hash == s_hash:
        min_window_string = s[:t_len]
        # this will the smallest if matching
        return min_window_string

    l = 0
    r= 0

    while l < (s_len-t_len):
        # starting and ending should be in substring
        if s[l] not in t_hash:
            l += 1
            continue

        if s[r] in t_hash: # we can ignore adding rest of the characters except in t
            s_hash[s[r]] = 1 + s_hash.get(s[r], 0)
            if t_hash[s[r]] != s_hash[s[r]]:
                l += 1
                continue
            if t_hash == s_hash:
                if len(min_window_string) > len(s[:r+1]):
                    min_window_string = s[:r+1]
                if s[l] in s_hash:
                    s_hash.pop(s[l])
                l += 1
        if r < s_len:
            r += 1
    return min_window_string


if __name__ == '__main__':
    s = 'ADOBECODEBANC'
    t = 'ABC'
    ans = min_sub_string(s, t)
    print(ans)