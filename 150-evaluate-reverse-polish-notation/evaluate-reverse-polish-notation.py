class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        operator = ['+', '-', '*', '/']
        for stacking in tokens:
            if stacking in operator:
                num1 = int(result.pop())
                num2 = int(result.pop())
                if stacking == "+":
                    cal = num1 + num2
                    result.append(cal)
                if stacking == "-":
                    cal = num2 - num1
                    result.append(cal)
                if stacking == "*":
                    cal = num1 * num2
                    result.append(cal)
                if stacking == "/":
                    print(f"dividing: {num2} / {num1}")
                    cal = int(num2 / num1)
                    result.append(cal)
            else:
                result.append(int(stacking))
        return result[-1]