class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        intermediate = 0
        stack = []

        for token in tokens:
            match token:
                case '+':
                    stack.append(int(stack.pop()) + int(stack.pop()))
                case '-':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b-a)
                case '*':
                    stack.append(int(stack.pop()) * int(stack.pop()))
                case '/':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b/a)
                case _:
                    stack.append(int(token))
        return int(stack.pop())

        