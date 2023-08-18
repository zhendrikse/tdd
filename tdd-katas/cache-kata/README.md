# Cache kata

This  is a short kata in which you are going to build a very basic cache.

The cache is initially empty and retrieves its content (from an 
unspecified location) the first time content is requested.
Subsequent requests will be returned directly from the cache, until a
certain expiration time.

After the expiration time, a request for the cached content results in an
update of the cached content and the updated content is returned.

The challenge of this kata is to write the cache in a
[TDD as if you meant it](https://cumulative-hypotheses.org/2011/08/30/tdd-as-if-you-meant-it/)-style, 
which also means that you have to
come up with a mechanism to deal with the expiry mechanism (and
system time).
