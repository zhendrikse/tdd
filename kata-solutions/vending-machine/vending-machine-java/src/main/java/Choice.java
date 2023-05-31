public enum Choice {
  FIZZY_ORANGE ("FIZZY_ORANGE"),
  BEER ("Beer"),
  COLA ("Cola");

  private final String description;

  Choice(String description) {
    this.description = description;
  }

  @Override
  public String toString() {
    return this.description;
  }
}