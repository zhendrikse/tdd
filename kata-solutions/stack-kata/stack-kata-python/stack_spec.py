from mamba import description, it, context, before
from expects import expect, be, raise_error, be_true, be_false
from stack import Stack


with description(Stack) as self:
  with context("Given a new stack"):
    with before.each:
      self.my_stack = Stack()
    
    with it("contains no elements"):
      expect(self.my_stack.is_empty()).to(be_true)

    with it("throws an exception on a pop operation"):
      expect(lambda: self.my_stack.pop()).to(raise_error(KeyError, "Stack underflow"))

    with context("with one item pushed"):
      with before.each:
        self.my_stack.push(8)

      with it("is not empty anymore"):
        expect(self.my_stack.is_empty()).to(be_false)

      with context("when element is popped"):
        with it("contains no more elements"):
          self.my_stack.pop()
          expect(self.my_stack.is_empty()).to(be_true)
    
        with it("returns the popped element"):
          expect(self.my_stack.pop()).to(be(8))

      with context("when an additional element is pushed"):
        with before.each:
          self.my_stack.push(9)

        with it("is not empty after a single pop"):
          self.my_stack.pop()
          expect(self.my_stack.is_empty()).to(be_false)
          
        with it("returns the most recent element after one pop"):
          expect(self.my_stack.pop()).to(be(9))

        with it("returns the first element after two pops"):
          self.my_stack.pop()
          expect(self.my_stack.pop()).to(be(8))



