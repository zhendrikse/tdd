# Introduction

Please read the general [introduction to the registration form kata](../README.md) first!

# Getting started

1. First, create an intial Javascript kata set-up as described 
   [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).
2. Next, copy the `index.html`, `index.js`, `package.json`, and `style.css` 
   files over to the root folder of your newly generated kata folder.
3. Copy the `helpers.js` file into the `src` folder 
4. Remove the originally generated Javavscript file in the `src` folder
5. Rename the spec file in the `spec` folder to `helper_spec.js`.
6. Finally, change the first line in the file `spec/helper_spec.js` to
   ```javascript
   const { fibonacci } = require('../src/helpers');
   ```

The Node.js app can be started as follows:

```bash
$ node index.js
```

or 

```bash
$ npm run serve
```

You are now ready to start this kata!

# Detailed instructions

## Last name field

First write a test for a successful validation of the last name field.

<details>
<summary>Reveal test</summary>
  
```javascript
it('should validate a valid last name', function () {
    const lastName = validateLastName('Solomon');
    expect(lastName).toEqual(true);
});
```
</details>

To make this test pass, we first make the newly invoked function known
in the `helper_spec.js`

<details>
  
```javascript
const { fibonacci, validateLastName } = require('../src/helpers');
```
</details>

Next, let's write a minimal implementation of `validateLastName`
in the `helpers.js` file that is just sufficient to make the test pass.

<details>
<summary>Reveal implementation</summary>

```javascript
function validateLastName(lastName) {
  return true
}

module.exports = {
  fibonacci: fibonacci,
  validator: formValidation,
  validateLastName: validateLastName
}
```
</details>

This makes our test green!

We only want to allow characters in the name, so a check
on the regular expression `^[A-Za-z]+$` is logical.

<details>

```javascript
  it('should invalidate an invalid last name', function () {
    const lastName = validateLastName('P5k');
    expect(lastName).toEqual(false);
  });
```
</details>
