import unittest
from approvaltests.approvals import verify
from approvaltests.combination_approvals import verify_all_combinations
from calculator import Calculator

class CalculatorTest(unittest.TestCase):

  def test_add_simple(self):
    # ARRANGE
    x: int = 1
    y: int = 2;
    # ACT
    result = Calculator.addNumbers(x, y)
    # APPROVE
    verify(result)

  def test_add_combinatorial(self):
    verify_all_combinations( Calculator.addNumbers, [[1,2], [4,3]])

if __name__ == "__main__":
    unittest.main()
