class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            complimentary = target - num
            if complimentary in hashmap:
                return [hashmap[complimentary],i]
            
            hashmap[num] = i

        return []