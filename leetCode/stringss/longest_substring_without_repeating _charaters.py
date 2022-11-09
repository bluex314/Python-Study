# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lenght_of_longest_substring_without_repeating(s):
    if len(s) == 0:
        return 0
    sh = {}
    max_count = 1
    sh[s[0]] = sh.get(s[0], 0)
    for i in range(1, len(s)):
        if s[i] in sh:
            sh.pop(s[i])
            max_count = max_count if max_count > len(sh) else len(sh)
        else:
            sh[s[i]] = sh.get(s[i], 0)
            max_count = max_count if max_count > len(sh) else len(sh)
    return max_count


if __name__ == '__main__':
    s = 'pwwkew'
    ans = lenght_of_longest_substring_without_repeating(s)
    print(ans)