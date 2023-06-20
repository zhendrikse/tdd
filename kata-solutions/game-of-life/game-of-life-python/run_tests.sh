export PYTHONPATH=$PYTHONPATH:src:test
poetry run mamba --format=documentation test/*_spec.py --enable-coverage && poetry run coverage html
