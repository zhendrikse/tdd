# Cache kata

This  is a short kata in which you are going to build a very basic cache.

The cache is initially empty, and retrieves its content (from an 
unspecified location) when content is requested for the first time.
Subsequent requests are directly returned from the cache, until a
certain expiration time.

After the expiration time, a request for the cache content leads to an
update of the cache content, and the updated content is returned.

The challenge of this kata is to develop the cache in a
[TDD as if you meant it](https://cumulative-hypotheses.org/2011/08/30/tdd-as-if-you-meant-it/)-style, 
which also means you have to
think of a mechanism to cope with the experation mechanism (and
the system time).