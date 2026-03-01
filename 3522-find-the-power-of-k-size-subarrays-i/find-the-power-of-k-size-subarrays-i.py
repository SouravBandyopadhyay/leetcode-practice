class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0 
        consect_cnt = 1
        for right in range(len(nums)):
            if right > 0 and nums[right - 1] + 1 == nums[right]:
                consect_cnt +=1
            
            if right - left + 1 > k:
                if nums[left] + 1 == nums[left + 1]:
                    consect_cnt -=1
            
                left +=1

            if right - left + 1== k:
                res.append(nums[right] if consect_cnt == k else - 1)
            
        
        return res