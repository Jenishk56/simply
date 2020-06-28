class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        N =len(nums)
        L = N-k
        res = nums[L:] + nums[:L]
        for i in range(N):
            nums[i] = res[i]