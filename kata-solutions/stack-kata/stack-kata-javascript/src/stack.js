export class Stack {
  #size
  #element

  constructor() {
    this.#size = 0;
    this.#element = [];
  }

  isEmpty() {
    return this.#size == 0;
  }

  pop() {
    if (this.isEmpty()) throw new Error("Stack underflow");

    return this.#element[--this.#size];
  }

  push(newElement) {
    this.#element[this.#size++] = newElement;
  }
}
