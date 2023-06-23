import kotlin.test.*
import org.assertj.core.api.Assertions.*

class {{ cookiecutter.kata }}Test {

  @Test
  fun anInitialTest() {
      val bla = {{ cookiecutter.kata }}()
      assertEquals(true, false)
  }
}