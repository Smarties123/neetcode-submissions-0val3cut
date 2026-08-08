class Solution:
    def isValid(self, s: str) -> bool:

        Parentheses_map = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for char in s:
            if char in Parentheses_map:
                stack.append(char)
            else:
                if not stack or Parentheses_map[stack.pop()] != char:
                    return False
        
        return len(stack) == 0
