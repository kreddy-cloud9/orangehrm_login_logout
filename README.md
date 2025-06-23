# OrangeHRMLive Login/Logout Automation
This is a basic Selenium automation script that tests the login and logout flow of the OrangeHRMlive demo application.

## Application Under Test
https://opensource-demo.orangehrmlive.com

## Functional tests
- Valid login test
- Logout flow test
- Negative test for invalid credentials

## Tools Used
- Python 3.9+
- Selenium 4.x
- Pytest

## Setup Instructions
1. Clone this repo or copy files to a local directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Assumptions
1. ChromeDriver is managed via Selenium 4.
2. Internet access is available to access the live demo site.
3. Basic error handling is implemented for assertion and visibility checks.
