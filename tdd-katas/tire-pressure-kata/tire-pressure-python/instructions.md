# Introduction

Please read the general [introduction to the tire pressure kata](../README.md) first!

# Getting started

Carry out the following steps in order:

1. Create an intial Python kata set-up as described
   [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).
   Choose 'n' when prompted for the rSpec syntax and as well as the code coverage.
2. Remove the `.py` files in the `src` and `test` directories, but leave the
   `__init__.py` files untouched!
3. Copy the `alarm.py` and `sensor.py` files into the `src` directory 
4. Copy the `alarm_test.py` file into the `test` directory
5. Invoke
   ```
   $ poetry install
   $ ./run_tests.sh
   ``` 

# Option 1: [the peel strategy](https://www.sammancoaching.org/learning_hours/testable_design/peel.html)

Let's first order the list of steps listed in 
[the explanation of the peel strategy](https://www.sammancoaching.org/learning_hours/testable_design/peel.html).
As we are continuously running the tests in an interpreted language, some
steps are redundant.

1. Identify the section of code you want to extract and copy it
2. Declare a new function with a suitable name
3. Define the arguments of the new function
4. Define the return type of the new function
5. Paste the section of code as the body of the new function
6. Replace the section of code with a call to the new function

The section of code we want to extract is

```python
  if psi_pressure_value < self._low_pressure_threshold \
          or self._high_pressure_threshold < psi_pressure_value:
      self._is_alarm_on = True
```

So let's first define

```python
def set_alarm_on_low_or_high_tire_pressure(psi_pressure_value):
  pass
```

Next we copy the section of code we want to extract into the body
and finally we replace the lines in the original function `check()`
by a call to our newly created function.

Now we can write tests for this function like so:

```python
    def test_alarm_is_on_when_tire_pressure_above_threshold(self):
      alarm = Alarm()
      alarm.check(23)
      assert alarm.is_alarm_on
```

# Option 2: [slice](https://www.sammancoaching.org/learning_hours/testable_design/slice.html)

We extend the `check()` function with one paramter:

```python
      def check(self, psi_pressure_value = None):
        if psi_pressure_value == None:
          psi_pressure_value = self._sensor.pop_next_pressure_psi_value()
          
        if psi_pressure_value < self._low_pressure_threshold \
                or self._high_pressure_threshold < psi_pressure_value:
            self._is_alarm_on = True
```

As described in option 1, we can now start writing our tests.

# Option 3: [monkey patching](https://betterprogramming.pub/what-are-duck-typing-and-monkey-patching-in-python-2f8e3d6b864f)

Since Python is a dynamically dynamic (scripting) language, it is
not only possible to dynamically type your variables, but also modify
its behavior at run time, e.g. redefine a function by declaring new
functionality in a function with the same name. The latter definition 
then overrules the behavior of the former. This is effectively what
monkey patching is all about.

Let's apply that to our tire pressure case by defining a new
function in our test that always returns a tire pressure that 
is too high:

```python
def get_too_high_tire_pressure(self):
  return 23
``` 

Next we assign this function to the `Sensor` class:

```python
Sensor.pop_next_pressure_psi_value = get_too_high_tire_pressure
``` 

We can now consistently check that the alarm is on when the tire
pressure is too high. Likewise we can test when it is too low.


