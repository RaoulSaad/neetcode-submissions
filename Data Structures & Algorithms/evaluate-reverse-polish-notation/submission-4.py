from collections import deque
class Solution:
    operators = ['+', '-', '*', '/']
    def evalRec(self, stack) -> int:
        if stack[-1] not in self.operators:
            return stack.pop()
        else:
            operator = stack.pop()
            op2 = self.evalRec(stack)
            op1 = self.evalRec(stack)
            if operator == '+':
                return op1 + op2
            elif operator == '-':
                return op1 - op2
            elif operator == '*':
                return op1 * op2
            else:
                return int(op1/op2)
            

    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        
        for token in tokens:
            if token in self.operators:
                stack.append(token)
                # match token:
                #     case '+':
                #         stack.append(token)
                #     case '-':
                #         stack.append(token)
                #     case '*':
                #         print('We here')
                #         op2 = self.evalRec(stack)
                #         print(op2)
                #         op1 = self.evalRec(stack)
                #         print(op1)
                #         stack.append(op1 * op2)
                #     case '/':
                #         print('We there')
                #         op2 = self.evalRec(stack)
                #         print(op2)
                #         op1 = self.evalRec(stack)
                #         print(op1)
                #         print(op1)
                #         stack.append(op1 // op2)
            else:
                stack.append(int(token))
        output = 0
        while len(stack) > 1:
            stack.append(self.evalRec(stack))


        return stack[0]

