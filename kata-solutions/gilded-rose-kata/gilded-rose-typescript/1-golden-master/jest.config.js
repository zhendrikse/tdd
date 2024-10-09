module.exports = {
    preset: 'ts-jest',
    testEnvironment: 'node',

    // Automatically clear mock calls, instances and results before every test
    clearMocks: true,

    // Indicates whether the coverage information should be collected while executing the test
    collectCoverage: true,
  
    // An array of glob patterns indicating a set of files for which coverage information should be collected
    // collectCoverageFrom: undefined,
  
    // The directory where Jest should output its coverage files
    coverageDirectory: "coverage",
  
    // An array of regexp pattern strings used to skip coverage collection
    // coveragePathIgnorePatterns: [
    //   "/node_modules/"
    // ],
  
    // Indicates which provider should be used to instrument code for coverage
    coverageProvider: "v8",
  
    // A list of reporter names that Jest uses when writing coverage reports
    coverageReporters: [
    //   "json",
       "text",
       "lcov",
    //   "clover"
    ],
  
    // An object that configures minimum threshold enforcement for coverage results
    // coverageThreshold: undefined,
  
    // A path to a custom dependency extractor
    // dependencyExtractor: undefined,
  
    // Make calling deprecated APIs throw helpful error messages
    // errorOnDeprecated: false,
  
    // Force coverage collection from ignored files using an array of glob patterns
    // forceCoverageMatch: [],
  
    // A path to a module which exports an async function that is triggered once before all test suites
    // globalSetup: undefined,
  
    // A path to a module which exports an async function that is triggered once after all test suites
    // globalTeardown: undefined,
};
