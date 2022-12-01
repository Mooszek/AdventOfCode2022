import requests
from dotenv import load_dotenv
import os
from datetime import datetime
load_dotenv()

YEAR = 2022
SESSION_COOKIE = os.getenv("SESSION_COOKIE")

get_today = datetime.today().day


url = f"https://adventofcode.com/{YEAR}/day/{get_today}/input"

response = requests.get(url=url, cookies={"session":SESSION_COOKIE})
response.raise_for_status()
new_input = response.text

curwd = os.getcwd()
today_dir = f"{curwd}\Day{get_today}"

if not os.path.isdir(today_dir):
    os.mkdir(f"Day{get_today}")

os.chdir(today_dir)

with open("input", "w") as input_file:
    input_file.write(new_input)