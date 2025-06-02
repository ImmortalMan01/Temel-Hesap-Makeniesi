import unittest
import math

# Assuming calculator.py is in the same directory or accessible via PYTHONPATH
# For testing, it's common to adjust sys.path or structure as a package.
# For this environment, let's assume direct import works if they are in the same folder.
from calculator import (
    add, subtract, multiply, divide,
    power, square_root, log_natural, log_base10,
    sine, cosine, tangent
)

class TestCalculator(unittest.TestCase):

    # --- Test Basic Arithmetic Operations ---
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(5, 10), -5)
        self.assertAlmostEqual(subtract(2.5, 1.5), 1.0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(-2, -3), 6)
        self.assertEqual(multiply(10, 0), 0)
        self.assertAlmostEqual(multiply(1.5, 2.0), 3.0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertAlmostEqual(divide(1, 3), 1/3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    # --- Test Advanced Mathematical Operations ---
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(10, -1), 0.1)
        self.assertAlmostEqual(power(4, 0.5), 2.0)
        self.assertAlmostEqual(power(-2, 2), 4.0) # (-2)^2 = 4
        self.assertAlmostEqual(power(-2, 3), -8.0) # (-2)^3 = -8

    def test_square_root(self):
        self.assertEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))
        self.assertEqual(square_root(0), 0)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            square_root(-4)

    def test_log_natural(self):
        self.assertAlmostEqual(log_natural(math.e), 1)
        self.assertAlmostEqual(log_natural(1), 0)
        self.assertAlmostEqual(log_natural(10), math.log(10))

    def test_log_natural_non_positive(self):
        with self.assertRaises(ValueError):
            log_natural(0)
        with self.assertRaises(ValueError):
            log_natural(-1)

    def test_log_base10(self):
        self.assertAlmostEqual(log_base10(100), 2)
        self.assertAlmostEqual(log_base10(1), 0)
        self.assertAlmostEqual(log_base10(50), math.log10(50))

    def test_log_base10_non_positive(self):
        with self.assertRaises(ValueError):
            log_base10(0)
        with self.assertRaises(ValueError):
            log_base10(-1)

    # --- Test Trigonometric Functions (angles in radians) ---
    def test_sine(self):
        self.assertAlmostEqual(sine(0), 0)
        self.assertAlmostEqual(sine(math.pi / 2), 1)
        self.assertAlmostEqual(sine(math.pi), 0)
        self.assertAlmostEqual(sine(3 * math.pi / 2), -1)
        self.assertAlmostEqual(sine(2 * math.pi), 0)

    def test_cosine(self):
        self.assertAlmostEqual(cosine(0), 1)
        self.assertAlmostEqual(cosine(math.pi / 2), 0)
        self.assertAlmostEqual(cosine(math.pi), -1)
        self.assertAlmostEqual(cosine(3 * math.pi / 2), 0)
        self.assertAlmostEqual(cosine(2 * math.pi), 1)

    def test_tangent(self):
        self.assertAlmostEqual(tangent(0), 0)
        self.assertAlmostEqual(tangent(math.pi / 4), 1)
        # self.assertAlmostEqual(tangent(3 * math.pi / 4), -1) # tan(pi - pi/4) = -tan(pi/4) = -1

    def test_tangent_undefined(self):
        with self.assertRaises(ValueError): # tan(pi/2)
            tangent(math.pi / 2)
        with self.assertRaises(ValueError): # tan(3pi/2)
            tangent(3 * math.pi / 2)
        # Test a value very close to pi/2
        with self.assertRaises(ValueError):
            tangent(math.pi/2 - 1e-9) # Should be a large number, but our check is for cos(x) being close to 0
        with self.assertRaises(ValueError):
            tangent(math.pi/2 + 1e-9)


    # --- Test Input Type Validation ---
    # Using a helper method to avoid repetition for type tests
    def _test_type_error_for_binary_op(self, func):
        with self.assertRaisesRegex(TypeError, "Inputs must be numeric"):
            func("a", 5)
        with self.assertRaisesRegex(TypeError, "Inputs must be numeric"):
            func(5, "b")
        with self.assertRaisesRegex(TypeError, "Inputs must be numeric"):
            func("a", "b")
        # Test with list, dict as well for thoroughness if desired
        with self.assertRaisesRegex(TypeError, "Inputs must be numeric"):
            func([1], 5)
        with self.assertRaisesRegex(TypeError, "Inputs must be numeric"):
            func(5, {"val": 1})


    def _test_type_error_for_unary_op(self, func):
        with self.assertRaisesRegex(TypeError, "Input must be numeric"):
            func("a")
        with self.assertRaisesRegex(TypeError, "Input must be numeric"):
            func([1,2])
        with self.assertRaisesRegex(TypeError, "Input must be numeric"):
            func({"val":1})


    def test_add_type_error(self):
        self._test_type_error_for_binary_op(add)

    def test_subtract_type_error(self):
        self._test_type_error_for_binary_op(subtract)

    def test_multiply_type_error(self):
        self._test_type_error_for_binary_op(multiply)

    def test_divide_type_error(self):
        self._test_type_error_for_binary_op(divide)

    def test_power_type_error(self):
        self._test_type_error_for_binary_op(power)

    def test_square_root_type_error(self):
        self._test_type_error_for_unary_op(square_root)

    def test_log_natural_type_error(self):
        self._test_type_error_for_unary_op(log_natural)

    def test_log_base10_type_error(self):
        self._test_type_error_for_unary_op(log_base10)

    def test_sine_type_error(self):
        self._test_type_error_for_unary_op(sine)

    def test_cosine_type_error(self):
        self._test_type_error_for_unary_op(cosine)

    def test_tangent_type_error(self):
        self._test_type_error_for_unary_op(tangent)


if __name__ == '__main__':
    unittest.main()
