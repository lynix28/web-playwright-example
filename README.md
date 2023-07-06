# WEB-PLAYWRIGHT-EXAMPLE

<h3><ins>How to Setup:</h3>
<sub> *if you use Python3, just change the command to `python3` & `pip3`</sub>
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
- `playwright cr "URL_to_website"` <sub>*use: cr = chromium | ff = firefox | wk = webkit</sub>

<h3><ins>Running the tests:</h3>
- `pytest ./[your_test_script].py --headed` <sub>don't use '--headed' to run as HEADLESS</sub>
- `pytest ./[your_test_script].py --browser firefox --headed` <sub>to use different browser add CLI argument 'firefox' or 'webkit', the default is 'chromium'</sub>