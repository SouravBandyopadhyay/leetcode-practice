class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        slow = 0
        n = len(nums)
        for fast in range(n):
            if nums[fast]%2 == 0:
                nums[slow], nums[fast] = nums[fast],nums[slow]
                slow +=1
        
        return nums
