find . -name node_modules | xargs rm -rf
find . -name target | xargs rm -rf
find . -name __pycache__ | xargs rm -rf
find . -name .pytest_cache | xargs rm -rf
find . -name poetry.lock | xargs rm -rf
find . -name package-lock.json | xargs rm -rf
