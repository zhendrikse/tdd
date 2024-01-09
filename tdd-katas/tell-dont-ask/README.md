This is a fork of the original Tell Don't Ask Kata of [@rachelcarmena](https://github.com/rachelcarmena/tell-dont-ask-kata) in Java. 
In this directory, you'll find ports to other languages as well. 

# Tell Don't Ask Kata
A legacy refactor kata, focused on the violation of the [tell don't ask](https://pragprog.com/articles/tell-dont-ask) principle and the [anemic domain model](https://martinfowler.com/bliki/AnemicDomainModel.html).

## Instructions
Here you find a simple order flow application. It's able to create orders, do some calculations (totals and taxes), and manage them (approval/rejection and shipment).

The old development team did not find the time to build a proper domain model but instead preferred to use a procedural style, building this anemic domain model.
Fortunately, they did at least take the time to write unit tests for the code.

Your new CTO, after many bugs caused by this application, asked you to refactor this code to make it more maintainable and reliable.

## What to focus on

As the title of the kata says, of course, the purpose is to get acquainted with the tell-don't-ask principle.
Eventually, you should be able to remove all the setters from the domain objects by moving the behavior into those very domain objects.

But don't stop there.

If you can remove some test cases because they don't make sense anymore, feel free to do so!
