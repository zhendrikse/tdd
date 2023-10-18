PYTHONPATH=$PYTHONPATH:src:test poetry run ptw --runner="poetry run mamba --format=documentation --enable-coverage test/tree_spec.py"
