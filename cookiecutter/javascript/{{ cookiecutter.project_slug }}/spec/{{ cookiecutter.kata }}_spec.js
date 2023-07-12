'use strict';
{% if cookiecutter.tests_in_browser == "n" %} 
const { {{ cookiecutter.kata }} } = require('../src/{{ cookiecutter.kata }}.js')
var expect = require('expect.js');
{% endif %}

describe("A new {{  cookiecutter.kata }}", function() {
    it("is successfully created", function () {
        var {{ cookiecutter.kata|lower }}  = new {{  cookiecutter.kata }}()
{% if cookiecutter.tests_in_browser == "y" %} 
        expect(true).toBeTruthy();
{% elif cookiecutter.tests_in_browser == "n" %} 
        expect(true).not.to.be(true);
{% endif %}
    })
})

