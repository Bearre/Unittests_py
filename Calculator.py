class Calculator:
    # empty constructor
    def __init__(self):
        pass

    def add(self, x1, x2):
        return x1 + x2

    def multiply(self, x1, x2):
        return x1 * x2

    def subtract(self, x1, x2):
        return x1 - x2

    def divide(self, x1, x2):
        if x2 != 0:
            return x1 / x2

    def divide_1(self, x1, x2):
        if x2 == 0:
            raise ZeroDivisionError(f"Знаменатель равен ({x2})")
        else:
            return x1 // x2

    def sqrt(self, x):
        return x**0.5

    def pow(self, x1, x2):
        return x1**x2


if __name__ == "__main__":
    Calculator()
