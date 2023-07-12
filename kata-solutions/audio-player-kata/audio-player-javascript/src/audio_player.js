'use strict';

const PlayPauseButton = {
	PLAY: "play",
	PAUSE: "pause",
}

class AudioPlayer {
  constructor(myPlaylist) {
    this.playlist = myPlaylist
    this.currentTrack = this.playlist.getCurrentTrack()
    this.songCounter = 0
  }

  getCurrentSong() {
    return "play: " + this.currentTrack
  }

  getPlayPauseButtonStatus() {
    return PlayPauseButton.PLAY
  }

  previousTrack() {
    this.currentTrack = this.playlist.previousTrack()
  }
  
  nextTrack() {
      this.currentTrack = this.playlist.nextTrack()
  }
}