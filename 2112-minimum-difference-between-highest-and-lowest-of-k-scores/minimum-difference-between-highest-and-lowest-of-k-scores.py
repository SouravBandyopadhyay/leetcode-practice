class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0 , k-1
        res = float('inf')
        n = len(nums)
        while right<n:
            res = min(res,nums[right]-nums[left])
            left +=1
            right +=1
        
        return res