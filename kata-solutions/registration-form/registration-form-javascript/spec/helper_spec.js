const { fibonacci, validateLastName } = require('../src/helpers');

describe('Test Helpers', function () {
  it('should calculate Fibonacci series', function () {
    const fib = fibonacci(4);
    expect(fib).toEqual(5);
  });
  it('should validate good last name', function () {
    const lastName = validateLastName('Solomon');
    expect(lastName).toEqual(true);
  });
});
