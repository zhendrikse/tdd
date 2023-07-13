This is a fork of the original Tell Don't Ask Kata of [@rachelcarmena](https://github.com/rachelcarmena/tell-dont-ask-kata). I've only added Python3 and Typescript versions. Probably I will pull request after a time.

# Tell Don't Ask Kata
A legacy refactor kata, focused on the violation of the [tell don't ask](https://pragprog.com/articles/tell-dont-ask) principle and the [anemic domain model](https://martinfowler.com/bliki/AnemicDomainModel.html).

## Instructions
Here you find a simple order flow application. It's able to create orders, do some calculations (totals and taxes), and manage them (approval/reject and shipment).

The old development team did not find the time to build a proper domain model but instead preferred to use a procedural style, building this anemic domain model.
Fortunately, they did at least take the time to write unit tests for the code.

Your new CTO, after many bugs caused by this application, asked you to refactor this code to make it more maintainable and reliable.

## What to focus on
As the title of the kata says, of course, the tell don't ask principle.
You should be able to remove all the setters moving the behavior into the domain objects.

But don't stop there.

If you can remove some test cases because they don't make sense anymore (eg: you cannot compile the code to do the wrong thing) feel free to do it!

## Starting
1. Clone the repository
> `$> git clone https://github.com/mapu77/tell-dont-ask-kata.git`
2. Open the language project in your favourite IDE
3. Open a terminal

     3.1. Java:

     ` $> mvn test`

     3.2. Python3:

     ` $> pip install -r requirements.txt`

     ` $> python -m unittest`

     3.3. Typescript:

     ` $> npm install`

     ` $> npm test`

## Known problems

### Typescript
- Due to the [Javascript BigDecimal library](https://github.com/royNiladri/js-big-decimal) precision and rounding methods, I had to change the test spec.
