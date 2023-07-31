public enum Choice {
  FIZZY_ORANGE ("Fizzy orange choice"),
  BEER ("Beer choice"),
  COLA ("Cola choice");

  private final String description;

  Choice(String description) {
    this.description = description;
  }

  @Override
  public String toString() {
    return this.description;
  }
}