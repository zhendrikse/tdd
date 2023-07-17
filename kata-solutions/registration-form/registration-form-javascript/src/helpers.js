function fibonacci(num, memo) {
  memo = memo || {};

  if (memo[num]) return memo[num];
  if (num <= 1) return 1;

  return (memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo));
}

function validateLastName(lastName) {
  // var letters = /^[A-Za-z]+$/;
  // if (lastName.match(letters)) {
  //   text = '';
  //   return true;
  // } else {
  //   return false;
  // }
  return true
}

module.exports = {
  fibonacci: fibonacci,
  validateLastName: validateLastName
}