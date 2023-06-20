export PYTHONPATH=$PYTHONPATH:src:test
poetry run mamba --format=documentation test/*_test.py --enable-coverage && poetry run coverage html
 
