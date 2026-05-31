class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        stack = []
        for char in s:
            stack .append(char)

        table = {
            '}': '{',
            ']': '[',
            ')': '(',
        }

        while True:
            top = stack.pop()
            if top not in table or len(stack) == 0:
                return False
            if table[top] == stack[0]:
                stack.pop(0)
            elif table[top] == stack[-1]:
                stack.pop()
            else:
                return False
            if len(stack) == 0:
                return True
            
        