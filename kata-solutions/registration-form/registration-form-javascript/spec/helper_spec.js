const { fibonacci, validateLastName, validator } = require('../src/helpers');

describe('Test Helpers', function () {
  it('should calculate Fibonacci series', function () {
    const fib = fibonacci(4);
    expect(fib).toEqual(5);
  });
  
  it('validates a valid last name', function () {
    const lastname = validateLastName('Puk');
    expect(lastname).toEqual(true);
  });

  it('returns error messages when validation is not ok', function() {
    const data = {lastName: "Puk"}
    expect(Object.keys(validator(data)).length).toEqual(0)
  });

  it('returns no error messages when validation is ok', function() {
    const data = {lastName: "P5k"}
    expect(Object.keys(validator(data)).length).toEqual(1)
  });
});
