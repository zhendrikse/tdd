export PYTHONPATH=$PYTHONPATH:src:test
{% if cookiecutter.rspec_syntax == "y" %}poetry run mamba --format=documentation test/*_test.py {% if cookiecutter.code_coverage == "y" %}--enable-coverage{% endif %}{% endif %} 
{% if cookiecutter.rspec_syntax == "n" %}ptw {% if cookiecutter.code_coverage == "y" %}--runner="poetry run coverage run -m pytest"{% endif %}{% endif %}
#
# TODO does not work yet with mamba
#
#ptw --runner "poetry run {% if cookiecutter.rspec_syntax == "y" %}mamba --format=documentation test/*_test.py {% if cookiecutter.code_coverage == "y" %}--enable-coverage{% endif %}{% endif %} {% if cookiecutter.rspec_syntax == "n" %}{% if cookiecutter.code_coverage == "n" %}pytest {% endif %}{% if cookiecutter.code_coverage == "y" %}coverage run -m pytest{% endif %}{% endif %}"