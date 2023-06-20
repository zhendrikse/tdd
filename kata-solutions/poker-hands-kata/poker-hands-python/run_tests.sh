export PYTHONPATH=src:spec
poetry run mamba --format=documentation spec/*_spec.py --enable-coverage && poetry run coverage html

