# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def max_profit(nums):
    max = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i] and nums[j]-nums[i] > max:
                max = nums[j]-nums[i]
    return max

# using two pointer algo
def max_profit_two(price):
    l, r = 0, 1
    maxP = 0

    while r < len(price):
        if price[l] < price[r]:
            currentP = price[r]-price[l]
            maxP = max(maxP, currentP)
        else:
            l = r
        r += 1
    return maxP


if __name__ == '__main__':
    nums = [7, 1, 3, 0, 3, 6]
    print(max_profit_two(nums))