const PlayPauseButton = {
	PLAY: "play",
	PAUSE: "pause",
}

class AudioPlayer {
  constructor(playlist) {
    this.currentTrack = "MyGreatSong.mp3"
    this.playlist = playlist
  }

  getCurrentSong() {
    return "play: " + this.playlist.getCurrentTrack()
  }

  getPlayPauseButtonStatus() {
    return PlayPauseButton.PLAY
  }

  previousTrack() {}

  nextTrack() {
    this.playlist.nextTrack()
  }
}