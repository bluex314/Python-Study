# https://leetcode.com/problems/
# /

def maximum_subarray(nums):
    max_sum = nums[0]
    csum = 0
    for i, num in enumerate(nums):
        if csum < 0:
            csum = 0
            out = []
        csum += num
        max_sum = max(max_sum, csum)
    return max_sum, out

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-15,4, 12]
    ans = maximum_subarray(nums)
    print(ans)
