'use strict';

import { expect, assert } from "chai"
import { {{ cookiecutter.kata }} } from "../src/{{ cookiecutter.kata }}"

describe("A new {{ cookiecutter.kata }}", function() {
    it("is successfully created", function () {
        var my{{ cookiecutter.kata }}  = new {{ cookiecutter.kata }}()
        assert.equal(true, true)
        expect(false).to.be.false 
        expect(30).to.equal(30)
        expect([]).to.be.empty;
    })
})


