class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left,right = 0 , n-1
        res = [0]*n
        index = n-1

        while left<=right:
            left_square = nums[left]**2
            right_square = nums[right]**2
            if left_square > right_square:
                res[index] = left_square
                left +=1
            
            else:
                res[index] = right_square
                right -=1
            
            index-=1
        
        return res
        
