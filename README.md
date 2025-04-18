# WEB-PLAYWRIGHT-EXAMPLE

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/lynix28/web-playwright-example/tree/master.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/lynix28/web-playwright-example/tree/master)

<h3><ins>How to Setup:</h3>

- Clone this repo and go to the project directory
- Install & create Virtual ENV

   - `pip install virtualenv`
   - `python -m venv ./venv`

- Use the Virtual ENV

   - `source ./venv/bin/activate` -> for Linux / Mac
   - `./venv/Script/Activate.ps1` -> for Windows

- Install PIP Packages

   - `pip install -r requirements.txt`

- Download required browser

   - `playwright install`

<h3><ins>Inspect an element:</h3>

- `playwright cr "URL_to_website"`
   - use: cr = chromium | ff = firefox | wk = webkit

<h3><ins>Running the tests:</h3>

- `pytest ./[your_test_script].py`
   - to run it on HEADLESS, update the `.env` file, the default is 'False'
   - to use different browser like 'firefox' or 'webkit', update the `.env` file, the default is 'chromium'

<h3><ins>Running the tests (with: run_test.sh):</h3>

- `./run_test.sh` | to run all tests
- `./run_test.sh [your_test_script_alias]` | to run a specific scenario
   - Make sure to give "execute" permission to `run_test.sh`
   - Make sure to add your test to `test_list.sh` if there is any new test scenario

- `./run_test.sh --help` | for more example how to run the test

<h3><ins>Running the tests (BDD):</h3>

- `pytest` | to run all tests
- `pytest -k "tag_or_alias"` | to run a specific scenario (ex: login)
