class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif c ==')':
                if stack:
                    stack.pop()
                else:
                    count += 1
        count += len(stack)
        return count