# https://leetcode.com/problems/product-of-array-except-self/

def product_of_array_except_self(nums):
    out = []
    prefix = 1
    nums_len = len(nums)
    # prefix array left to right run
    for i in range(nums_len):
        out.append(prefix)
        prefix *= nums[i]

    postfix = 1
    index = 0
    # right to left run
    # postfix with answer
    for i in range(nums_len):
        index = nums_len - i - 1
        out[index] *= postfix
        postfix *= nums[index]

    return out


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    ans = product_of_array_except_self(nums)
    print(ans)
