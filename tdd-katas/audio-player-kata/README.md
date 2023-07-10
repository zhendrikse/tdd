# TDD implementation an audio player

## Objectives

- Getting acquainted with somewhat more advanced TDD concepts
  - Mocks, spies, etc.
  - Delegates
  - London school vs Detroit school
- Show how all buttons on the audioplayer can quickly be implemented mocking the delegate(s)

## Description of the functionality

```
now ᴘʟᴀʏɪɴɢ: MyGreatSong.mp3 ───────────⚪────── ◄◄⠀▐▐⠀►► 𝟸:𝟷𝟾 / 𝟹:𝟻𝟼⠀───○ 🔊
```

The audio player boasts the following functions:
- A combined(!) play/pause button
- Buttons for the previous and next tracks
- A display for the current song (and its total duration) 
The display shows the song that is _going to be_ played by preceding it 
by "play:" and preceding it by "now playing:" if the song is currently 
being played.

For this excercise, we assume that a playlist is present and that the 
audio player is looking at the first song in the playlist, but _not_ playing it yet.

The play list consists of the following songs:
- MyGreatSong.mp3
- MyUpbeatSong.mp3
- MyWorkoutSong.mp3
- MyRelaxSong.mp3
- MyFavouriteSong.mp3

## User stories

The first user stories are:
- As a music lover, I want to be able to play my playlist, so that I can enjoy my favourite music.
- As a music lover, I want to be able to press the previous track button endlessly, even if I am already at my first song in the playlist, so that I don't have to worry how many keypress I have to make to get at the start of my playlist.
- The same as above, but then for the next track button.


# Further reading

- [Mocking calls with jasmine](https://volaresystems.com/technical-posts/mocking-calls-with-jasmine)
- [Don't mock what you don't own](https://github.com/testdouble/contributing-tests/wiki/Don%27t-mock-what-you-don%27t-own)
- [Examples for using mocks in Jasmine tests](https://gist.github.com/tbuschto/9766267)
- [Mocking calls with Jasmine](https://volaresystems.com/technical-posts/mocking-calls-with-jasmine)