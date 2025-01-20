class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        components = path.split('/')

        for i in components:
            if i == '..':
                if stack:
                    stack.pop()
            elif i == '.' or not i:
                continue
            else:
                stack.append(i)            

        new_path = '/' + '/'.join(stack)
        return new_path