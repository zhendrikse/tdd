PYTHONPATH=$PYTHONPATH:src:test
poetry run pytest && poetry run coverage run --branch --source gilded_rose gilded_rose_test.py && poetry run coverage report -m && poetry run coverage html