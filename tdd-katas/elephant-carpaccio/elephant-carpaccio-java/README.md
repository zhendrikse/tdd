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
        OrderPriceCalculator classUnderTest = new OrderPriceCalculator();
        assertEquals(classUnderTest.getStartUpMessage(), "Welcome to the order price calculator!");
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

Also, we need to verify the output when we run the executable JAR file:

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
    assertEquals(calculator.calculateOrderValue(2, 345.00), 690.00);
}
```

We can make this test pass by adding the `calculateOrderValue()` method to the production code:

```java
Double calculateOrderValue(final int quantity, final double price) {
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
    System.out.println(calculator.calculateOrderValue(input.quantity, input.price));
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
Double calculateTax(final InputParameters input) {
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
    System.out.println(calculator.calculateTax(input));
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
public double calculateTax(final InputParameters input) {
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

    public Double calculateTax(final InputParameters input) {
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

## Intermezzo: How about invalid input?

Note that we did not provide any logic for invalid state codes.
The most likely thing to do is to throw an `UnsupportedStateException`.

However, it may be even better to ask your product owner what the calculator
is supposed to do in these cases!

Likewise, we probably also want to validate the other two input fields.
For example, we should not be able to enter zero or even a negative amount
of items. And should there also be a maximum?

The same holds for the prices of products, these can never be
negative!

### **User story VII**: invalid state codes
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
        if (quantity < 1) throw new IllegalArgumentException("Quantity should be positive");
        if (price < 0) throw new IllegalArgumentException("Price should be positive");

        this.quantity = quantity;
        this.price = price;
        this.state = State.valueOf(state);
    }

    // ...
```

As the sprints are so short, we'll leave the other two [primitive obsession](https://refactoring.guru/smells/primitive-obsession) code smells
for the price and quantity alone for the time being.

</details>

### **User story VIII**: unsupported state taxes
---

> As a user I want to get notified of an unsupported (valid) state so that I can correct my input.

<details>
<summary>Unsupported state codes</summary>

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
public double calculateTax(final InputParameters input) {
    if (!stateTaxMap.containsKey(input.state))
        throw new UnsupportedStateException("Unknown state code: '" + input.state + "'");
    return input.quantity * input.price * stateTaxMap.get(input.state) * 0.01;
}
```

</details>

### **User story IX**: non-positive item quantities
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

### **User story X**: non-positive item prices
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

### **User story XI**: rounding off
---

> As a user I want to get prices rounded off so that I can directly use them.

<details>
<summary>Rounding off prices</summary>

Let's write a test first!

```java
@Test
void calculatesRoundedTotalPrice() {
    assertEquals(733.13, calculator.calculateRoundedTotalPrice(new InputParameters(2, 345.00, "TX")));
}
```

We make this test pass by adding a `` method

```java
public double calculateRoundedTotalPrice(final InputParameters input) {
    return Math.round(100 * (calculateOrderValue(input.quantity, input.price) + calculateTax(input))) / 100.0;
}
```

By invoking this method in the `main()`, we get the desired endresult:

```java
public static void main(String[] args) {
    // ...

    final InputParameters input = calculator.readInputParameters();
    System.out.println(input);
    System.out.println("Grand total: " + calculator.calculateRoundedTotalPrice(input));
}
```

</details>

## Discounts


### **User story XII**: discounts for Utah
---

> As a user I want to know the discount value when I ordered in Utah so that I can get my discount.

<details>
<summary>Discounts in Utah</summary>

Let's write a test first!

```java
@Test
void calculatesDiscountForUtah() {
    assertEquals(20.70, calculator.calculateDiscountValue(2, 345.00));
}
```

and the production code to make the test pass

```java
Double calculateDiscountValue(final int quantity, final double price) {
    return 0.03 * quantity * price;
}
```
</details>


### **User story XIII**: calculate taxes based on discounts in Utah
---

> As a user I want to know the tax based on the discount value when I ordered in Utah so that I can calculate my total price.

<details>
<summary>Taxes on discounted products in Utah</summary>

Let's write a test first!

```java
@Test
void calculatesTaxesBasedOnDiscountForUtah() {
    calculator.configure(State.UT, 6.85, 3);

    assertEquals(45.84705, calculator.calculateTax(new InputParameters(2, 345.00, "UT")), 0.001);
}
```

and the production code to make the test pass

```java
double calculateTax(final InputParameters input) {
    if (!stateTaxMap.containsKey(input.state))
        throw new UnsupportedStateException("Unsupported state: '" + input.state + "'");
    
    double orderValue = calculateOrderValue(input.quantity, input.price); 
    if (discount != 0) 
        orderValue -= calculateDiscountValue(input.quantity, input.price);

    return orderValue * stateTaxMap.get(input.state) * 0.01;
}
```
</details>

### **User story XIV**: calculate taxes based on discounts in Texas
---

> As a user I want to know the tax based on the discount value when I ordered in Texas so that I can calculate my total price.

<details>
<summary>Taxes on discounted products in Texas</summary>

Let's write a test first!

```java
@Test
void calculatesTaxesBasedOnDiscountForTexas() {
    calculator.configure(State.TX, 6.85, 7);
    assertEquals(43.95645, calculator.calculateTax(new InputParameters(2, 345.00, "TX")), 0.001);
}
```

and the production code to make the test pass

```java
double calculateTax(final InputParameters input) {
    if (!stateTaxMap.containsKey(input.state))
        throw new UnsupportedStateException("Unsupported state: '" + input.state + "'");
    
    double orderValue = calculateOrderValue(input.quantity, input.price); 
    if (discountsMap.containsKey(input.state)) 
        orderValue -= calculateDiscountValue(input);

    return orderValue * stateTaxMap.get(input.state) * 0.01;
```

where we have introduced a discounts hashmap as well:

```java
public class OrderPriceCalculator {
    private Map<State, Double> stateTaxMap = new HashMap<>();
    private Map<State, Integer> discountsMap = new HashMap<>();

    // ...
```
</details>

### **User story XV**: calculate total price based on taxes and discounts
---

> As a user I want to know the total price based on tax and discount so that I can quote an order.

<details>
<summary>Total price based on taxes and discounts</summary>

Let's write a test first!

```java
@Test
void calculatesTotalPriceBasedOnTaxesAndDiscountForTexas() {
    calculator.configure(State.TX, 6.85, 7);
    assertEquals(733.96, calculator.calculateRoundedTotalPrice(new InputParameters(2, 345.00, "TX")));
}
```

Because of  the way we implemented the order price calculator, this
test immediately jumps to green, so we may as well discard it.

Let's take the opportunity to update the `main()`, so that the discounts
are also taken into account when running the stand-alone executable:

```java
    public static void main(String[] args) {
        final OrderPriceCalculator calculator = new OrderPriceCalculator();
        calculator.configure(State.UT, 6.85, 3);
        calculator.configure(State.NV, 8.00, 5);
        calculator.configure(State.TX, 6.25, 7);
        calculator.configure(State.AL, 4.00, 10);
        calculator.configure(State.CA, 8.25, 15);

        // ...
```
</details>