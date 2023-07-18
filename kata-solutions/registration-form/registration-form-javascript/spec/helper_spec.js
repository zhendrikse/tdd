const { fibonacci, validateLastName } = require('../src/helpers');

describe('Test Helpers', function () {
  it('should calculate Fibonacci series', function () {
    const fib = fibonacci(4);
    expect(fib).toEqual(5);
  });
  
  it('should validate a valid last name', function () {
    const lastname = validateLastName('Puk');
    expect(lastname).toEqual(true);
  });
  
  it('should invalidate an invalid last name', function () {
    const lastname = validateLastName('P5k');
    expect(lastname).toEqual(false);
  });
});
