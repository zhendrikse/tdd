'use strict';

import { expect, assert } from "chai"
import { Stack } from "../src/Stack"

describe("A new stack", function () {
  var myStack: Stack;

  beforeEach(function () {
    myStack = new Stack()
  })

  it("should be empty", function () {
    expect(myStack.isEmpty()).to.equal(true);
  })

  it("should throw an exception on a pop operation", function () {
    expect(function () { myStack.pop() }).to.throw("Stack underflow")
  })


  describe("which had one push", function () {
    beforeEach(function () {
      myStack.push(8)
    })
    
    it("should not be empty", function () {
      expect(myStack.isEmpty()).to.be.false
    })
    
    it("should be empty after one pop", function () {
      myStack.pop()
      expect(myStack.isEmpty()).to.be.true
    })
    
    it("should not be empty after another push and 1 pop", function () {
      myStack.push(9)
      myStack.pop()
      expect(myStack.isEmpty()).to.be.false;
    })
    
    it("should pop the pushed element", function () {
      expect(myStack.pop()).to.equal(8)
      myStack.push(9)
      expect(myStack.pop()).to.equal(9)
    })
    
    it("should pop 2 elements after another push", function() {
      myStack.push(9)
      expect(myStack.pop()).to.equal(9)
      expect(myStack.pop()).to.equal(8)
    })
  })
})

