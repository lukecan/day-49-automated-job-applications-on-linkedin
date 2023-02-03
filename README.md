# LinkedIn Job Saver

This script is a simple LinkedIn job saver that automates the process of logging in to LinkedIn, navigating to the LinkedIn Jobs page, and saving all job listings.

## Prerequisites

Before running the script, you need to have:

- Chrome web browser installed on your computer
- ChromeDriver installed and added to your PATH
- A LinkedIn account
- The LinkedIn account's username and password saved in the environment variables as user_name and password, respectively.

## How to run the script

- Clone the repository
- Run `pip install -r requirements.txt` to install the required libraries
- Run the script using python `main.py`

## Libraries used

- selenium
- dotenv
- time

## What the script does

- Loads environment variables using the dotenv library
- Initializes a ChromeDriver service
- Starts a ChromeDriver session
- Navigates to the LinkedIn Jobs page
- Logs into LinkedIn using the username and password from the environment variables
- Loops through all job listings and clicks on each one to save it.