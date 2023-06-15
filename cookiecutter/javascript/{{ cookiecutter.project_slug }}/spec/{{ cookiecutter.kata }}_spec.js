'use strict';

const { {{ cookiecutter.kata }} } = require('../src/{{ cookiecutter.kata }}.js')
var expect = require('expect.js');

describe("A new {{  cookiecutter.kata }}", function() {
    it("is successfully created", function () {
        var {{ cookiecutter.kata|lower }}  = new {{  cookiecutter.kata }}()
        expect(true).not.to.be(true);
    })
})

