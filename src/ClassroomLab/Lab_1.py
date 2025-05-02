class Lab:
    def GreatestCommonDivisor(self, num1: int, num2: int) -> int:
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        return num1

    def LeastCommonMultiple(self, num1: int, num2: int) -> int:
        gcd = self.GreatestCommonDivisor(num1, num2)
        multiplied = abs(num1 * num2)
        return int(multiplied / gcd)