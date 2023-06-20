PYTHONPATH=$PYTHONPATH:src:test
ptw --runner "poetry run coverage run -m pytest"
