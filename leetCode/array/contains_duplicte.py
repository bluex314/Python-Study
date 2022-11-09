# https://leetcode.com/problems/contains-duplicate/


def contains_duplicate(nums):
    s = {}
    for n in nums:
        if n in s:
            return True
        s[n] = n
    return False

if __name__ == '__main__':
    nums = [1,23,4,5, 1]
    ans = contains_duplicate(nums)
    print(ans)