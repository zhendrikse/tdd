export PYTHONPATH=$PYTHONPATH:src:test
 
poetry run ptw 

#
# TODO does not work yet with mamba
#
#ptw --runner "poetry run  pytest "