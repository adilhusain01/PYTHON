def countSmaller(nums):
    def merge_sort(enumerated_nums):
        if len(enumerated_nums) <= 1:
            return enumerated_nums, [0]

        mid = len(enumerated_nums) // 2
        left_half, left_count = merge_sort(enumerated_nums[:mid])
        right_half, right_count = merge_sort(enumerated_nums[mid:])
        
        merged_nums = []
        merged_count = []
        i, j = 0, 0
        while i < len(left_half) or j < len(right_half):
            if j == len(right_half) or (i < len(left_half) and left_half[i][1] <= right_half[j][1]):
                merged_nums.append(left_half[i])
                merged_count.append(left_count[i] + j)
                i += 1
            else:
                merged_nums.append(right_half[j])
                merged_count.append(right_count[j])
                j += 1
        
        return merged_nums, merged_count

    nums = list(map(int, nums.split()))
    enumerated_nums = list(enumerate(nums))
    _, result_count = merge_sort(enumerated_nums)
    
    return result_count

nums_input = input("Enter a space-separated list of integers: ")
output = countSmaller(nums_input)
print("Counts of smaller elements to the right:", output)
