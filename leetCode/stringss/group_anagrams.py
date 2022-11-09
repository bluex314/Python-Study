# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict


def group_anagrams(strs):
    anagram_group = []
    anagram_dict = {}
    for words in strs:
        sw = ''.join(sorted(words))
        if sw not in anagram_dict:
            anagram_dict[sw] = [words]
        else:
            anagram_dict[sw].append(words)

    for key in anagram_dict:
        anagram_group.append(anagram_dict[key])

    return anagram_group


def anagram(strs):
    #res = defaultdict(list)
    res = {}

    for s in strs:
        count = [0] * 26
        
        for c in s:
            count[ord(c) - ord('a')] += 1

        res[tuple(count)] = [s] + res.get(tuple(count),[])

    return res.values()


if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]

    ans = anagram(strs)
    print(ans)