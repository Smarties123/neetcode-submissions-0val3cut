class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for char in s:
            if char in bracket_map:
                # char is a closing bracket

                if not stack:
                    return False

                top = stack.pop()

                if top != bracket_map[char]:
                    return False

            else:
                # char is an opening bracket
                stack.append(char)

        return len(stack) == 0