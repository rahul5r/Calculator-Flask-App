class Calculate:
    def __init__(self, text):
        self.text = text.strip()

    def get_nums_operators(self):
        num = ""
        nums = []
        operators = []

        for i in self.text:
            if i.isdigit() or i == '.':
                num += i
            else:
                nums.append(float(num))
                operators.append(i)
                num = ""
        if num:
            nums.append(float(num))
        nums.reverse()
        operators.reverse()
        return nums, operators

    @staticmethod
    def is_float(num):
        if '.' in str(num):
            splits = str(num).split('.')
            if splits[-1] == '0':
                return False
            return True
        return False

    def perform_calculation(self):
        nums, operators = self.get_nums_operators()
        while operators:
            operator1 = nums.pop()
            operator2 = nums.pop()
            operand = operators.pop()
            match operand:
                case '+':
                    ans = operator1+operator2
                    nums.append(ans)
                case '-':
                    ans = operator1 - operator2
                    nums.append(ans)
                case '*':
                    ans = operator1 * operator2
                    nums.append(ans)
                case '/':
                    ans = operator1 / operator2
                    nums.append(ans)
                case '^':
                    ans = operator1 ** operator2
                    nums.append(ans)
                case '%':
                    ans = operator1 % operator2
                    nums.append(ans)
                case _:
                    nums.append(None)

        if self.is_float(nums[0]):
            return round(nums[0],10)
        return int(nums[0])

"""
text = "78/2"
Cal = Calculate(text)
print(Cal.perform_calculation())
"""

