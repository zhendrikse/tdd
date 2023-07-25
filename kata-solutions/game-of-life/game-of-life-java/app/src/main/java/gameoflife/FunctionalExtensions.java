package gameoflife;

import java.util.List;
import java.util.function.Predicate;
import java.util.function.BiFunction;

public class FunctionalExtensions {

	public static <T> BiFunction<Predicate<T>, Predicate<T>, Predicate<T>> and() {
		return (predicateLeft, predicateRight) -> predicateLeft.and(predicateRight);
	}

	public static <T> BiFunction<Predicate<T>, Predicate<T>, Predicate<T>> or() {
		return (predicateLeft, predicateRight) -> predicateLeft.or(predicateRight);
	}
  
  public static <T> Predicate<T> which(Predicate<T> leftPredicate,
			BiFunction<Predicate<T>, Predicate<T>, Predicate<T>> combiner, Predicate<T> rightPredicate) {
		return combiner.apply(leftPredicate, rightPredicate);
	}
}