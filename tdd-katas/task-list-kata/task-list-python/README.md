# The Check List Kata

![Checklist](./assets/to-do.png)

## Kata context, purpose, and boundary conditions

This section contains a reproduction of [the original task list kata](https://kata-log.rocks/task-list-kata). 

### Task list
This kata is an example of code obsessed with primitives.

A _primitive_ is any concept technical in nature, and not relevant to your business domain. This includes integers, characters, strings, and collections (lists, sets, maps, etc.), but also things like threads, readers, writers, parsers, exceptions, and anything else purely focused on technical concerns. By contrast, the business concepts in this project, “task”, “project”, etc. should be considered part of your _domain model_. The domain model is the language of the business in which you operate, and using it in your code base helps you avoid speaking different languages, helping you to avoid misunderstandings. In our experience, misunderstandings are the biggest cause of bugs.

### Exercise
Try implementing the following features, refactoring primitives away as you go. Try not to implement any new behaviour until the code you’re about to change has been completely refactored to remove primitives, i.e. **_Only refactor the code you’re about to change, then make your change. Don’t refactor unrelated code_**.

One set of criteria to identify when primitives have been removed is to only allow primitives in constructor parameter lists, and as local variables and private fields. They shouldn’t be passed into methods or returned from methods. The only exception is true infrastructure code &#8212; code that communicates with the terminal, the network, the database, etc. Infrastructure requires serialisation to primitives, but should be treated as a special case. You could even consider your infrastructure as a separate domain, technical in nature, in which primitives _are_ the domain.

You should try to wrap tests around the behaviour you’re refactoring. At the beginning, these will mostly be high-level system tests, but you should find yourself writing more unit tests as you proceed.

### Features

You should be able to give the list with tasks the following commands:

1. Deadlines
  - Give each task an optional deadline with the `deadline <ID> <date>` command.
  - Show all tasks _due today_ with the `today` query.
2. Customisable IDs
  - Allow the user to specify an identifier that’s not a number.
  - Disallow spaces and special characters from the ID.
3. Deletion
  - Allow users to delete tasks with the `delete <ID>` command.
4. Views
  - View tasks sorted by date with the `view by date` query.
  - View tasks sorted by deadline with the `view by deadline` query.
  - Optional: don’t remove the functionality that allows users to view tasks by project, but change the query to `view by project`.

Please also take into consideration the [Considerations and Approaches](https://kata-log.rocks/task-list-kata) section that can be found in the original description of this kata. At least alwyas segregate commands (that don't return anything and modify the state of the system) and queries (returning values but leaving the state of the system invariant).

Last but not least: verify all the time you have 100% test coverage. As soon as you get below 100%, you wrote production code that you did not specify/test yet!

# Implementation

Let's implement the requirements one by one. With this kata, keep in mind not accidentally to fall into the trap of an [analysis paralysis](https://exceptionnotfound.net/analysis-paralysis-the-daily-software-anti-pattern/), so keep the [necessary & sufficient](https://github.com/testdouble/contributing-tests/wiki/Necessary-%26-Sufficient) guideline in mind.


## Implementing the deadline command

As discussed in the first course, let's first make a plan.

### Making a plan first

Like the stack kata, we'll start with an empty task list first. The simplest thing that could possibly work! Do not forget to run your tests/specificatons as frequently as possible, preferrably after changing each and every line!

1. An new/empty task list
    - Contains zero tasks / has a zero task count (hint!)
    - Throws an exception when we request a task by ID
2. Implement the possibility to add one or more tasks to the task list
    - Verify that the task(s) is/are returned when getting the list of tasks
    - Verify that the right task(s) is/are returned when retrieved by ID
    - Specify we expect an exception when you try to add another task with an existing ID
3. Make the task list accept the `deadline <ID> <date>` command
    - Throw an exception when the command token is not `deadline`
    - Throw an exception if the `deadline` is not followed by an integer and date
    - Throw an exception when task with `<ID>` does not exist
    - Should fire and forget when task with `<ID>` exists, but task due date must be set
4. Make the task list accept the `today` query, which returns all tasks due today
    - Make the query return an empty list when invoked on an empty task list
    - Make the query return the task of today after setting deadline of a task to today
    - Make the query return an empty list after setting deadline of a task to tomorrow
5. In order to implement the `view by date` query, we have to store the date of creation too
    - Add a creation date to a task
    - Implement the `view by date` query
    - Implement the `view by deadline` query, and make sure you are able to deal with tasks that haven't set the deadline date 
 

## Implementing ID as string

The main challenge here is to generalze the existing code base in (extremely) small steps. A possible solution is to use Python's unions:

```python
class Task:
  def __init__(self, id:Union[int, str], description: str) -> None:
```

These type cases can then be distinguished like so: 

```python
  def validate_id(self, id:Union[int, str]) -> None:
    if type(id) is int:
      self.validate_int_id(id)
    if type(id) is str:
      self.validate_string_id(id)
```

## Refactoring activities

During the implementation, you may watch to keep a very close eye on applying the following additional principles during your refactoring phase:

- [Command query separation](https://martinfowler.com/bliki/CommandQuerySeparation.html)
- [Single responsibility principle](https://stackify.com/solid-design-principles/) (from SOLID Design Principles)

Note that in the previous katas we have mainly applied the [DRY and KISS](https://dzone.com/articles/software-design-principles-dry-and-kiss) principles.

### Task ID

You may want to move the task ID related logic into its own (value) object. 

### Command handling

Command handling should not be a responsibility of the task list. The command handling logic should therefore also be moved to its own classes.


### References

- [Task list kata](https://kata-log.rocks/task-list-kata)
- [Expects matchers](https://expects.readthedocs.io/en/stable/matchers.html#)
- [Mamba PDF doc](https://readthedocs.org/projects/mamba-bdd/downloads/pdf/latest/)