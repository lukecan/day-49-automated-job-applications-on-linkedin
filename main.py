from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Load environment variables
load_dotenv()

# Get credentials from environment variables
username = os.getenv("user_name")
password = os.getenv("password")

# LinkedIn jobs URL
url = "https://www.linkedin.com/jobs/search/?currentJobId=3387660807&f_AL=true&f_WT=2&keywords=Python%20Developer" \
      "&refresh=true&sortBy=R "

# Path to the ChromeDriver
chrome_driver_path = "/Users/mece/Desktop/chromedriver"

# Initialize ChromeDriver service
service = Service(chrome_driver_path)

# Start a ChromeDriver session
driver = webdriver.Chrome(service=service)

# Open LinkedIn jobs page
driver.get(url)

# Wait 5 seconds for page to load
time.sleep(5)

# Find and click the sign-in button
sign_in = driver.find_element(By.CSS_SELECTOR, "body > div.base-serp-page > header > nav > div > "
                                               "a.nav__button-secondary.btn-md.btn-secondary-emphasis")
sign_in.click()

# Enter username
login_user = driver.find_element(By.CSS_SELECTOR, "#username")
login_user.send_keys(username)

# Wait 5 seconds
time.sleep(5)

# Enter password
login_pass = driver.find_element(By.CSS_SELECTOR, "#password")
login_pass.send_keys(password)

# Wait 5 seconds
time.sleep(5)

# Find and click the login button
button = driver.find_element(By.CSS_SELECTOR, '#organic-div > form > div.login__form_action_container > button')
button.click()

# Wait 5 seconds for page to load
time.sleep(5)

# Find all job listings
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

# Loop through all job listings
for job in all_listings:
    # Click on the job listing
    job.click()

    # Wait 3 seconds for page to load
    time.sleep(3)

    # Find and click the "Save" button
    save = driver.find_element(By.CSS_SELECTOR, "#main > div > section.scaffold-layout__detail.overflow-x-hidden.jobs"
                                                "-search__job-details > div > div.job-view-layout.jobs-details > "
                                                "div:nth-child(1) > div > div:nth-child(1) > div > div.relative > "
                                                "div.jobs-unified-top-card__content--two-pane > div:nth-child(4) > "
                                                "div > button")

