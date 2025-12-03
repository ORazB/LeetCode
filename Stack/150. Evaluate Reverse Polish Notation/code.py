from typing import List

# Time Compleixty: O(n)
# Space Complexity: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      
        # What is Reverse Polish Notation?
        # Reverse Polish Notation is a mathematical notation in which every operator follows all of its operands
        # http://en.wikipedia.org/wiki/Reverse_Polish_notation
        
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                # Order matters in subtraction
                second = stack.pop()
                first = stack.pop()

                stack.append(first - second)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                # Order matters in division
                second = stack.pop()
                first = stack.pop()

                stack.append(int(first / second))
            else:
                # Keep adding numbers until it found an operator
                stack.append(int(token))
        return stack[0]