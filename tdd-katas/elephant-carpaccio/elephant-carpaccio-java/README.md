# Instructions

# Getting started

First, create an initial Java kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).
We suggest naming the kata `OrderPriceCalculator`.

Add the following snippet to the `build.gradle.kts`, so that you can generate an executable JAR:

```kotlin
tasks.jar {
    manifest.attributes["Main-Class"] = "OrderPriceCalculator"
}
```

## Creating an executable JAR

We should now be able to create an executable JAR by invoking

```bash
$ ./gradlew jar
```

We can execute this JAR by invoking

```bash
$ java -jar build/libs/orderpricecalculator.jar
```

# A possible solution

## Value of an order

### **User story I**: Print "Welcome to the order price calculator"
---

> As a user I want to invoke the order price calculator so that I know I can use it.

<details>
  <summary>Calculator shows start-up message</summary>

Let's write a test first:

```java
class OrderPriceCalculatorTest {
    @Test 
    void calculatorShowsStartUpMessage() {
        OrderPriceCalculator calculator = new OrderPriceCalculator();
        assertEquals("Welcome to the order price calculator!", calculator.getStartUpMessage());
    }
}
```

and make it pass

```java
public class OrderPriceCalculator {
    public String getStartUpMessage() {
        return "Welcome to the order price calculator!";
    }
    // ...
```

For the calculator, in the `main()` we add

```java
public static void main(String[] args) {
    final OrderPriceCalculator calculator = new OrderPriceCalculator();
    System.out.println(calculator.getStartUpMessage());
}
```

Finally, we need to verify the output when we run the executable JAR file:

```bash
$ java -jar build/libs/orderpricecalculator.jar 
Picked up JAVA_TOOL_OPTIONS:  -Xmx3489m
Welcome to the order price calculator!
```

</details>

### **User story II**: Echo input parameters
---

> As a user I want to see the input parameters echoed so that I know the calculator parsed them correctly.

Since the sprints are only eight minutes during this kata, let's for the input to fall back to a manual test only.

<details>
  <summary>Echo input parameters</summary>

Let's collect all parameters into one value (i.e. immutable) object:

```java
public class InputParameters {
    public final int quantity;
    public final double price;
    public final String state;

    public InputParameters(final int quantity, final double price, final String state) {
        this.quantity = quantity;
        this.price = price;
        this.state = state;
    }

    public String toString() {
        return "Quantity: " + quantity + ", Price: " + price + ", State: " + state;
    }
}
```

With this object, we can easily read the input parameters from the command line

```java
    // ...

    public InputParameters readInputParameters() {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("How many items: ");
            Integer numberOfItems = scanner.nextInt();

            System.out.print("Price item: ");
            Double pricePerItem = scanner.nextDouble();

            System.out.print("Two-letter state code: ");
            String stateCode = scanner.next();

            return new InputParameters(numberOfItems, pricePerItem, stateCode);
        }
    }

    public static void main(String[] args) {
        final OrderPriceCalculator calculator = new OrderPriceCalculator();
        System.out.println(calculator.getStartUpMessage());
        System.out.println(calculator.readInputParameters());
    }
}
```
</details>

### **User story III**: calculate the order value
---

> As a user I want to calculate the order value so that I know the total order price.

<details>
<summary>Order value calculation</summary>

Let's write a test first!

```java
@Test
void calculatesOrderValue() {
    assertEquals(690.0, calculator.calculateOrderValue(2, 345.00));
}
```

We can make this test pass by adding the `calculateOrderValue()` method to the production code:

```java
double calculateOrderValue(final int quantity, final double price) {
    return quantity * price;
}
```

Finally, this should also be echoed on the console:

```java
public static void main(String[] args) {
    final OrderPriceCalculator calculator = new OrderPriceCalculator();
    System.out.println(calculator.getStartUpMessage());

    final InputParameters input = calculator.readInputParameters();
    System.out.println(input);
    System.out.println("Order value: " + calculator.calculateOrderValue(input.quantity, input.price));
}
```
</details>

## State taxes

### **User story IV**: calculate the tax for one state
---

> As a user I want to calculate the taxes in the state of Utah so that I serve my products in Utah.

<details>
<summary>Selling products in Utah</summary>

Let's write a test first!

```java
@Test
void calculatesTaxesInUtah() {
    OrderPriceCalculator classUnderTest = new OrderPriceCalculator();
    assertEquals(47.265, classUnderTest.calculateTax(new InputParameters(2, 345.00, "UT")));
}
```

We can make this test pass by adding the `calculateTax()` method to the production code:

```java
double calculateTax(final InputParameters input) {
    return calculateOrderValue(input.quantity, input.price) * 6.85 * 0.01;
}
```

Finally, this should also be echoed on the console:

```java
public static void main(String[] args) {
    final OrderPriceCalculator calculator = new OrderPriceCalculator();
    System.out.println(calculator.getStartUpMessage());

    final InputParameters input = calculator.readInputParameters();
    System.out.println(input);
    System.out.println("Order value: " + calculator.calculateOrderValue(input.quantity, input.price));
    System.out.println("Tax amount: " + calculator.calculateTax(input));
}
```

</details>

### **User story V**: calculate the tax for two states
---

> As a user I want to calculate the taxes in the state Nevada so that I serve my products in Nevada.

<details>
<summary>Selling products in Nevada</summary>

Let's write a test first!

```java
@Test
void calculatesTaxesInNevada() {
    OrderPriceCalculator classUnderTest = new OrderPriceCalculator();
    assertEquals(classUnderTest.calculateTax(55.20, new InputParameters(2, 345.00, "NV")));
}
```

We make this test pass easily

```java
double calculateTax(final InputParameters input) {
    if (input.state.equals("UT"))
        return calculateOrderValue(input.quantity, input.price) * 6.85 * 0.01;

    return calculateOrderValue(input.quantity, input.price) * 8.00 * 0.01;
}
```

No further changes in the `main()` method are needed at this point.

</details>

### **User story VI**: calculate the tax for all states
---

> As a user I want to calculate the taxes in all five states so that I serve my products everywhere.

<details>
<summary>Selling products in all five states</summary>

Let's write a test first!

```java
@Test 
void calculatesTaxesInTexas() {
    assertEquals(43.125, calculator.calculateTax(new InputParameters(2, 345.00, "TX")));
}
```

We make this test pass by

```java
public double calculateTax(final InputParameters input) {
    if (input.state.equals("UT"))
        return calculateOrderValue(input.quantity, input.price) * 6.85 * 0.01;
    else if (input.state.equals("TX"))
        return calculateOrderValue(input.quantity, input.price) * 6.25 * 0.01;

    return calculateOrderValue(input.quantity, input.price) * 8.00 * 0.01;
}
```

which can then easily be refactored to

```java
public class OrderPriceCalculator {
    private Map<String, Double> stateTaxMap = new HashMap<>();

    // ...

    double calculateTax(final InputParameters input) {
        return calculateOrderValue(input.quantity, input.price) * stateTaxMap.get(input.state) * 0.01;
    }

    public void configure(String state, double tax) {
        stateTaxMap.put(state, tax);
    }

    public static void main(String[] args) {
        final OrderPriceCalculator calculator = new OrderPriceCalculator();
        calculator.configure("UT", 6.85);
        calculator.configure("NV", 8.00);
        calculator.configure("TX", 6.25);
        calculator.configure("AL", 4.00);
        calculator.configure("CA", 8.25);
    
        // ...
```
</details>

## Discounts

### **User story VIII**: discounts for order prices &gt; 1000 and &lt; 5000
---

> As a user I want to know the discount value for orders &gt; 1000 and &lt; 5000 so that I can get my discount.

<details>
<summary>Discounts for orders &gt; 1000 &lt; 5000</summary>

Let's write a test first!

```java
@Test
void calculatesDiscountForOverrOneThousand() {
    assertEquals(20.70, calculator.calculateDiscountValue(10, 345.00), 0.001);
}
```

and the production code to make the test pass

```java
double calculateDiscountValue(final int quantity, final double price) {
    return 0.03 * quantity * price;
}
```

Obviously we need to test also that this discount is not applied for
prices less than 1000,00: 

```java
@Test
void calculatesDiscountForUnderOneThousand() {
    assertEquals(0.0, calculator.calculateDiscountValue(2, 345.00), 0.001);
}
```

so the modified `calculateDiscountValue` becomes:

```java
double calculateDiscountValue(final int quantity, final double price) {
    final double orderValue = calculateOrderValue(quantity, price);
    if (orderValue < 1000) return 0.0;
    return 0.01 * 3 * orderValue; 
}
```

The production code needs to show the result as well:

```java
public static void main(String[] args) {
    final OrderPriceCalculator calculator = new OrderPriceCalculator();

    // ...
    System.out.println("Order value: " + calculator.calculateOrderValue(input.quantity, input.price));
    System.out.println("Discount: " + calculator.calculateDiscountValue(input.quantity, input.price));
    System.out.println("Tax amount: " + calculator.calculateTax(input));
}
```

Now we notice that the tax is not calculated based on the discounted value, but it should!

Let's write a test for that case

```java
@Test
void calculatesTaxesBasedOnDiscountedPrice() {
    calculator.configureDiscount(1000, 0);
    calculator.configureDiscount(5000, 3);
    assertEquals(267.72, calculator.calculateTax(new InputParameters(10, 345.00, "NV")), 0.01);
}
```

This forces us to modify the calculation of the taxes

```java
double calculateTax(final InputParameters input) {
    final double discountedValue = calculateOrderValue(input.quantity, input.price) - calculateDiscountValue(input.quantity, input.price);
    return discountedValue * stateTaxMap.get(input.state) * 0.01;
}
```
</details>

### **User story IX**: discounts for order prices &gt; 1000 and &lt; 5000
---

> As a user I want to know the discount value for orders &gt; 1000 and &lt; 5000 so that I can get my discount.

<details>
<summary>Discounts for orders &gt; 1000 &lt; 5000</summary>

Let's write a test first!

```java
@Test
void calculatesDiscountForOverFiveThousand() {
    assertEquals(345.0, calculator.calculateDiscountValue(20, 345.00), 0.001);
}
```

and the code to make this test pass

```java
double calculateDiscountValue(final int quantity, final double price) {
    final double orderValue = calculateOrderValue(quantity, price);
    if (orderValue < 1000) return 0.0;
    if (orderValue < 5000) return 0.01 * 3 * orderValue;
    return 0.01 * 5 * orderValue; 
}
```
</details>


### **User story X**: discounts for order prices in general
---

> As a user I want to know the discount value for orders in general so that I can get my discount.

<details>
<summary>Discounts for orders in general</summary>

Let's write a test first!

```java
@Test
void calculatesDiscountForOverSevenThousand() {
    assertEquals(603.75, calculator.calculateDiscountValue(25, 345.00), 001);
}
```

with implementation

```java
double calculateDiscountValue(final int quantity, final double price) {
    final double orderValue = calculateOrderValue(quantity, price);
    if (orderValue < 1000) return 0.01 * 0 * orderValue;
    if (orderValue < 5000) return 0.01 * 3 * orderValue;
    if (orderValue < 7000) return 0.01 * 5 * orderValue;
    return 0.01 * 7 * orderValue; 
}
```

This can then easily be generalized:

```java
public class OrderPriceCalculator {    
    private Map<String, Double> stateTaxMap = new HashMap<>();
    private Map<Integer, Integer> discountsMap = new TreeMap<>();

    public void configureDiscount(final int upperLimit, final int percentage) {
        discountsMap.put(upperLimit, percentage);
    }

    double calculateDiscountValue(final int quantity, final double price) {
        final double orderValue = calculateOrderValue(quantity, price);
        for (Entry<Integer, Integer> entry : discountsMap.entrySet()) 
            if (orderValue < entry.getKey()) 
                return 0.01 * entry.getValue() * orderValue;
       
        return 0.0;
    }

    // ...
```
</details>

### **User story XI**: total price
---

> As a user I want to get the total price so that I can directly use it.

<details>
<summary>Total price</summary>

Let's write a test first!

```java
@Test
void calculatesTotalOrderValue() {
    calculator.configureTax("UT", 6.85);
    calculator.configureDiscount(1000, 0);
    calculator.configureDiscount(5000, 3);
    assertEquals(3575.73525, calculator.calculateGrandTotal(new InputParameters(10, 345.00, "UT")), 0.01);
}
```

We make this test pass by adding a `calculateGrandTotal()` method

```java
double calculateGrandTotal(final InputParameters input)  {
    return calculateOrderValue(input.quantity, input.price) - calculateDiscountValue(input.quantity, input.price) + calculateTax(input);
}
```

By invoking this method in the `main()`, we get the desired endresult:

```java
public static void main(String[] args) {
    // ...

    final InputParameters input = calculator.readInputParameters();
    System.out.println(input);
    System.out.println("Order value: " + calculator.calculateOrderValue(input.quantity, input.price));
    System.out.println("Discount: " + calculator.calculateDiscountValue(input.quantity, input.price));
    System.out.println("Tax amount: " + calculator.calculateTax(input));
    System.out.println("Grand total: " + calculator.calculateGrandTotal(input));
}
```
</details>

### **User story XII**: rounding off
---

> As a user I want to get prices rounded off so that I can directly use them.

<details>
<summary>Rounding off prices</summary>

Let's write a test first!

```java
@Test
void calculatesRoundedTotalOrderValue() {
    calculator.configureTax("UT", 6.85);
    calculator.configureDiscount(1000, 0);
    calculator.configureDiscount(5000, 3);
    assertEquals(3575.74, calculator.calculateRoundedGrandTotal(new InputParameters(10, 345.00, "UT")), 0.01);
}
```

We make this test pass by adding a `calculateRoundedGrandTotal` method

```java
double calculateRoundedGrandTotal(final InputParameters input) {
    return  Math.round(100 * calculateGrandTotal(input)) / 100.0;
}
```

By invoking this method in the `main()`, we get the desired endresult:

```java
public static void main(String[] args) {
    // ...

    System.out.println("Tax amount: " + calculator.calculateTax(input));
    System.out.println("Grand total: " + calculator.calculateRoundedGrandTotal(input));
}
```

</details>


## Validating input

Note that we did not provide any logic for invalid state codes.
The most likely thing to do is to throw an `UnsupportedStateException`.

However, it may be even better to ask your product owner what the calculator
is supposed to do in these cases!

Likewise, we probably also want to validate the other two input fields.
For example, we should not be able to enter zero or even a negative amount
of items. And should there also be a maximum?

The same holds for the prices of products, these can never be
negative!

### **User story XIII**: invalid state codes
---

> As a user I want to get notified of invalid state codes so that I can correct my input.

<details>
<summary>Invalid state codes</summary>

Let's write a test first!

```java
@Test 
void letsUserKnowThatStateCodeIsinvalid() {
    IllegalArgumentException thrown = assertThrows(
        IllegalArgumentException.class,
        () -> calculator.calculateTax(new InputParameters(2, 345.00, "99")),
        "Expected calculateTax() to throw, but it didn't"
        );
}
```

We can make this test pass by introducing an enumeration for the state codes:

```java
enum State {
    NY,
    TX,
    NV,
    CA,
    AL,
    UT
}
```

And removing the [primitive obsession](https://refactoring.guru/smells/primitive-obsession) code smells in the `InputParameters`, `OrderPriceCalculator`, and `OrderPriceCalculatorTest`

```java
public class InputParameters {
    public final int quantity;
    public final double price;
    public final State state;

    public InputParameters(final int quantity, final double price, final String state) {
        this.quantity = quantity;
        this.price = price;
        this.state = State.valueOf(state);
    }

    // ...
```

As the sprints are so short, we'll leave the other two [primitive obsession](https://refactoring.guru/smells/primitive-obsession) code smells
for the price and quantity alone for the time being.

</details>

### **User story XIV**: unsupported state taxes
---

> As a user I want to get notified of an unsupported (valid) state tax so that I can correct my input.

<details>
<summary>Unsupported state taxes</summary>

Let's write a test first!

```java
@Test 
void letsUserKnowThatStateCodeIsUnsupported() {
    UnsupportedStateException thrown = assertThrows(
        UnsupportedStateException.class,
        () -> calculator.calculateTax(new InputParameters(2, 345.00, "NY")),
        "Expected calculateTax() to throw, but it didn't"
        );

        assertTrue(thrown.getMessage().contains("Unsupported state: 'NY'"));
}
```

We can make this test pass by modifying the `calculateTax()` method:

```java
double calculateTax(final InputParameters input) {
    if (!stateTaxMap.containsKey(input.state))
        throw new UnsupportedStateException("Unknown state code: '" + input.state + "'");
        
    final double discountedValue = calculateOrderValue(input.quantity, input.price) - calculateDiscountValue(input.quantity, input.price);
    return discountedValue * stateTaxMap.get(input.state) * 0.01;
}
```

</details>

### **User story XV**: non-positive item quantities
---

> As a user I want to get notified of non-positive quantities so that I can correct my input.

<details>
<summary>Non-positive quantities</summary>

Let's write a test first!

```java
@Test 
void letsUserKnowThatNonPositiveQuantityIsUnsupported() {
    IllegalArgumentException thrown = assertThrows(
        IllegalArgumentException.class,
        () -> calculator.calculateTax(new InputParameters(0, 345.00, "UT")),
        "Expected calculateTax() to throw, but it didn't"
        );

        assertTrue(thrown.getMessage().contains("Quantity should be positive"));
}
```
We can make this test pass by adding a guard statement to the constructor of the input parameters:

```java
    public InputParameters(final int quantity, final double price, final String state) {
        if (quantity < 1) throw new IllegalArgumentException("Quantity should be positive");

        // ...
```
</details>

### **User story XVI**: non-positive item prices
---

> As a user I want to get notified of non-positive prices so that I can correct my input.

<details>
<summary>Non-positive prices</summary>

Let's write a test first!

```java
@Test 
void letsUserKnowThatNonPositivePriceIsUnsupported() {
    IllegalArgumentException thrown = assertThrows(
        IllegalArgumentException.class,
        () -> calculator.calculateTax(new InputParameters(1, -345.00, "UT")),
        "Expected calculateTax() to throw, but it didn't"
        );

        assertTrue(thrown.getMessage().contains("Price should be positive"));
}
```
We can make this test pass by adding a guard statement to the constructor of the input parameters:

```java
    public InputParameters(final int quantity, final double price, final String state) {
        if (price < 0) throw new IllegalArgumentException("Price should be positive");
        if (quantity < 1) throw new IllegalArgumentException("Quantity should be positive");

        // ...
```
</details>
