# Introduction

This is the famous [video store refactoring kata](https://martinfowler.com/articles/refactoring-video-store-js/)
by [Martin Fowler](https://martinfowler.com/). This kata was
subsequently [translated to Java](https://github.com/unclebob/videostore) 
(as well as slightly modified) by [Uncle Bob](https://github.com/unclebob). 
Finally, I personally decided
to translate the version of Uncle Bob to Python.

In the [original version](https://martinfowler.com/articles/refactoring-video-store-js/), it is stated that code smells by themselves are not enough of a reason to 
refactor code. So an additional feature is imposed, namely to also be able 
to create an HTML version of the current text-based only rental statement 

```
Rental Record for martin
  Ran 3.5
  Trois Couleurs: Bleu 2
Amount owed is 5.5
You earned 2 frequent renter points
```

to 

```html
<h1>Rental Record for <em>martin</em></h1>
<table>
  <tr><td>Ran</td><td>3.5</td></tr>
  <tr><td>Trois Couleurs: Bleu</td><td>2</td></tr>
</table>
<p>Amount owed is <em>5.5</em></p>
<p>You earned <em>2</em> frequent renter points</p>
```

# Instruction video by Emily Bache

There is an instruction (spoiler 😏) video available by Emily Bache that is called [What Would Martin Fowler Do? Javascript Code Refactoring Demo](https://www.youtube.com/watch?v=cZJ36B3iXok).
