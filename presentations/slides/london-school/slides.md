---
title: London school of test-driven development
author: Zeger Hendrikse
date: 2023-09-29
---

#### Coders should test

### Testers should code

## We all should do TDD!

by [Zeger Hendrikse](https://www.it-essence.nl/)

---
![Goals](./images/goals.png)
<ul>
<div>
<li><a href="https://blog.devgenius.io/detroit-and-london-schools-of-test-driven-development-3d2f8dca71e5">London vs Detroit schools of TDD</a></li>
</div>
<div class="fragment">
<li>See when mocks should be used <em>in practice</em></li>
</div> 
<div class="fragment">
<li>Practice TDD as a mockist</li>
</div> 
</ul>

---

### Don't mock what you don't own

<div class="fragment">
  <h2>Use <a href="../clean-architecture/repository-adapter/slides.md">adapters</a> instead!</h2>
</div>

> Effective unit tests only test one thing. To do this you have to move the irrelevant portions out of the way (e.g., MockObjects). This forces out what might be a poor design choice.
---

### Test doubles

<ul>
  <div class="fragment">
    <li><b>Dummy</b>: a filler, i.e. not really used</li>
  </div>
  <div class="fragment">
    <li><b>Fake</b>: fake implementation, e.g. in-mem DB</li>
  </div>
  <div class="fragment">
    <li><b>Stubs</b>: canned answers (for <i>queries</i>)</li>
  </div>
  <div class="fragment">
    <li><b>Spies</b>: objects that record call info(<i>commands</i>)</li>
  </div>
  <div class="fragment">
    <li><b>Mocks</b>: objects that verify <i>behaviour</i></li>
  </div>
</ul>

---

### Rulez of the TDD game

<table>
  <colgroup>
    <col span="1" style="width: 60%;"/>
    <col span="1" style="width: 40%;"/>
  </colgroup>
			         
  <tbody><tr>
    <td>
      <img alt="Red Green Refactor" src="./images/redgreenrefactor.png"/>
    </td>
    <td>
      <ol>
        <li>Write a failing test</li>
        <li>Make it pass</li>
        <li>Refactor relentlessly</li>
      </ol>
    </td>
  </tr></tbody>
</table>

---

### Rulez of the TDD game

**Small increments**, so we are [not allowed to write](http://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html)
<ol>
  <div class="fragment">
    <li>any code unless it is to make a failing test pass</li>
  </div>
  <div class="fragment">
    <li>any more of a test than is sufficient to fail (also compilation!)</li>
  </div>
  <div class="fragment">
    <li>any more code than is sufficient to pass the one failing unit test</li>
  </div>
</ol>
---

### Kent Beck

![Kent Beck](./images/kentbeck.jpg)

---
### <a href="https://en.wikipedia.org/wiki/Kent_Beck">Kent Beck's</a> [design rules](https://martinfowler.com/bliki/BeckDesignRules.html)

1. Passes the tests
2. Reveals intention ([Clean code](https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29))
3. No duplication ([DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself))
4. Fewest elements (<a href="http://wiki.c2.com/?DoTheSimplestThingThatCouldPossiblyWork">Simplest thing that could possibly work</a>)

---

### User story / epic

#### Audio player

<div style="font-size: 20px; border: 1px solid;" >

now ᴘʟᴀʏɪɴɢ: MyGreatSong.mp3 ───────────⚪────── ◄◄⠀▐▐⠀►► 𝟸:𝟷𝟾 / 𝟹:𝟻𝟼⠀───○ 🔊

</div>
&nbsp;

<div style="text-align: left">
<b>As</b> a music lover 

<b>I want</b> to play my favourite playlist(s)

<b>so that</b> I can use the music during my workouts
<div>

---

#### Plans are worthless ...

### ... but planning is essential:

- Audio player in initial state
- Previous track button
- Next track button
- Next track button twice
- Pressing next and previous

&nbsp;

<div class="fragment">
Credits to <a href="http://barbra-coco.dyndns.org/yuri/Kent_Beck_TDD.pdf">Kent Beck</a> and <a href="https://quoteinvestigator.com/2017/11/18/planning/">Eisenhower</a>!
</div>

---

### What the result will be

<iframe width="100%" height="500" src="//jsfiddle.net/zhendrikse/bu7tv1kp/3/embedded/js,result/dark/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>

---

### Jasmine prerequisites

- Creating a [spy object](https://stackoverflow.com/questions/24321307/what-is-the-difference-between-createspy-and-createspyobj)
```javascript
beforeEach(function() {
  tape = jasmine.createSpyObj('tape', ['play', 'pause', 'stop', 'rewind']);

  tape.play();
  tape.pause();
  tape.rewind(0);
});
```

---

### Jasmine prerequisites

- Mocking return value
```javascript
my_object.my_method.and.returnValue("my_return_value")
```

- Mocking subsequent return values
```javascript
my_object.my_method.and.returnValues("my_return_value1", "my_return_value2")
```
---

### Jasmine prerequisites

- Calls [with arguments](https://jasmine.github.io/api/edge/Spy#withArgs)
  
  ```javascript
  spyOn(componentInstance, 'myFunction')
      .withArgs(myArg1).and.returnValue(myReturnObj1)
      .withArgs(myArg2).and.returnValue(myReturnObj2);
  ```

- Verify behaviour
  ```javascript 
  expect( foo.callMe ).toHaveBeenCalled();
  ```

---


### Let's do this

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@zwh/Audioplayer-with-TDD-Javascript-and-Jasmine?lite=false"></iframe>

---

### Player in initial state

```javascript
describe('Given a just switched on audioplayer', function () {
  it('should show the first song in the playlist on display', function() {
    audioplayer = new AudioPlayer()
    expect(
      audioplayer.getCurrentSong()).toEqual("play: MyGreatSong.mp3")
  })
})
```

----

```javascript
class AudioPlayer {
  getCurrentSong() {
    return "play: MyGreatSong.mp3"
  }
}
```
---

### Is the song playing?

```javascript
it('should have the play/pause button in state play', function(){
  audioplayer = new AudioPlayer()

  expect(
    audioplayer.getPlayPauseButtonStatus()).toEqual(PlayPauseButton.PLAY)
})
```

----

```javascript
const PlayPauseButton = {
	PLAY: "play",
	PAUSE: "pause",
}

class AudioPlayer {
  getCurrentSong() {
    return "play: MyGreatSong.mp3"
  }

  getPlayPauseButtonStatus() {
    return PlayPauseButton.PLAY
  }
}

```

---

### Red, green, ..., refactor!

```javascript
describe('Given a just switched on audioplayer', function () {
  beforeEach(function () {
    audioplayer = new AudioPlayer()
  })

  it('should show the first song in the playlist on display', function() {
    expect(
      audioplayer.getCurrentSong()).toEqual("play: MyGreatSong.mp3")   
    })

  it('should have the play/pause button in state play', function(){
    expect(audioplayer.getPlayPauseButtonStatus()).toEqual(PlayPauseButton.PLAY)
  })
})

```

---

### Our updated plan

- ~~Audio player in initial state~~ &#10003;
- Previous track button
- Next track button
- Next track button twice
- Pressing next and previous
---

### Previous track button

```javascript
describe('When the previous track button is pressed', function() {
  it('should do nothing', function() {
      spyOn(audioplayer, "previousTrack")
      audioplayer.previousTrack()
      expect(audioplayer.previousTrack).toHaveBeenCalled();
  })
})
```

----

```javascript

  previousTrack() {}

```

---

### Our updated plan

- ~~Audio player in initial state~~ &#10003;
- ~~Previous track button~~ &#10003;
- Next track button
- Next track button twice
- Pressing next and previous

---

### Next track button

```javascript
describe('When the next track button is pressed', function () {
  it('should show the next song in the playlist on display', function () {
    audioplayer.nextTrack()
    expect(audioplayer.getCurrentSong()).toEqual("play: MyUpbeatSong.mp3")
  })
})
```

----

```javascript
class AudioPlayer {
  constructor() {
    this.currentTrack = "MyGreatSong.mp3"
  }

  getCurrentSong() {
    return "play: " + this.currentTrack
  }

  getPlayPauseButtonStatus() {
    return PlayPauseButton.PLAY
  }

  previousTrack() {}

  nextTrack() {
    this.currentTrack = "MyUpbeatSong.mp3"
  }
}
```

---

### Our updated plan

- ~~Audio player in initial state~~ &#10003;
- ~~Previous track button~~ &#10003;
- ~~Next track button~~ &#10003;
- Next track button twice
- Pressing next and previous

---

### Next track _once more_

```javascript
describe('When the next track button is pressed twice', function () {
  it('should show the third song in the playlist on display', function () {
    audioplayer.nextTrack()
    audioplayer.nextTrack()
    expect(audioplayer.getCurrentSong()).toEqual("play: MyWorkoutSong.mp3")
  })
})
```

----

### Make the test pass!

```javascript
class AudioPlayer {
  constructor() {
    this.currentTrack = "MyGreatSong.mp3"
    this.songCounter = 0
  }

  // ...

  nextTrack() {
    this.songCounter++

    if (this.songCounter == 1)
      this.currentTrack = "MyUpbeatSong.mp3"
    else
      this.currentTrack = "MyWorkoutSong.mp3"
  }
}
```

---

### Refactor...

#### Playlist collaborator inevitable

Introduce mock in small increments!

```javascript
playlist = jasmine.createSpyObj('playlist', ['getCurrentTrack', 'nextTrack'])
playlist.getCurrentTrack.and.returnValue("MyGreatSong.mp3")

audioplayer = new AudioPlayer(playlist)
```

----

### Step 1

```javascript
class AudioPlayer {
  constructor(myPlaylist) {
    this.playlist = myPlaylist
    this.currentTrack = this.playlist.getCurrentTrack()
    this.songCounter = 0
  }
```
Run unit tests ...
----

### Step 2

```javascript
  nextTrack() {
    this.songCounter++

    if (this.songCounter == 1)
      this.currentTrack = this.playlist.getNextTrack()
    else
      this.currentTrack = this.playlist.getNextTrack()
  }
```
Run unit tests ...

----

### Step 3

```javascript
  nextTrack() {
     this.currentTrack = this.playlist.getNextTrack()
  }
```
Run unit test ...

----

### Step 4

#### Grouping the double button presses

1. Promote the `playlist` to a global `var playlist` 
2. Move the `playlist.getNextTrack.and.returnValues` to the double-press tests
3. Introduce a new `beforeEach` for the double press tests

To become ... (next slide)

----

```javascript
describe('Given a next track button command', function () {
  beforeEach(function () {
    playlist.getNextTrack.and.returnValues("MyUpbeatSong.mp3", "MyWorkoutSong.mp3")
    audioplayer.nextTrack()
  })

  it('should show the next song in the playlist on display', function () {
    expect(audioplayer.getCurrentSong()).toEqual("play: MyUpbeatSong.mp3")
  })

  describe('When the next track button is pressed again', function () {
    it('should show the third song in the playlist on display', function () {
      audioplayer.nextTrack()
      expect(audioplayer.getCurrentSong()).toEqual("play: MyWorkoutSong.mp3")
    })
  })
})
```

----
### Step 5

#### Make the test(s) use the playlist too!

```javascript
it('should show the first song in the playlist on display', function () {
  expect(
    audioplayer.getCurrentSong()).toEqual("play: " + playlist.getCurrentTrack())
})
```

---

### Our updated plan

- ~~Audio player in initial state~~ &#10003;
- ~~Previous track button~~ &#10003;
- ~~Next track button~~ &#10003;
- ~~Next track button twice~~ &#10003;
- Pressing next and previous

---

### Pressing next and then previous

```javascript
describe('When the previous buttons is pressed', function () {
  it('should show the first song in the playlist on display', function () {
    playlist.getPreviousTrack.and.returnValue("MyGreatSong.mp3")
    audioplayer.previousTrack()
    expect(audioplayer.getCurrentSong()).toEqual("play: MyGreatSong.mp3")
  })
})
```
(Update `playlist` spy obj method array too!)

----

```javascript
previousTrack() {
  this.currentTrack = this.playlist.getPreviousTrack()
}
```

---

### Our updated plan

- ~~Audio player in initial state~~ &#10003;
- ~~Previous track button~~ &#10003;
- ~~Next track button~~ &#10003;
- ~~Next track button twice~~ &#10003;
- ~~Pressing next and previous~~ &#10003;

---

### Possible next steps

- Walk through complete playlist
- Make the play button work
- Make the progress bar do its work (difficult!)
- ...

---

### Retrospective

<ul>
<div>
<li>We applied mocks/spies to what we really own!
</div>
<div class="fragment">
<li>...</li>
</div>
<div class="fragment">
<li>...</li>
</div>
</ul>

---

### References

- [How to write better Jasmine tests with mocks](https://eclipsesource.com/blogs/2014/03/27/mocks-in-jasmine-tests/)
- [Don't mock what you don't own](https://github.com/testdouble/contributing-tests/wiki/Don%27t-mock-what-you-don%27t-own)
- [Examples for using mocks in Jasmine tests](https://gist.github.com/tbuschto/9766267)
- [Mocking calls with Jasmine](https://volaresystems.com/technical-posts/mocking-calls-with-jasmine)

