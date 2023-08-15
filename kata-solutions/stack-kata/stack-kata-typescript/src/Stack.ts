'use strict';

export class Stack {
  size: number = 0
  element: Array<number> = new Array()

  isEmpty(): boolean {
    return this.size == 0
  }

  pop(): number {
    if (this.isEmpty())
      throw new Error("Stack underflow")
    
    return this.element[--this.size]
  }

  push(newElement: number): void {
    this.element[this.size++] = newElement
  }
}
