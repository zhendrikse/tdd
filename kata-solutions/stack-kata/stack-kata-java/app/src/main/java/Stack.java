public class Stack {
  private Plate[] plates = new Plate[2];
  int size = 0;
  
  public boolean isEmpty() {
    return this.size == 0;
  }

  public void push(Plate plate) {
     
     this.plates[this.size++] = plate;
  }

  public Plate pop() {
     if (isEmpty()) {
       throw new RuntimeException("Stack underflow");
     }
    
     return this.plates[--this.size];
  }
}