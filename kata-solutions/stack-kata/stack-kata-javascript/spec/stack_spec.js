import { Stack } from "../src/stack.js";

describe("A new stack", function () {
  var myStack;

  beforeEach(function () {
    myStack = new Stack();
  });

  it("is empty after initialization", function () {
    expect(myStack.isEmpty()).toEqual(true);
  });

  it("should throw an exception on a pop operation", function () {
    expect(function () {
      myStack.pop();
    }).toThrow(new Error("Stack underflow"));
  });

  describe("which had one push", function () {
    beforeEach(function () {
      myStack.push(8);
    });
    it("should not be empty", function () {
      expect(myStack.isEmpty()).toEqual(false);
    });
    it("should be empty after one pop", function () {
      myStack.pop();
      expect(myStack.isEmpty()).toEqual(true);
    });
    it("should not be empty after another push and 1 pop", function () {
      myStack.push(9);
      myStack.pop();
      expect(myStack.isEmpty()).toEqual(false);
    });
    it("should pop the pushed element", function () {
      expect(myStack.pop()).toEqual(8);
      myStack.push(9);
      expect(myStack.pop()).toEqual(9);
    });
    it("should pop 2 elements after another push", function () {
      myStack.push(9);
      expect(myStack.pop()).toEqual(9);
      expect(myStack.pop()).toEqual(8);
    });
  });
});
