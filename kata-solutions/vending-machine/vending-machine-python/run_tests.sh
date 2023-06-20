export PYTHONPATH=src:test
poetry run mamba --format=documentation test/*_test.py  

#
# TODO does not work yet with mamba
#
#ptw --runner "poetry run mamba --format=documentation test/*_test.py  "
