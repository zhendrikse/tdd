#python -m http.server 8000 -d htmlcov >/dev/null 2>/dev/null &
PYTHONPATH=$PYTHONPATH:src:test poetry run mamba --format=documentation spec/*_spec.py --enable-coverage && poetry run coverage html
