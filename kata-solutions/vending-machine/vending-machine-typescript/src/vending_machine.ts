export enum Choice {
  Cola = "Cola choice",
  FizzyOrange = "Fizzy orange choice",
  Beer = "BEER choice"
}

export enum Can {
  Nothinbg = "No can",
  Coke = "Can of Coke",
  Fanta = "Can of Fanta"
}

class Cashier {
  constructor(private balanceInCents: number = 0) {}  

  public insert(amountInCents: number) {
    this.balanceInCents += amountInCents
  }

  public doesBalanceAllow(priceInCents: number) {
    return this.balanceInCents >= priceInCents
  }

  public buy(amountInCents: number) {
    this.balanceInCents -= amountInCents
  }
}

class Drawer {
  constructor(public can: Can, public priceInCents: number) {}

  deliver(cashier: Cashier) {
    if (!cashier.doesBalanceAllow(this.priceInCents))
      return Can.Nothinbg
    
    cashier.buy(this.priceInCents)
    return this.can    
  }
}

export class VendingMachine {
    private choiceDrawerMap: Map<Choice, Drawer> = new Map<Choice, Drawer>()
    private cashier: Cashier = new Cashier()

    public configure(choice: Choice, can: Can, priceInCents = 0): void {
      this.choiceDrawerMap.set(choice, new Drawer(can, priceInCents))
    }

    public insert(amountInCents: number): void  {
      this.cashier.insert(amountInCents)
    }
  
    public deliver(choice: Choice): Can {
      if (!this.choiceDrawerMap.has(choice))
          return Can.Nothinbg

      let drawer = this.choiceDrawerMap.get(choice) as Drawer
      return drawer.deliver(this.cashier)
    }
}
