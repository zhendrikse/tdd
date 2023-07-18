const { fibonacci, validateLastName, validator } = require('../src/helpers');

describe('Test Helpers', function () {
  beforeEach(function () {
    jasmine.addMatchers({
      containsErrorMessages: function () {
        return {
          compare: function (actual, expected) {
            const errorMessages = actual;
  
            return {
              pass: Object.keys(errorMessages).length === expected
            };
          }
        };
      }
    });
  });
  
  it('should calculate Fibonacci series', function () {
    const fib = fibonacci(4);
    expect(fib).toEqual(5);
  });
  
  it('validates a valid last name', function () {
    expect(validateLastName('Puk')).toEqual(true);
  });

  it('returns error messages when validation is not ok', function() {
    const data = {lastName: "Puk"}
    expect(validator(data)).containsErrorMessages(0)
  });

  it('returns no error messages when validation is ok', function() {
    const data = {lastName: "P5k"}
    expect(Object.keys(validator(data)).length).toEqual(1)
  });
});
