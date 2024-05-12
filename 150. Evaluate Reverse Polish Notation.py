class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["/", "*", "+", "-"]
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                res = 0
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if token == "+":
                    res = num1 + num2
                elif token == "-":
                    res = num2 - num1
                elif token == "*":
                    res = num1 * num2
                elif token == "/":
                    res = int(num2/num1)
                stack.append(res)
        return stack.pop()