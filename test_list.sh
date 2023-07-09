#!/bin/bash
# the test suite variable name must contain '_tests'
# example: 'login_tests'
# when you run the test with './run_test.sh', you only need to call the first suite name only
# example: './run_test.sh login'

login_tests=(
    "./tests/test_login.py"
    # ... add more test file here
)
dashboard_tests=(
    "./tests/test_dashboard.py"
    # ... add more test file here
)

# ... add new_suite_tests here