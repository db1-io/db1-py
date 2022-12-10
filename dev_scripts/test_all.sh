#!/bin/bash

# Python 3.7
source $(conda info --base)/etc/profile.d/conda.sh
rm -rf $(conda info --base)/envs/temp_db1_test
printf "\n\n**********************************************\n"
printf "Init Python 3.7 env...\n"
{
    yes | conda create --name temp_db1_test python=3.7
    conda activate temp_db1_test 
    python -m pip install pytest
    python -m pip install ./
} &> /dev/null
printf "Run tests with Python 3.7\n\n"
python -m pytest -vv -s ./tests/test_serializer.py
python -m pytest -vv -s ./tests/test_item.py
{
    conda deactivate
    conda env remove --name temp_db1_test
} &> /dev/null


# Python 3.8
printf "\n\n**********************************************\n"
printf "Init Python 3.8 env...\n"
{
    yes | conda create --name temp_db1_test python=3.8
    conda activate temp_db1_test 
    python -m pip install pytest
    python -m pip install ./
} &> /dev/null
printf "Run tests with Python 3.8\n\n"
python -m pytest -vv -s ./tests/test_serializer.py
python -m pytest -vv -s ./tests/test_item.py
{
    conda deactivate
    conda env remove --name temp_db1_test
} &> /dev/null


# Python 3.9
printf "\n\n**********************************************\n"
printf "Init Python 3.9 env...\n"
{
    yes | conda create --name temp_db1_test python=3.9
    conda activate temp_db1_test 
    python -m pip install pytest
    python -m pip install ./
} &> /dev/null
printf "Run tests with Python 3.9\n\n"
python -m pytest -vv -s ./tests/test_serializer.py
python -m coverage run -m pytest -vv -s ./tests/test_item.py
coverage report -m
printf "\n\nRun code checks with Python 3.9\n\n"
{
    python -m pip install -r requirements_dev.txt
    python -m mypy ./
    yes | python -m mypy --install-types
} &> /dev/null
printf "mypy --------------------------------------------------------------\n"
python -m mypy ./
printf "\nblack -------------------------------------------------------------\n"
python -m black ./
printf "\nflake8 ------------------------------------------------------------\n"
python -m flake8 ./
{
    conda deactivate
    conda env remove --name temp_db1_test
} &> /dev/null
