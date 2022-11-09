def binary_search(number, nums, mid_index=0):
    left_index = 0
    right_index = len(nums) -1
    mid_index = mid_index
    index = []

    while left_index <= right_index:
        mid_index = (right_index + left_index) // 2
        mid_number = nums[mid_index]

        if number == mid_number:
            index.append(mid_index)
            if right_index != left_index:
                index + [binary_search(number, nums[:mid_number])]
                index + [binary_search(number, nums[mid_index:right_index-mid_index])]
            return index

        if number < mid_number:
            right_index = mid_index - 1

        if number > mid_number:
            left_index = mid_index + 1


    return -1


if __name__=="__main__":
    nums = [1,1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number_to_search = 1

    index = binary_search(number_to_search, nums)
    print(index)