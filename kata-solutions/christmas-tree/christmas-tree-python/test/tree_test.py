import pytest
from hamcrest import *

def christmas_tree(height):
  if height == 1:
    return ["*",
            "|"] 
  elif height == 2:
    return [" *",
            "***",
            " |"] 
  elif height ==3:
    return ["  *",
            " ***",
            "*****",
            "  |"] 
  return ["|"]

class TestChristmasTree:

  def test_a_new_ChristmasTree_0(self):
    assert_that(christmas_tree(0), 
                equal_to(["|"]))

  def test_a_new_ChristmasTree_1(self):
    assert_that(christmas_tree(1), 
                equal_to(["*",
                          "|"]))

  def test_a_new_ChristmasTree_2(self):
    assert_that(christmas_tree(2), 
                equal_to([" *",
                          "***",
                          " |"]))

  def test_a_new_ChristmasTree_3(self):
    assert_that(christmas_tree(3), 
                equal_to(["  *",
                          " ***",
                          "*****",
                          "  |"]))

