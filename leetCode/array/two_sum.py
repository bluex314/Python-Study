# https://leetcode.com/problems/two-sum/

def two_sum(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        remaining = target-value
        if remaining in seen:
            print(i, seen[remaining])
            return i, seen[remaining]
        seen[value] = i


if __name__ == '__main__':
    nums = [3, 2 ,4]
    target = 6
    print(two_sum(nums, target))
