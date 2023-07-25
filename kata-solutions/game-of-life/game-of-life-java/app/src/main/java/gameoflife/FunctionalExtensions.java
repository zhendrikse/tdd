package gameoflife;

import java.util.List;
import java.util.function.Predicate;
import java.util.function.BiFunction;

public class FunctionalExtensions {

	public static BiFunction<Predicate<String>, Predicate<String>, Predicate<String>> and = 
      (leftPredicate, rightPredicate) -> leftPredicate.and(rightPredicate);

	public static BiFunction<Predicate<String>, Predicate<String>, Predicate<String>> or = 
      (leftPredicate, rightPredicate) -> leftPredicate.or(rightPredicate);

  public static <T> Predicate<T> which(Predicate<T> leftPredicate,
			BiFunction<Predicate<T>, Predicate<T>, Predicate<T>> combiner, Predicate<T> rightPredicate) {
		return combiner.apply(leftPredicate, rightPredicate);
	}
}