import math

"""
Performs basic mathematical operations:
- Add(+).
- Subtract(-).
- Multiply(*).
- Divide(/).
- Power(x^).
- Square Root(√).
- n-th Root.
- Chain of mathematical operations((5+9)*54^5).
"""


class BasicCalculator:

    def add(self, x, y):
        return x+y

    def sub(self, x, y):
        return x-y

    def mul(self, x, y):
        return x*y

    def div(self, x, y):
        return x/y

    def power(self, x, y):
        return pow(x, y)

    def square_root(self, x):
        # Remeber: Throw an exception  if x < 0
        return math.sqrt(x)

    def nth_root(self, x, y):
        return pow(x, (1/y))

    # this function takes a string of operations, ex:"900/(6*12)+(85*96)"
    def string_of_operations(self, exp):
        priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        operators = {'+', '-', '*', '/', '(', ')', '^'}
        stack, numbers, num, i = [], [], '', 0

        while True:
            if exp[i] not in operators:
                num = num + exp[i]
                if i == len(exp) - 1:
                    numbers.append(int(num))
            else:
                if num != '':
                    numbers.append(int(num))
                    num = ''

                if not stack or exp[i] == '(':
                    stack.append(exp[i])
                elif exp[i] == ')':
                    while stack[-1] != '(':
                        operator, op2, op1 = stack.pop(), numbers.pop(), numbers.pop()
                        numbers.append(self.operations(operator, op1, op2))
                    stack.pop()
                elif priority[exp[i]] > priority[stack[len(stack) - 1]]:
                    stack.append(exp[i])
                elif priority[exp[i]] <= priority[stack[-1]]:
                    operator, op2, op1 = stack.pop(), numbers.pop(), numbers.pop()
                    numbers.append(self.operations(operator, op1, op2))
                    stack.append(exp[i])

            if i == len(exp) - 1:
                while stack:
                    operator, op2, op1 = stack.pop(), numbers.pop(), numbers.pop()
                    numbers.append(self.operations(operator, op1, op2))
                return numbers.pop()
            i += 1

    # helper function for STRING OF OPERATIONS function
    def operations(self, operator, op1, op2):
        if operator == '+':
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        elif operator == '*':
            return op1 * op2
        elif operator == '/':
            return op1 / op2
        elif operator == '^':
            return pow(op1, op2)

    