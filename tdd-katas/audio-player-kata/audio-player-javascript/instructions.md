# Introduction

Please read the general [introduction to the audio player kata](../README.md) first!

# Getting started

## Setting up an empty project

First, create an intial Javascript kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the the newly created project directory and consult
the provided ``README.md`` in there.


## Jasmine prerequisites

- **Creating a [spy object](https://stackoverflow.com/questions/24321307/what-is-the-difference-between-createspy-and-createspyobj)**
  ```javascript
  beforeEach(function() {
    tape = jasmine.createSpyObj('tape', ['play', 'pause', 'stop', 'rewind']);
  
    tape.play();
    tape.pause();
    tape.rewind(0);
  });
  ```

- **Mocking return value**
  ```javascript
  my_object.my_method.and.returnValue("my_return_value")
  ```

- **Mocking subsequent return values**
  ```javascript
  my_object.my_method.and.returnValues("my_return_value1", "my_return_value2")
  ```

- **Calls [with arguments](https://jasmine.github.io/api/edge/Spy#withArgs)**  
    ```javascript
    spyOn(componentInstance, 'myFunction')
        .withArgs(myArg1).and.returnValue(myReturnObj1)
        .withArgs(myArg2).and.returnValue(myReturnObj2);
    ```
- **Verify behaviour**
  ```javascript 
  expect( foo.callMe ).toHaveBeenCalled();
  ```
  
- **Custom matchers**
  
  We can easily introduce custom matchers to let the code express its
  intent even better than the standard matchers allow us to do:
  
  ```javascript
  // demonstrates use of custom matcher
    expect(player).toBePlaying(song);
  ```
  
  For this to work, we just have to define a funtion in our `beforeEach()` step:
  
  ```javascript
  beforeEach(function () {
    jasmine.addMatchers({
      toBePlaying: function () {
        return {
          compare: function (actual, expected) {
            const player = actual;
  
            return {
              pass: player.currentlyPlayingSong === expected && player.isPlaying
            };
          }
        };
      }
    });
  });
  ```

# Implementation

## Preliminary TODO list

Our preliminary TODO list looks as follows:

- [ ] Audio player in initial state 
- [ ] Previous track button
- [ ] Next track button
- [ ] Next track button twice
- [ ] Pressing next and previous


# London school

## The playlist user story

### Step 1: Audio player in initial state

Assume that when we switch on the audio player, it displayes the first song in
the playlist by default.

```javascript
describe('Given a just switched on audioplayer', function () {
  it('shows the first song in the playlist on display', function() {
    audioplayer = new AudioPlayer()
    expect(
      audioplayer.getCurrentSong()).toEqual("play: MyGreatSong.mp3")
  })
})
```

We can easily make this test pass by hardcoding the desired output:

```javascript
class AudioPlayer {
  getCurrentSong() {
    return "play: MyGreatSong.mp3"
  }
}
```

### Step 2: Is the song playing?

```javascript
it('shows the play/pause button in state play', function() {
  var audioplayer = new AudioPlayer()

  expect(
    audioplayer.getPlayPauseButtonStatus()).toEqual(PlayPauseButton.PLAY)
})
```

This forces us to implement a `getPlayPauseButtonStatus()` function:

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

Bearing in mind the red, green, ..., refactor and the DRY principle,
we should rewrite the test code to initialize the audio player in one
location only:

```javascript
describe('Given a just switched on audioplayer', function () {
  beforeEach(function () {
    audioplayer = new AudioPlayer()
  })

  it('shows the first song in the playlist on display', function() {
    expect(
      audioplayer.getCurrentSong()).toEqual("play: MyGreatSong.mp3")   
    })

  it('shows the play/pause button in state play', function(){
    expect(audioplayer.getPlayPauseButtonStatus()).toEqual(PlayPauseButton.PLAY)
  })
})
```

With which we can check one item off of our TODO list:

- Audio player in initial state &#10003;
- Previous track button
- Next track button
- Next track button twice
- Pressing next and previous

### Step 3: Previous track button

As the audio player starts with the first song in the playlist by default,
a press on the previous track button should not have any effects (yet).

```javascript
describe('When the previous track button is pressed', function() {
  it('simply ignores the press', function() {
      spyOn(audioplayer, "previousTrack")
      audioplayer.previousTrack()
      expect(audioplayer.previousTrack).toHaveBeenCalled();
  })
})
```

We can make this test pass by adding the new method:

```javascript
  previousTrack() {}
```

This means we may remove one more item from our TODO list.

- ~~Audio player in initial state~~ &#10003;
- ~~Previous track button~~ &#10003;
- Next track button
- Next track button twice
- Pressing next and previous


### Step 4: Next track button

```javascript
describe('When the next track button is pressed', function () {
  it('shows the next song in the playlist on display', function () {
    audioplayer.nextTrack()
    expect(audioplayer.getCurrentSong()).toEqual("play: MyUpbeatSong.mp3")
  })
})
```

which requires us to extend the production code

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

and our TODO becomes:

- ~~Audio player in initial state~~ &#10003;
- ~~Previous track button~~ &#10003;
- ~~Next track button~~ &#10003;
- Next track button twice
- Pressing next and previous

### Step 5: Next track _once more_

```javascript
describe('When the next track button is pressed twice', function () {
  it('shows the third song in the playlist on display', function () {
    audioplayer.nextTrack()
    audioplayer.nextTrack()
    expect(audioplayer.getCurrentSong()).toEqual("play: MyWorkoutSong.mp3")
  })
})
```

Let's first make this test pass in the most clumsy way we can think of:

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

But obviously this immediately makes some serious refactoring inevitable!

### Step 6: Introduction of a playlist collaborator

1. We first introduce a mock in small increments:
   ```javascript
     beforeEach(function () {
       playlist = jasmine.createSpyObj('playlist',
         ['getCurrentTrack', 'nextTrack', 'previousTrack'])
       playlist.getCurrentSong.and.returnValues("MyFavouriteSong.mp3", "MyUpbeatSong.mp3", "MyWorkoutSong.mp3")  
       audioplayer = new AudioPlayer(playlist)
     })
   ```
   and modify the `AudioPlayer` class accordingly:

    ```javascript
    class AudioPlayer {
      constructor(myPlaylist) {
        this.playlist = myPlaylist
        this.currentTrack = this.playlist.getCurrentTrack()
        this.songCounter = 0
      }
    ```

2. Use the playlist in the `nextTrack()` method:

   First we set up our mock
   ```javascript
   playlist.nextTrack.and.returnValues("MyUpbeatSong.mp3", "MyWorkoutSong.mp3")
   ```
   which can then be used in our implementation of `nextTrack()`:
    ```javascript
      nextTrack() {
        this.songCounter++
    
        if (this.songCounter == 1)
          this.currentTrack = this.playlist.getNextTrack()
        else
          this.currentTrack = this.playlist.getNextTrack()
      }
    ```
    which simplifies to
    
    ```javascript
      nextTrack() {
         this.currentTrack = this.playlist.getNextTrack()
      }
    ```
    
3. Grouping the double button presses

    1. Promote the `playlist` to a global `var playlist` 
    2. Move the `playlist.nextTrack.and.returnValues` to the double-press tests
    3. Introduce a new `beforeEach` for the double press tests

    ```javascript
    describe('Given a next track button command', function () {
      beforeEach(function () {
        playlist.nextTrack.and.returnValues("MyUpbeatSong.mp3", "MyWorkoutSong.mp3")
        audioplayer.nextTrack()
      })
    
      it('shows the next song in the playlist on display', function () {
        expect(audioplayer.getCurrentSong()).toEqual("play: MyUpbeatSong.mp3")
      })
    
      describe('When the next track button is pressed again', function () {
        it('shows the third song in the playlist on display', function () {
          audioplayer.nextTrack()
          expect(audioplayer.getCurrentSong()).toEqual("play: MyWorkoutSong.mp3")
        })
      })
    })
    ```
    
4. Make the test(s) use the playlist too!

    ```javascript
    it('shows the first song in the playlist on display', function () {
      expect(
        audioplayer.getCurrentSong()).toEqual("play: " + playlist.getCurrentTrack())
    })
    ```

5. Updated our plan
    
    - ~~Audio player in initial state~~ &#10003;
    - ~~Previous track button~~ &#10003;
    - ~~Next track button~~ &#10003;
    - ~~Next track button twice~~ &#10003;
    - Pressing next and previous
    

### Step 7: Pressing next and then previous

```javascript
describe('When the previous button is pressed', function () {
  it('shows the first song in the playlist on display', function () {
    playlist.previousTrack.and.returnValue("MyGreatSong.mp3")
    audioplayer.previousTrack()
    expect(audioplayer.getCurrentSong()).toEqual("play: MyGreatSong.mp3")
  })
})
```
Don't forget to update `playlist` spy obj method array too!

Let's extend our production code accordingly

```javascript
previousTrack() {
  this.currentTrack = this.playlist.previousTrack()
}
```

This also means we have completed our TODO list!

- ~~Audio player in initial state~~ &#10003;
- ~~Previous track button~~ &#10003;
- ~~Next track button~~ &#10003;
- ~~Next track button twice~~ &#10003;
- ~~Pressing next and previous~~ &#10003;


## Next steps

- [ ] Walk through complete playlist
- [ ] Make the play button work
- [ ] Make the progress bar do its work (difficult!)
- ...

