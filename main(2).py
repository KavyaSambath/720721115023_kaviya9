def Find_index(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    for i in range(len(nums)):
        if nums[i] > target:
            return i
        elif nums[i] < target:
            continue
    return len(nums)    

print(Find_index([1, 3, 5, 6], 5))
print(Find_index([1, 3, 5, 6], 2))
print(Find_index([1, 3, 5, 6], 7))