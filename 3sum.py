def threesum(nums):
    nums.sort()
    n = len(nums)
    result = []
    for i in range(n-2):
        if i >= 0 and nums[i - 1] != nums[i]:
            x = nums[i]
            l = i+1
            r = n-1
            while l < r:
                if x + nums[l] + nums[r] == 0:
                    result.append([x, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif x + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
    return result

print(threesum([-1,0,1,2,-1,-4]))