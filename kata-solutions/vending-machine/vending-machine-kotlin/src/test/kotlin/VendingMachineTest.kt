import kotlin.test.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.api.BeforeEach 

class FreeDrinksVendingMachineTest() {
  private var vendingMachine: VendingMachine = VendingMachine()
  
  @BeforeEach
  internal fun initVendingMachine() {
      vendingMachine = VendingMachine()
      vendingMachine.configure(Choice.FIZZY_ORANGE, Can.FANTA)
      vendingMachine.configure(Choice.COLA, Can.COKE)
  }
  
  @Test
  fun aNewVendingMachineDeliversNothingWhenItIsUnconfigured() {
      assertEquals(vendingMachine.deliver(Choice.WATER), Can.NOTHING)
  }

  @Test
  fun aNewVendingMachineDeliversCokeWhenColaIsChosen() {
      assertEquals(vendingMachine.deliver(Choice.COLA), Can.COKE)
  }

  @Test
  fun aNewVendingMachineDeliversFantaWhenFizzyOrangeIsChosen() {
      assertEquals(vendingMachine.deliver(Choice.FIZZY_ORANGE), Can.FANTA)
  }
}

class PaidDrinksVendingMachineTest() {
    private var vendingMachine: VendingMachine = VendingMachine()
    
    @BeforeEach
    internal fun initVendingMachine() {
        vendingMachine = VendingMachine()
        vendingMachine.configure(Choice.FIZZY_ORANGE, Can.FANTA, 200)
        vendingMachine.configure(Choice.COLA, Can.COKE, 250)
    }

    @Test
    fun aPaidVendingMachineDoesNotDeliversCokeWhenColaIsChosen() {
      assertEquals(vendingMachine.deliver(Choice.COLA), Can.NOTHING)
    }
  
    @Test
    fun aPaidVendingMachineDeliversCokeWhenColaIsPaid() {
      vendingMachine.insertMoney(250)
      assertEquals(vendingMachine.deliver(Choice.COLA), Can.COKE)
    }
  
    @Test
    fun aPaidVendingMachineDeliversFantaWhenFizzyOrangeIsPaid() {
      vendingMachine.insertMoney(200)
      assertEquals(vendingMachine.deliver(Choice.FIZZY_ORANGE), Can.FANTA)
    }
  
    @Test
    fun aPaidVendingMachineDoesNotDeliverFantaTwiceWhenOneIsPaid() {
      vendingMachine.insertMoney(200)
      vendingMachine.deliver(Choice.FIZZY_ORANGE)
      assertEquals(vendingMachine.deliver(Choice.FIZZY_ORANGE), Can.NOTHING)
    }
  }  