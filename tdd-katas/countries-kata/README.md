# Introduction

This is a kata on ports and adapters architecture. 
The task is to retrieve a list with
[country information](https://restcountries.com/v3.1/all?fields=name,capital,population,cioc,region) from the [REST countries API](https://restcountries.com/) and output the result into a CSV file 
of the following format:

```
name,capital,region,subregion,population,cca3,cca2,ccn3,unMember
Jordan,Amman,Asia,Western Asia,10203140,JOR,JO,400,True
Northern Mariana Islands,Saipan,Oceania,Micronesia,57557,MNP,MP,580,False
Serbia,Belgrade,Europe,Southeast Europe,6908224,SRB,RS,688,True
```

**Caveat**: 
Note that the API returns the capital city in a list, and sometimes this 
list may even be empty!

There are two options to start this kata:
1. Approach it as a legacy application, that has no tests yet.
   The exercise is to make this application better
   testable by refactoring it to include ports &amp; adapters.
   Both the CSV writer as well as the retrieval of country data
   should be handled using adapters.
2. Approach it as a greenfield application, that has to be written from the
   ground up.

The goal is not to complete this kata as quickly as possible, 
but to follow the rules of ports &amp; adapters architecture:

- The application itself does not depend directly on
  any external systems, but only on ports
- The protocol for a port is given by the purpose of the conversation it describes
- For each external system there is an adapter that converts
  the API definition to the format 
  needed by that system and vice versa

## Possible extensions

- Add a possibility to update a reference table in a database with these
  country data. Optionally according to a certain time schedule, e.g. weekly.
- Add a possibility to filter, e.g. only export those countries to CSV that
  are a UN member, or only export those countries that have more than 10 million
  inhabitants.
