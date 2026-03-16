class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(nums, k):
            left = 0
            freq = defaultdict(int)
            res = 0

            for right in range(len(nums)):
                if nums[right] % 2:
                    freq[right] += 1

                while len(freq) > k:
                    if nums[left] % 2:
                        freq[left] -= 1
                        if freq[left] == 0:
                            del freq[left]

                    left += 1

                res += right - left + 1

            return res

        return at_most(nums, k) - at_most(nums, k - 1)
