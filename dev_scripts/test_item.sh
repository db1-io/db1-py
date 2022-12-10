#!/bin/bash
python -m coverage run -m pytest -vv -s ./tests/test_item.py
coverage report -m 
