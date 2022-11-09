# https://leetcode.com/problems/ransom-note/

def ransom_note(ransomNote, magazine):
    h = {}
    for v in magazine:
        h[v] = 1 + h.get(v, 0)

    for rw in ransomNote:
        if rw not in h:
            return False
        h[rw] -= 1
        if h[rw] == 0:
            h.pop(rw)
    return True


if __name__ == '__main__':
    ransomNote = 'aa'
    magazine = 'ab'
    ans = ransom_note(ransomNote, magazine)
    print(ans)