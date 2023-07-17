const { fibonacci } = require('../src/helpers');

describe('Test Helpers', function () {
  it('should calculate Fibonacci series', function () {
    const fib = fibonacci(4);
    expect(fib).toEqual(5);
  });
});
