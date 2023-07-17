# Introduction

Please read the general [introduction to the registration form kata](../README.md) first!

# Getting started

1. First, create an intial Javascript kata set-up as described 
   [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).
2. Next, copy the `index.html`, `index.js`, and `style.css` 
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

You are now ready to start this kata!

# Detailed instructions


