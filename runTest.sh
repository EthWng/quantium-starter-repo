#!/bin/bash

# activate virtual environment
source venv/Scripts/activate  # Windows

# run tests
pytest testApp.py

# return exit code — pytest automatically sets $? to 0 (pass) or 1 (fail)
exit $?

#bash runTest.sh