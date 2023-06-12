import pytest
from stack import Stack

# 
# Make the exercise here if you are using pytest
#

class TestNewStack:

  @pytest.fixture(autouse = True)
  def new_stack(self):
    self._my_stack = Stack()

  def test_a_new_stack_should_be_empty(self):
      assert self._my_stack.is_empty() == True
    
  def test_pop_on_a_new_stack_should_throw_an_exception(self):
    with pytest.raises(KeyError, match='Stack underflow') as error_info:
      self._my_stack.pop()

class TestStackWithOneElement:

  @pytest.fixture(autouse = True)
  def new_stack(self):
    self._my_stack = Stack()
    self._my_stack.push(4)

  def test_stack_should_not_be_empty(self):
      assert self._my_stack.is_empty() == False

  def test_after_a_pop_stack_should_be_empty(self):
      self._my_stack.pop()
      assert self._my_stack.is_empty() == True

  def test_pop_returns_value(self):
      value = self._my_stack.pop()
      assert value == 4

class TestStackWithTwoElements:

  @pytest.fixture(autouse = True)
  def new_stack(self):
    self._my_stack = Stack()
    self._my_stack.push(4)
    self._my_stack.push(5)

  def test_after_pop_stack_is_not_empty(self):
      self._my_stack.pop()
      assert self._my_stack.is_empty() == False

  def test_pop_returns_the_most_recently_push_value(self):
      value = self._my_stack.pop()
      assert value == 5

  def test_pop_returns_the_first_pushed_value(self):
      value = self._my_stack.pop()
      value = self._my_stack.pop()
      assert value == 4
