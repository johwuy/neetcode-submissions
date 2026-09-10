class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = list()
        mapping = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        for char in s:
            if char in mapping:
                if len(stack) > 0 and mapping[char] == stack[-1]:
                    stack.pop()
                    continue
                return False
            stack.append(char)
        return len(stack) == 0