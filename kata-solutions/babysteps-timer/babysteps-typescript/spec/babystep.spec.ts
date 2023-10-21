'use strict';

import { describe, it } from "mocha"
import { expect, assert } from "chai"
import { CreateTimerHtml, command, Clock } from "../src/babystep"

class FakeClock implements Clock {
    private nextTimeValue: number = 0

    currentTime(): number {
        return Date.now()
    }

    async nextCurrentTimeValueIs(nextTimeValue: number): Promise<void> {
        this.nextTimeValue = nextTimeValue * 1000
        await new Promise(resolve => setTimeout(resolve, this.nextTimeValue))
    }
}

describe("A new babysteps timer", function() {
    let fakeClock: FakeClock

    beforeEach(() => {
        fakeClock = new FakeClock()
        command("start", fakeClock)
    })

    afterEach(() => {
        command("stop")
    })

    it("h1 contains the time", function() {
        expect(document.querySelector("h1")?.innerHTML).to.equal("02:00")
    })

    it("time ticks back over time", async() => {
        await fakeClock.nextCurrentTimeValueIs(0.75)
        expect(document.querySelector("h1")?.innerHTML).to.equal("01:59")
    })

    it("time ticks back over longer time", async() => {
        await fakeClock.nextCurrentTimeValueIs(1.75)
        expect(document.querySelector("h1")?.innerHTML).to.equal("01:58")
    })
})

