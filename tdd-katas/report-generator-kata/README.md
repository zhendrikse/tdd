# Report generation kata

The report generation kata is based on 
[this exercise](https://nbviewer.org/github/jerry-git/learn-python3/blob/master/notebooks/intermediate/exercises/05_idiomatic_python_exercise.ipynb).

## The specification of the report generation

Given a file with the following content:
```
something
1
7
somEThing

2
wassup
woop
woop
something
WoOP
```

This file should result in the following report:

```
missing values: 1
highest number: 7.0
most common words: something, woop
occurrences of most common: 3
#####
numbers: [1.0, 7.0, 2.0]
words: ['something', 'something', 'wassup', 'woop', 'woop', 'something', 'woop']
```

# Goals

The code should be refactored, _preferably_ in small steps. To facilitate this process, 
a script has been provided, that continuously runs the unit test(s):

```bash
$ ./run_watch.sh
```

## Possible improvement strategies

- Apply some (or perhaps all?) [SOLID principles](https://dnamic.ai/blog/introduction-of-solid-design-principles-by-uncle-bob/)
- Refactor towards more [Python idiomatic code](https://docs.python-guide.org/writing/style/)
- Apply the principles of [clean code in Python](https://testdriven.io/blog/clean-code-python/)
- Make tests independent from the file system ([FIRST](https://medium.com/pragmatic-programmers/unit-tests-are-first-fast-isolated-repeatable-self-verifying-and-timely-a83e8070698e))

