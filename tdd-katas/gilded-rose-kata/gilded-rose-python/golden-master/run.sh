echo "Running pytest with coverage..."
pytest && coverage run --branch --source gilded_rose gilded_rose_test.py && coverage report -m && coverage html