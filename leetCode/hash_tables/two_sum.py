# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - value
        if remaining in seen:
            return i, seen[remaining]
        seen[value] = i



if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    ans = twoSum(nums, target)
    print(ans)