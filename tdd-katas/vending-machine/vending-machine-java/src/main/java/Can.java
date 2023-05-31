public enum Can {
  COKE ("Coke"),
  FANTA ("Fanta"),
  NOTHING ("Nothing");

  private final String description;

  Can(String description) {
    this.description = description;
  }

  @Override
  public String toString() {
    return this.description;
  }
}