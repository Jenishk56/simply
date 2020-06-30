def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    non_zero_counter = 0
    for i in range(n):
        if nums[i] != 0:
            nums[non_zero_counter] = nums[i]
            non_zero_counter += 1
            
    for i in range(non_zero_counter, n):
        nums[i] = 0