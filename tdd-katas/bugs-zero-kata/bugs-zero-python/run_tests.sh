PYTHONPATH=$PYTHONPATH:src:test
poetry run coverage run game_test.py && poetry run coverage report && poetry run coverage html