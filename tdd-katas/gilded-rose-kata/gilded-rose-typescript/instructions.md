# Introduction

Please read the general [introduction to the gilded rose kata](../README.md) first!

# Getting started

First, create an initial Typescript kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the newly created project directory and consult
the provided ``README.md`` in there.

## Copying the required files

Copy the contents of the ``GildedRose.ts`` file over to the generated 
source file in the ``src`` folder. Depending on how you named your kata,
this should be something similar as

```shell
$ cat GildedRose.ts > gilded_rose_kata/src/gilded_rose_kata.ts
```

Do the same with the spec file

```shell
$ cat GildedSpec.ts > gilded_rose_kata/spec/gilded_rose_kata_spec.ts
```

#### IMPORTANT

Inspect the third line of your spec file. The import/require statement 
on line three should match the file name that is in the ``src`` 
directory. Make  sure this file name and the import/require 
statement are properly aligned!

Next, enter your generated kata directory and install the approvals test 
library

```shell
$ npm install approvals --save-dev
```

Finally, you should be able to start working by invoking

```shell
npm run test
```

# Improving the coverage

<details>
<summary>Using the approval test framework</summary>

```typescript
function convert_items_to_string(items = [] as Array<Item>) {
  let items_as_string = items.map((item) => item.toString() + "\n")
  return items_as_string.reduce(
    (accumulator, currentValue) => accumulator + currentValue,
    "",
  );
}

describe('Gilded Rose', () => {
  it('updates a foo item', () => {
    const items = [
      new Item("Foo", 0, 0)
    ];
    const gildedRose = new GildedRose(items);
    const updated_items = gildedRose.updateQuality();
    verify(convert_items_to_string(updated_items));
  });
});
```
</details>

To get a useful baseline, we have to add a `toString()` method to the `Item` class

<details>
<summary>Adding a `toString()` method to the `Item` class</summary>

```typescript

  public toString(): string {
    return "name: " + this.name + ", sellIn: " + this.sellIn + ", quality: " + this.quality
  }
```
</details>

## Inspecting the code coverage

Let's see what the current coverage is by running

```bash
$ npm run test
```

The task is to get the code coverage up to 100% by adding more items.
