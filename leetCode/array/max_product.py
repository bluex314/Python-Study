# https://leetcode.com/problems/maximum-product-subarray/

# yet to work on

def max_product(nums):
    cp = 1
    mp = nums[0]
    nnp = 1

    for n in nums:
        cp *= n
        if n > 0:
            nnp *= n
        else:
            nnp = 1
        mp = max(cp, nnp, mp)
        if n == 0:
            cp = 1

    return mp


if __name__ == '__main__':
    nums = [-1, -2, -3]
    ans = max_product(nums)
    print(ans)

