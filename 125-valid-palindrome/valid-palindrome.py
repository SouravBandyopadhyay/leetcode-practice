class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0 , len(s) -1

        def is_alphanumeric(str):
            return str.isalnum()
        
        while left<right:
            while left<right and not is_alphanumeric(s[left]):
                left+=1
            
            while left<right and not is_alphanumeric(s[right]):
                right -=1
            
            if s[left].lower() != s[right].lower():
                return False
        
            left +=1
            right -=1
    
        return True
