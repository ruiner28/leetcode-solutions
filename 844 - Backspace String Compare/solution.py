class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(string):
            stack = []
            for i in string:
                if i != '#':
                    stack.append(i)
                elif stack:
                    stack.pop()
            return "".join(stack)            
        return process(s) == process(t)          