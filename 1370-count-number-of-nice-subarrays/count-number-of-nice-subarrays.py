class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        odd_count = 0 
        res = 0

        for num in nums:
            if num%2:
                odd_count += 1
            
            res += prefix[odd_count - k ]

            prefix[odd_count] += 1
        
        return res
