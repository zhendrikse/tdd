# Registration form kata

This kata is based on 
[the original login form UI kata](https://github.com/SoftDevGang/login-form-tdd-ui-kata)
and comprehensively introduced [here](http://blog.code-cop.org/2020/01/login-form-tdd-ui-kata.html).

## Introduction

This kata is based on a combination of resources:

- The section [How to test Node.js applications with Jasmine](https://www.lambdatest.com/learning-hub/jasmine-unit-testing#how-to-test-nodejs-applications-with-jasmine)
- The HTML page is inspired by the [Aliens' Registration Form with validation](https://codepen.io/absalan/pen/WNbwbXB?editors=1111)
- The project lay-out is inspired by [this Jasmine example](https://github.com/Kaperskyguru/jasmine-example/) available on GitHub. Warning, this project contains many bugs though!

The idea is to learn how to apply TDD to code that is meant to be used/executed in a front-end.

## Goal

The goal is to build the validation logic belonging to the [Aliens' Registration Form ](https://codepen.io/absalan/pen/WNbwbXB?editors=1111)
using TDD. This way practitioners should get an idea of how the same principles can/should be applied to front-end development.

Requirements for the minimum functionality
- There is a user name input field, which is limited to 20 characters.
- The label "Phone, email or username" is left, next to the input field.
- There is a password field, which is limited to 20 characters.
- The password is either visible as asterisk or bullet signs.
- The label "Password" is left, next to the input field.
- There is a "Log in" button in the bottom right corner of the window.
- There is a label in a red box above the button. It is only visible if there was an error.

### Possible extensions

- The app can be made more interesting by persisting the user
  data into a database, see for example
  [this post](https://medium.com/swlh/read-html-form-data-using-get-and-post-method-in-node-js-8d2c7880adbf)!
