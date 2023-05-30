from mamba import description, it, context, before, after
from expects import expect, equal, raise_error, have_length, be_empty, contain, contain_only, be, be_true, be_false, be_a, be_none
from example import ASampleClass

# Caveat:
#
# This piece of code is mainly intended to look up certain
# constructs, thus for the sake of conciseness, it contains 
# multiple assertions in one expectation.
#
# Normally you'll want to put at most only one or two 
# expectations together!
with description("Examples you can use in the exercises"):
  with context('when writing assertions for lists'):

    with it("can do equality matching of primitives"):
      expect(3 + 4).to(equal(7))
      expect(3 + 4).to(be(7))
      expect(0).to(equal(False))
      expect(3 + 4).not_to(equal(9))

    with it("can do equality matching of lists"):
      expect((3, 5)).to(be((3, 5)))
      expect((3, 5, [2, 4, 6])).to(equal((3, 5, [2, 4, 6])))

    with it('can use the following matchers to match lists'):
      expect(["aap", "noot", "mies"]).to(have_length(3))
      expect([]).to(be_empty)
      expect(["aap", "noot", "mies"]).to(contain("noot"))
      expect(["noot"]).to(contain_only("noot"))

    with description(ASampleClass):
      with it('is an instance of the class'):
        expect(ASampleClass()).to(be_a(ASampleClass))

      with it('can test for exceptions'):
        sample_class = ASampleClass()
        expect(lambda: sample_class.method_throws_error()).to(raise_error(ValueError, "Illegal value"))

      with it("can assess none to be returned"):
        expect(ASampleClass().return_none()).to(be_none)

    with description("and nesting can and should be used!"):
      with context("within another context"):
        with it("asserts boolean values"):
          expect(True).to(be_true)
          expect(False).to(be_false)
      

  with context('Using before and after to set up and tear down'):
    with before.all:
      print ('This code will be run once, before all examples')

    with before.each:
      print ('This code will be run before each example')

    with after.each:
      print ('This code will be run after each example')

    with after.all:
      print ('This code will be run once, after all examples')    

    with context("Given all hooks are configured"):
      with it('activates all context hooks'):
        expect(True).to(be_true)
