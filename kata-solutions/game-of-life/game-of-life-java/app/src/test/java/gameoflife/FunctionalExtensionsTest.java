package gameoflife;

import static gameoflife.FunctionalExtensions.and;
import static gameoflife.FunctionalExtensions.or;
import static gameoflife.FunctionalExtensions.which;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;

import org.junit.jupiter.api.Test;

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
  
  @Test
  void orBiFunctionCombinesPredicates() {
    List<String> filteredList = READING_SHELF
      .stream()
      .filter(or().apply(word -> word.equals(WIM), word -> word.equals(MIES)))
      .collect(Collectors.toList());

    assertEquals(2, filteredList.size());
    assertTrue(filteredList.contains(WIM));
    assertTrue(filteredList.contains(MIES));
  }
  
  @Test
  void andBiFunctionCombinesPredicates() {
    List<String> filteredList = READING_SHELF
      .stream()
      .filter(and().apply(word -> word.equals(WIM), word -> word.equals(MIES)))
      .collect(Collectors.toList());

    assertTrue(filteredList.isEmpty());
  }
 
  @Test
  void whichFunctionCombinesOrPredicates() {
    List<String> filteredList = READING_SHELF
      .stream()
      .filter(which(isMies, or(), isWim))
      .collect(Collectors.toList());

    assertEquals(2, filteredList.size());
    assertTrue(filteredList.contains(WIM));
    assertTrue(filteredList.contains(MIES));
  }
 
  @Test
  void whichFunctionCombinesAndPredicates() {
    List<String> filteredList = READING_SHELF
      .stream()
      .filter(which(isMies, and(), isWim))
      .collect(Collectors.toList());

    assertTrue(filteredList.isEmpty());
  }
}