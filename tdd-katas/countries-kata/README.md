# Introduction

This is a kata on ports and adapters architecture. 
The task is to retrieve a list with
[country information](https://restcountries.com/v3.1/all?fields=name,capital,population,cioc,region) from the [REST countries API](https://restcountries.com/) and output the result into a CSV file of the following format:

```
name, capital, region, subregion, population, cca3, cca2, ccn3, unMember
```

for example

```
Jordan, Amman, Asia, Western Asia, 10203140, JOR, JO, 400, true 
```

Optionally you may want to add the header field to the generated CSV file.

```
name, capital, region, subregion, population, cca3, cca2, ccn3, unMember
Jordan, Amman, Asia, Western Asia, 10203140, JOR, JO, 400, true 
```

The goal is not to get this done as quickly as possible, but to follow the rules of ports and adapters architecture:

- The application itself does not depend directly on any external systems, but only on ports
- The protocol for a port is given by the purpose of the conversation it describes
- For each external system there is an adapter that converts the API definition to the format 
  needed by that system and vice versa

