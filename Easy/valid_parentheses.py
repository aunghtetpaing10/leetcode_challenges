class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    open_bracket = stack.pop()
                    if pairs[open_bracket] != char:
                        return False

        return not stack