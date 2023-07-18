function fibonacci(num, memo) {
  memo = memo || {};

  if (memo[num]) return memo[num];
  if (num <= 1) return 1;

  return (memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo));
}
function formValidation(data) {
  const messages = {};
  
  return messages;
}

module.exports = {
  fibonacci: fibonacci,
  validator: formValidation
}