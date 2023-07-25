package gameoflife;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.function.BiFunction;

import static gameoflife.FunctionalExtensions.*;

class FunctionalExtensionsTest {

	private static final String AAP = "Aap";
	private static final String NOOT = "Noot";
	private static final String MIES = "Mies";
	private static final String WIM = "Wim";
	private static final String ZUS = "Zus";
	private static final String JET = "Jet";
	private static final String FILTER_VALUE = WIM;
  

	private static final List<String> READING_SHELF = List.of(AAP, NOOT, MIES, WIM, ZUS, JET);
  private static final Predicate<String> isWim = word -> word.equals(WIM);
  private static final Predicate<String> isMies = word -> word.equals(MIES);
  
  // @Test
  // void orBiFunctionCombinesPredicates() {
  //   List<String> filteredList = READING_SHELF
  //     .stream()
  //     .filter(or().apply(isMies(), isWim()))
  //     .collect(Collectors.toList());

  //   assertEquals(2, filteredList.size());
  //   assertTrue(filteredList.contains(WIM));
  //   assertTrue(filteredList.contains(MIES));
  // }
  
  @Test
  void andBiFunctionCombinesPredicates() {
    List<String> filteredList = READING_SHELF
      .stream()
      .filter(isMies.and(isWim))
      .collect(Collectors.toList());

    assertTrue(filteredList.isEmpty());
  }
 
  @Test
  void whichFunctionCombinesPredicates() {
    List<String> filteredList = READING_SHELF
      .stream()
      .filter(which(isMies, or(), isWim))
      .collect(Collectors.toList());

    assertEquals(2, filteredList.size());
    assertTrue(filteredList.contains(WIM));
    assertTrue(filteredList.contains(MIES));
  }
}