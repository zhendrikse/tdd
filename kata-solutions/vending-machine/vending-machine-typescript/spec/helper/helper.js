//-------------------------------------------------
// spec/helpers/helper.js
//-------------------------------------------------
const TSConsoleReporter = require("jasmine-ts-console-reporter");
jasmine.getEnv().clearReporter(); //Clear default console reporter
jasmine.getEnv().addReporter(new TSConsoleReporter());