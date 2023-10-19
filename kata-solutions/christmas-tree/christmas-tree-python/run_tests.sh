PYTHONPATH=$PYTHONPATH:src:test poetry run mamba --format=documentation test/tree_spec.py --enable-coverage && poetry run coverage html
