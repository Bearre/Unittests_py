import unittest
from Calculator import Calculator


class CalculatorBasicTests(unittest.TestCase):
    # Фикстура, до теста
    def setUp(self) -> None:
        """ Set up """
        self.calculator = Calculator()
        print("Set up for ", self.shortDescription())

    # Фикстура, после теста
    def tearDown(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        print("Set up class CalculatorBasicTest")
        print("===================================")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Tear Down class CalculatorBasicTest")
        print("===================================\n")

    def test_add(self) -> None:
        """ Тест Сложения """
        print("ID " + self.id())
        self.assertEqual(self.calculator.add(4, 7), 11)  # +
        self.assertEqual(self.calculator.add(1, -1), 0)  # +
        self.assertEqual(self.calculator.add(-33, 2), -31)  # +
        self.assertEqual(self.calculator.add(2, 9), 11)  # +

    def test_subtract(self) -> None:
        """ Тест Вычитания """
        print("ID " + self.id())
        self.assertEqual(self.calculator.subtract(10, 5), 5)  # -

    def test_multiply(self) -> None:
        """ Тест умножения """
        print("ID " + self.id())
        self.assertEqual(self.calculator.multiply(3, 7), 21)  # *
        self.assertEqual(self.calculator.multiply(2, 1), 2)  # *
        self.assertEqual(self.calculator.multiply(8, 8), 64)  # *

    def test_divide(self) -> None:
        """ Тест деления """
        print("ID " + self.id())
        self.assertEqual(self.calculator.divide(10, 2), 5)  # /

    def test_negative_values(self) -> None:
        """ Тест отрицательных значений """
        print("ID " + self.id())
        self.assertEqual(self.calculator.add(-2, -2), -4)  # /
        self.assertEqual(self.calculator.subtract(-2, -2), 0)  # /
        self.assertEqual(self.calculator.multiply(-2, -2), 4)  # /
        self.assertEqual(self.calculator.divide(-2, -2), 1)  # /

    @unittest.skipIf(True, "Temporary skip test_zeros")
    def test_zeros(self) -> None:
        """ Тест нулей """
        print("ID " + self.id())
        self.assertEqual(self.calculator.add(0, 0), 0)  # /
        self.assertEqual(self.calculator.subtract(0, 0), 0)  # /
        self.assertEqual(self.calculator.multiply(0, 0), 0)  # /
        self.assertEqual(self.calculator.divide(0, 0), None)  # /

    @unittest.skip("Temporary skip test_divide_1")
    def test_divide_1(self) -> None:
        print("ID " + self.id())
        self.assertEqual(self.calculator.divide_1(5, 2), 2)  # /
        self.assertTrue(self.calculator.divide_1(5, 2) == 2)  # /

    def test_zero_division(self) -> None:
        """ Деление на ноль """
        print("ID " + self.id())
        with self.assertRaises(ZeroDivisionError) as e:
            self.calculator.divide_1(5, 0)
        exception = e.exception
        self.assertEqual("Знаменатель равен (0)", e.exception.args[0])


class CalculatorExTests(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()
        print("Set up for ", self.shortDescription())

    def tearDown(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        print("Set up class CalculatorExTests")
        print("===================================")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Tear Down class CalculatorExTests")
        print("===================================")

    def test_sqrt(self) -> None:
        """ Корень """
        self.assertEqual(self.calculator.sqrt(4), 2)

    def test_pow(self) -> None:
        """ Возведение в степень """
        self.assertEqual(self.calculator.pow(3,3), 27)


if __name__ == "__main__":
    unittest.main()
