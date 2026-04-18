class Solution:
    def isValid(self, s: str) -> bool:

        pair = {')': '(', ']': '[', '}': '{'}


        stack = []


        for ch in s:
            if ch in pair.values(): # opening bracket
                stack.append(ch)
            elif ch in pair: # closing bracket
                if not stack or stack.pop() != pair[ch]:
                    return False
            else:
                return False
        
        return not stack