# Introduction

This is a kata on ports and adapters architecture. 
The task is to retrieve a list of 
[name, capital, population, cioc, and region information](https://restcountries.com/v3.1/all?fields=name,capital,population,cioc,region) from the [REST countries API](https://restcountries.com/) and output the result into a CSV file of the following format:

name, capital, population, cioc, region

where the cioc field represents the [three-letter country code](https://en.wikipedia.org/wiki/List_of_IOC_country_codes).

Optionally you may want to add a header field to the generated CSV file.

The goal is not to get this done as quickly as possible, but to follow the rules of ports and adapters architecture:

- The application itself does not depend directly on any external systems, but only on ports
- The protocol for a port is given by the purpose of the conversation it describes
- For each external system there is an adapter that converts the API definition to the format 
  needed by that system and vice versa

