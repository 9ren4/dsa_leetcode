class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        value = 0
        second_round = 0
        for number in tokens:
            if number != '*' and number != '+' and number != '-' and number != '/':
                stack.append(int(number))
            else:
                b = stack.pop()
                a = stack.pop()
                if number == '+':
                    stack.append(a+b)
                if number == '-':
                    stack.append(a-b)
                if number == '*':
                    stack.append(a*b)
                if number == '/':
                    stack.append(int(a/b))
            
        return stack[-1]