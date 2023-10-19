# Introduction

Please read the general [introduction to the babysteps timer kata](../README.md) first!

## Starting the babysteps timer

The timer can be started like so:

```bash
$ npm install
$ npm run test
$ npm run compile
$ npm run serve
``` 

## Goal of the babysteps timer kata

The constraint is to write tests for the babysteps timer before refactoring
the Typescript code. A first example test has already been provided to get
you started, but feel free to throw that (somewhat) useless test away!

Tip: you may want to run tests continuously by using:

```bash
$npm run watch
```

## References

I first read about this kata in [5 coding exercises to practice refactoring Legacy Code](https://understandlegacycode.com/blog/5-coding-exercises-to-practice-refactoring-legacy-code/).

The original code was taken from the 
[Babysteps timer](https://github.com/dtanzer/babystepstimer) 
repository with some modifcations and updates such as

- Updates of all the npm packages.
- Removed deprecated `mocha.opts` file
- Updates (using modules) of the `package.json` and `tsconfig.json` to make tests possible
- Minor update of `babysteps.ts` to latest node (timer) types.
- Changed the way the Javascript is included as a module from within the HTML file using
  [these tips](https://stackoverflow.com/questions/69888029/how-to-call-a-function-declared-in-a-javascript-module-type-module-from-an-htm).

These updates have now been merged into the original GitHub repository!

# Detailed instructions

## Our first actual test

As the test that is already given purely serves as an illustration,
let's start by writing a meaningful test.

<details>
  <summary>Test that <code>H1</code> contains the time</summary>

  ```typescript
  it("h1 contains the time", function() {
    expect(document.querySelector("h1")?.innerHTML).to.equal("02:00")
  })
  ```
</details>

## Check that the clock starts ticking

Next, we can check that after receiving a start command, the clock starts ticking.

<details>
  <summary>Test that the clock starts ticking after <code>start</code>-command</summary>

  ```typescript
  it("time ticks back over time", async() => {
    command("start")
    await new Promise(resolve => setTimeout(resolve, 50))
    expect(document.querySelector("h1")?.innerHTML).to.equal("01:59")
    command("stop")
  })
  ```
</details>

## Check that the clock has ticked twice


Next, we can check that after receiving a start command, the clock starts ticking.

<details>
  <summary>Test that the clock starts ticking back two seconds</summary>

  ```typescript
  it("time ticks back over time", async() => {
    command("start")
    await new Promise(resolve => setTimeout(resolve, 1050))
    expect(document.querySelector("h1")?.innerHTML).to.equal("01:58")
    command("stop")
  })
  ```

  We may as well move the start and stop commands into a `beforeEach()`
  and `afterEach()`
  ```typescript
  beforeEach(() => {
    command("start")
  })

  afterEach(() => {
  command("stop")
  })
  ```
</details>

## Introducing an additional layer of indirection

In the `babystep.ts` file, we find at line 24 a hard-coded
call to the system date-time

```typescript
  _currentCycleStartTime = Date.now();
```

Let's obtain that value via a separate function call:

<details>
  <summary>Opening our first seam: <code>Date.now()</code></summary>

  ```typescript
  function currentTime() {
    return Date.now();
  }

  export function command(arg: string): void {
    // 
    // ...
    //

        _timerRunning = true;
        _currentCycleStartTime = currentTime();
  ```

  Next, let's generalize it to a class

  ```typescript
  function currentTime() {
    return new class {
      currentTime() {
       return Date.now();
      }
    }().currentTime()
  }
  ```

  This allows us to promote the anonymous inner class up to
  a named class called `RealClock`, and pass a new instance 
  of that `RealClock` as a default value of an additional 
  parameter to the `command()` function.

  This results in the following modifications (where an additional
  `Clock` interface has been introducted at the same time)

  ```typescript
  interface Clock {
    currentTime(): number
  }
  
  class RealClock implements Clock {
    currentTime() {
       return Date.now();
    }
  }

  export function command(arg: string, clock: RealClock = new RealClock()): void {
    //
    // ...
    //
  ```
</details>