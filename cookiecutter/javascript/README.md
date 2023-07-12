# Options

### Kata name

```
kata [GameOfLife]: 
```

Name of the kata. The name of the two generatied source and 
test files will be based on this name.

### Project slug

```
project_slug [gameoflife]: 
```

This slug is automatically generated and generally doesn't
need to be modified. The directory name of the kata will be
named usiing this slug.

### Short description

```
project_short_description [This kata practices TDD]: 
```

Optional, will be used in packaging files such as the ```package.json```.

### Code coverage

Code coverage only works in stand-alone mode, so it does _not_ apply
when running tests in the browser. In this case just press return.

```
Select code_coverage:
1 - y
2 - n
Choose from 1, 2 [1]: 
```

Choose this if you want to have code coverage facilities.

### Tests in browser

```
Select tests_in_browser:
1 - n
2 - y
```

Select yes here if you want to run your specifications (test) in a browser 
served by nodejs http-server.

### Author

```
author [Your name]: 
```

Optional, will be used in packaging files such as the ```package.json```.

