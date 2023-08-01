import kotlin.test.*
import org.assertj.core.api.Assertions.*
import org.junit.jupiter.api.BeforeEach 

class VendingMachineTest() {
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