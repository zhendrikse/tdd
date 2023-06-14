import { {{  cookiecutter.kata }} } from '../src/{{ cookiecutter.kata }}.js';

describe("A new {{ cookiecutter.kata }}", function() {
    it("is successfully created", function () {
        var {{ cookiecutter.kata|lower }}  = new {{  cookiecutter.kata }}()
        expect(false).toEqual(true);
    })
})

