import json, os, urllib.parse, subprocess
import test_data
from dotenv import load_dotenv

load_dotenv(".env")
username = test_data.variables["username"]
password = test_data.variables["password"]
capabilities = [{
    "browserName": os.getenv("BROWSER"),
    "browserVersion": "latest",
    "build": "Testing",
    "name": "Playwright Test",
    "console": True
}]