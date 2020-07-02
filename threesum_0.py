 def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(0, n-1):
            x = nums[i]
            l = i+1
            r = n-1
            while l<r:
                if x + nums[l] + nums[r] == 0:
                    result.append([x, nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif x + nums[l] + nums[r] < 0: 
                    l += 1
                else:
                    r -= 1
                    
        return result