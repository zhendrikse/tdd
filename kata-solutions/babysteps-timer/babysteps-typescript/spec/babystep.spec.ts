'use strict';

import { describe, it } from "mocha"
import { expect, assert } from "chai"
import { CreateTimerHtml, command } from "../src/babystep"

describe("A new babysteps timer", function() {  
    beforeEach(() => {
        command("start")
    })

    afterEach(() => {
        command("stop")
    })

    it("h1 contains the time", function() {
        expect(document.querySelector("h1")?.innerHTML).to.equal("02:00")
    })

    it("time ticks back over time", async() => {
        await new Promise(resolve => setTimeout(resolve, 50))
        expect(document.querySelector("h1")?.innerHTML).to.equal("01:59")
    })

    it("time ticks back over longer time", async() => {
        await new Promise(resolve => setTimeout(resolve, 1050))
        expect(document.querySelector("h1")?.innerHTML).to.equal("01:58")
    })
})


