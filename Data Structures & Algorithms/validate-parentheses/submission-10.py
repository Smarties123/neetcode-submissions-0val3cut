class Solution:
    def isValid(self, s: str) -> bool:
        closing_to_opening = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in closing_to_opening.values():  # opening brackets
                stack.append(ch)
            else:  # closing brackets
                if not stack or stack[-1] != closing_to_opening.get(ch, ''):
                    return False
                stack.pop()

        return not stack