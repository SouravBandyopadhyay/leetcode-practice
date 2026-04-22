class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            
            elif s[i] == ')' and stack and stack[len(stack)-1] == '(':
                stack.pop()
            
            elif s[i] == ']' and stack and stack[len(stack)-1] == '[':
                stack.pop()
            
            elif s[i] == '}' and stack and stack[len(stack)-1] == "{":
                stack.pop()
            
            else:
                stack.append(s[i])
        
        return len(stack)==0