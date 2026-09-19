"""Tests the calculator's full command-line menu."""

from pathlib import Path
import subprocess
import sys
import unittest


CALCULATOR = Path(__file__).with_name("calculator.py")


class TestCalculatorMenu(unittest.TestCase):
    def run_menu(self, answers):
        result = subprocess.run(
            [sys.executable, str(CALCULATOR)],
            input="\n".join(answers) + "\n",
            text=True,
            capture_output=True,
            timeout=5,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        return result.stdout

    def test_calculation_then_exit(self):
        output = self.run_menu(["1", "10", "5", "n"])
        self.assertIn("10.0 + 5.0 = 15.0", output)
        self.assertIn("You have successfully exited the calculator!", output)

    def test_division_by_zero_then_successful_calculation(self):
        output = self.run_menu(["4", "10", "0", "4", "10", "2", "n"])
        self.assertIn("Error: Division by zero is not allowed.", output)
        self.assertIn("10.0 / 2.0 = 5.0", output)

    def test_invalid_number_then_successful_calculation(self):
        output = self.run_menu(["1", "oops", "3", "10", "5", "n"])
        self.assertIn("Invalid input. Please enter a number.", output)
        self.assertIn("10.0 * 5.0 = 50.0", output)


if __name__ == "__main__":
    unittest.main()
