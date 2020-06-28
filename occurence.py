import collections
def occurences(nums):
    result = dict()
    for num in nums:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    
    sorted(result.items(), key=lambda KV:KV[1], reverse=True)

nums1 = [8,2,4,5,7,8,4,2,6,8]
occurences(nums1)