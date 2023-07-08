# WEB-PLAYWRIGHT-EXAMPLE

<h3><ins>How to Setup:</h3>
    
- Clone this repo and go to the project directory
- Install & create Virtual ENV
    - `pip install virtualenv`
    - `python -m venv ./venv`
- Use the Virtual ENV
    - `source ./venv/bin/activate`
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
