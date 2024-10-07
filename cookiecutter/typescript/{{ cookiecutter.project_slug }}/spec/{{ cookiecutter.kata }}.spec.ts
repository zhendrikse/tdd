'use strict';
{% if cookiecutter.jest_tests == "n" %}
import { expect, assert } from "chai"
{% endif %}
import { {{ cookiecutter.kata }} } from "../src/{{ cookiecutter.kata }}"

describe("A new {{ cookiecutter.kata }}", function() {
    it("is successfully created", function () {
        var my{{ cookiecutter.kata }}  = new {{ cookiecutter.kata }}()
{% if cookiecutter.jest_tests == "n" %}
        assert.equal(true, true)
        expect(false).to.be.false 
        expect(30).to.equal(30)
        expect([]).to.be.empty;
{% endif %}
{% if cookiecutter.jest_tests == "y" %}
	expect(true).toEqual(true)
        expect(false).toBe(false)
        expect(30).toEqual(30)
        expect([]).toHaveLength(0)
{% endif %}
    })
})


