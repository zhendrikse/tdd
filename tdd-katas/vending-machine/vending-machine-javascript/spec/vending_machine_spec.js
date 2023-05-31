describe("A vending machine", function() {
  var vendingMachine

  beforeEach(function () {
    vendingMachine = new VendingMachine()
    vendingMachine.provision(Choice.FIZZY_ORANGE, Can.FANTA)
    vendingMachine.provision(Choice.COLA, Can.COKE)
  })

  it("delivers nothing when asked for a non-existing choice", function () {
    expect(vendingMachine.deliver(Choice.BEER)).toEqual(Can.NOTHING)
  })

  it("delivers cola when asked for a can of coke", function () {
    expect(vendingMachine.deliver(Choice.COLA)).toEqual(Can.COKE)
  })

  it("delivers fanta when asked for a can of fizzy orange", function () {
    expect(vendingMachine.deliver(Choice.FIZZY_ORANGE)).toEqual(Can.FANTA)
  })
  
})
