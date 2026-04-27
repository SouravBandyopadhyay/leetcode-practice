class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0]*n

        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = i - prev_day
            
            stack.append(i)
        
        return res