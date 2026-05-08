class Solution:
    def simplifyPath(self, path: str) -> str:
        component = path.split('/')
        stack = []

        for comp in component:
            if comp == "" or comp == ".":
                continue
            
            elif comp == "..":
                if stack:
                    stack.pop()
            
            else:
                stack.append(comp)
        
        return '/'+'/'.join(stack)