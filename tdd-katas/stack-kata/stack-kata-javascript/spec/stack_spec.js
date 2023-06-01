import {Stack} from '../src/stack.js';

describe("A new stack", function() {
  it("is empty after initialization", function () {
    var my_stack = new Stack()
    expect(my_stack.isEmpty()).toEqual(true);
  })
})
