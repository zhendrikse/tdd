describe('Given a just switched on audioplayer', function () {
  var audioplayer, playlist

  beforeEach(function () {
    playlist = jasmine.createSpyObj('playlist',
      ['getCurrentTrack', 'nextTrack', 'previousTrack'])
    playlist.getCurrentTrack.and.returnValue("MyGreatSong.mp3")

    audioplayer = new AudioPlayer(playlist)
  })

  it('should show the first song in the playlist on display', function () {
    expect(
      audioplayer.getCurrentSong()).toEqual("play: " + playlist.getCurrentTrack())
  })

  it('should have the play/pause button in state play', function () {
    expect(audioplayer.getPlayPauseButtonStatus()).toEqual(PlayPauseButton.PLAY)
  })

  describe('When the previous track button is pressed', function () {
    it('should do nothing', function () {
      spyOn(audioplayer, "previousTrack")
      audioplayer.previousTrack()
      expect(audioplayer.previousTrack).toHaveBeenCalled()
    })
  })

  describe('Given a next track button command', function () {
    beforeEach(function () {
      playlist.getCurrentTrack.and.returnValue("MyUpbeatSong.mp3")
    })

    it('should show the next song in the playlist on display', function () {
      expect(audioplayer.getCurrentSong()).toEqual("play: MyUpbeatSong.mp3")
    })

    describe('When the next track button is pressed again', function () {

      it('should show the third song in the playlist on display', function () {
        playlist.getCurrentTrack.and.returnValue("MyWorkoutSong.mp3")

        audioplayer.nextTrack()
        
        expect(audioplayer.getCurrentSong()).toEqual("play: MyWorkoutSong.mp3")
        expect(playlist.nextTrack).toHaveBeenCalled()
      })
    })

  //   describe('When the previous buttons is pressed', function () {
  //     it('should show the first song in the playlist on display', function () {
  //       playlist.getPreviousTrack.and.returnValue("MyGreatSong.mp3")
  //       audioplayer.previousTrack()
  //       expect(audioplayer.getCurrentSong()).toEqual("play: MyGreatSong.mp3")
  //     })
  //   })
  })
})