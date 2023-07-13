package hotel;

public enum Room {
  BLUE_ROOM("Blue room"),
  RED_ROOM("Red room"),
  GREEN_ROOM("Green room"),
  YELLOW_ROOM("Yellow room"),
  BROWN_ROOM("Brown room");

  private String name;

  Room(final String name) {
    this.name = name;
  }

  @Override
  public String toString() {
    return name;
  }
}