# bdd-python
BDD Basico con Python

pip install pytest
pip install pytest-bdd



# [project root directory]
# |‐‐ [product code packages]
# |-- pages
# |-- [test directories]
# |   |-- features
# |   |   `-- *.feature
# |   `-- step_defs
# |       |-- __init__.py
# |       |-- conftest.py
       


# filter tests by tags
# running by tag is typically better than running by path
python -m pytest -k "web"
