#python -m http.server 8000 -d htmlcov >/dev/null 2>/dev/null &
poetry run mamba --format=documentation *_spec.py --enable-coverage && poetry run coverage html