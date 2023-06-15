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

Optional, will be used in packaging files such as the ```pyproject.toml```.

### rSpec syntax

```
Select rspec_syntax:
1 - y
2 - n
Choose from 1, 2 [1]: 
```

Option one will prepare a [Mamba](https://github.com/nestorsalceda/mamba)-based 
project, else you'll be using [pytest](https://docs.pytest.org/en/7.3.x/).

### Code coverage

```
Select code_coverage:
1 - y
2 - n
Choose from 1, 2 [1]: 
```

Choose this if you want to have code coverage facilities.

When code coverage is enabled, a file called ``coverage`` will be produced.
This can be inspected by invoking

```shell
$ poetry run coverage report
```

Alternatively, you may generate an HTML report by invoking

```shell
$ poetry run coverage html
```

A directory named ``htmlcov`` is then generated, that
can then be inspected by starting an HTTP server like so

```shell
python -m http.server 8000 -d htmlcov >/dev/null 2>/dev/null &
```

### Author

```
author [Your name]: 
email [your@email.com]: 
```

Optional, will be used in packaging files such as the ```pyproject.toml```.

