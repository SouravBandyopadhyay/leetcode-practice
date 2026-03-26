class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        |2-6| = 4
        |4-6| = 2 - 4 (cuz its smaller)
        |5-6| = 1 - 5
        |8-6| = 2
        '''
        left, right = 0 , len(arr) - 1

        while right - left>=k:
            if abs(x-arr[left])>abs(x-arr[right]):
                left +=1
            else:
                right -=1
            
        return arr[left:right+1]