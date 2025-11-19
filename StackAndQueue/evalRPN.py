from operator import add, sub, mul, truediv
from typing import List

def div(x, y):
    return int(x / y) if x * y > 0 else -(abs(x) // abs(y))

class Solution:
    op_map = {'+': add, '-': sub, '*': mul, '/': div}
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in self.op_map:
                stack.append(token)
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(str(self.op_map[token](int(op1), int(op2))))
        return stack.pop()
if __name__ == "__main__":
    tokens =  ["4", "13", "5", "/", "+"]
    print(Solution().evalRPN(tokens))
