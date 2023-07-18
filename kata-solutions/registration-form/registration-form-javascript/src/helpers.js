function fibonacci(num, memo) {
  memo = memo || {};

  if (memo[num]) return memo[num];
  if (num <= 1) return 1;

  return (memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo));
}

function validateLastName(lastname) {
  var allowed_letters = /^[A-Za-z]+$/;
  return lastname.match(letters);
}

function formValidation(data) {
  const messages = [];
  var contentsLastNameField = data['lastName'];

  if (!validateLastName(contentsLastNameField)) 
    messages['lastName'] = 'Last name should contain only letters';
  
  return messages;
}

module.exports = {
  fibonacci: fibonacci,
  validator: formValidation,
  validateLastName: validateLastName
}
