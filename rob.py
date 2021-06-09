def rob(nums):
    rob1 = 0
    rob2 = 0
    for num in nums:
        max_so_far = max(rob1 + num, rob2)
        rob1 = rob2
        rob2 = max_so_far
    return rob2

print(rob([1,3,7,9]))