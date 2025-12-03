class Solution:
    def isValidBracket(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == '[':
                stack.append(char)
            elif char == '{':
                stack.append(char)
            else:
                stack.pop()

        return True if not stack else False

if __name__ == '__main__':
    s = Solution()
    str = "()[]{}"
    print(s.isValidBracket(str))