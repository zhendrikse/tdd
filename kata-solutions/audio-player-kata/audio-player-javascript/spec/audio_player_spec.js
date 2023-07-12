describe('Given a just switched on audioplayer', function () {
  var playlist = jasmine.createSpyObj('playlist',
      ['getCurrentTrack', 'nextTrack', 'previousTrack'])
  
  beforeEach(function () {
    playlist.getCurrentTrack.and.returnValue("MyGreatSong.mp3")
    playlist.nextTrack.and.returnValues("MyUpbeatSong.mp3", "MyWorkoutSong.mp3")
    
    audioplayer = new AudioPlayer(playlist)
  })

  it('shows the first song in the playlist on display', function() {
    expect(
        audioplayer.getCurrentSong()).toEqual("play: " + playlist.getCurrentTrack())
    })

  it('shows the play/pause button in state play', function(){
    expect(audioplayer.getPlayPauseButtonStatus()).toEqual(PlayPauseButton.PLAY)
  })
  
  describe('When the previous track button is pressed', function() {
    it('simply ignores the button press', function() {
        spyOn(audioplayer, "previousTrack")
        audioplayer.previousTrack()
        expect(audioplayer.previousTrack).toHaveBeenCalled();
    })
  })
  
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
    
    describe('When the previous button is pressed', function () {
      it('shows the first song in the playlist on display', function () {
        playlist.previousTrack.and.returnValue("MyGreatSong.mp3")
        audioplayer.previousTrack()
        expect(audioplayer.getCurrentSong()).toEqual("play: MyGreatSong.mp3")
      })
    })
  })
  
})