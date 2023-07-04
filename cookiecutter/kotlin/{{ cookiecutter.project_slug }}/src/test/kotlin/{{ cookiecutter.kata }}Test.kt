import kotlin.test.*
import org.assertj.core.api.Assertions.*

class {{ cookiecutter.kata }}Test {

  @Test
  fun anInitialTest() {
      val myInstance = {{ cookiecutter.kata }}()
      assertEquals(true, false)
  }
}