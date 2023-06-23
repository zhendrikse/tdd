'use strict';

export enum Choice {
  COLA = "Cola choice",
  FIZZY_ORANGE = "Fizy orange choice",
  BEER = "Beer choice"
}

export enum Can {
  NOTHING = "No can",
  COKE = "Can of Coke",
  FANTA = "Can of Fanta"
}

export class VendingMachine {
    private choiceCanMap: Map<Choice, Can> = new Map<Choice, Can>();

    public configure(choice: Choice, can: Can): void {
      this.choiceCanMap.set(choice, can)
    }
  
    public deliver(choice: Choice): Can {
      if (!this.choiceCanMap.has(choice)) return Can.NOTHING

      return this.choiceCanMap.get(choice) as Can        
    }
}
