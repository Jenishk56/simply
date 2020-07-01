def partition(nums: list):
    n = sum(nums)
    if n % 2 != 0:
        return 0
    target = n // 2
    dp = [1] + [0] * target

    for n in nums:
        for i in range(target, n-1, -1):
            dp[i] = dp[i] or dp[i-n]

    return dp[target]

print(partition([1,5,11,5]))
    