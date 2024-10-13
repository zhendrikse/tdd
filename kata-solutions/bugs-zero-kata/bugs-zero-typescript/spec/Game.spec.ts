'use strict';

import { GameRunner } from "../src/GameRunner"
import { verify, verifyAsJson } from "approvals/lib/Providers/Jest/JestApprovals";

const jestConsole = console;


describe("A new Trivia", function () {
  beforeEach(() => {
    global.console = require('console');
  });

  afterEach(() => {
    global.console = jestConsole;
  });

  it("is successfully created", function () {
    var gameRunner = new GameRunner()

    const capcon = require('capture-console');

    let stdout = "";
    stdout = capcon.captureStdout(() => {
      gameRunner.playGame(gameRunner.doRoll());
    });

    verify(stdout);
  })
})

