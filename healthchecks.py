import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging
# Function to send an email
def send_email(subject, body, to_email):
    from_email = "hi@demomailtrap.com"
    from_password = "0fa5bfb5fd83f20112de58505c1cc214"
    
    # Create the email message
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Set up the server and send the email
        server = smtplib.SMTP("live.smtp.mailtrap.io", 587)
        server.starttls()  # Enable security
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, message.as_string())
        server.close()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Define Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Print current working directory to help with troubleshooting
print(f"Current working directory: {os.getcwd()}")

try:
    # Open Kibana login page
    login_url = "http://kibana:5601"
    driver.get(login_url)

    # Wait for the login page to load
    time.sleep(5)

    logging.info('started logging in...')

    # Enter login credentials
    username = driver.find_element(By.NAME, "username")  # Adjust if necessary
    password = driver.find_element(By.NAME, "password")  # Adjust if necessary
    username.send_keys("elastic")  # Replace with actual username
    password.send_keys("kibana123")  # Replace with actual password
    password.send_keys(Keys.RETURN)  # Press Enter to submit

    logging.info('lockedin....')


    # Wait for the dashboard page to load
    time.sleep(10)

    # List of multiple Kibana dashboard URLs
    dashboard_urls = [
        "http://kibana:5601/app/dashboards#/view/722b74f0-b882-11e8-a6d9-e546fe2bba5f?_g=(filters:!())",
        "http://kibana:5601/app/dashboards#/view/7adfa750-4c81-11e8-b3d7-01146121b73d?_g=(filters:!())"
    ]

    for i, url in enumerate(dashboard_urls, start=1):
        logging.info('taking screenshots...')
        driver.get(url)
        time.sleep(15) 

        # full-page screenshot
        total_width = driver.execute_script("return document.body.scrollWidth")
        total_height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(total_width, total_height)
        logging.info(f'H: {total_height} and W: {total_width}')



        # Capture full-page screenshot and specify the directory to save it
        screenshot_directory = "/app/screenshots"  # Specify your folder path
        if not os.path.exists(screenshot_directory):
            os.makedirs(screenshot_directory)  # Create the directory if it doesn't exist
        
        screenshot_path = os.path.join(screenshot_directory, f"kibana_dashboard_{i}.png")
        driver.get_screenshot_as_file(screenshot_path)
        logging.info(f"Screenshot saved: {screenshot_path}")

        logging.info(f"Contents of /app/screenshots: {os.listdir(screenshot_directory)}")


        # # Send email after screenshot is saved
        # subject = f"Kibana Dashboard {i} - Screenshot"
        # body = f"The screenshot for Kibana Dashboard {i} has been successfully captured and saved as {screenshot_path}."
        # send_email(subject, body, "anselemo.flavian@outlook.com")

finally:
    logging.info('Done...')
    driver.quit()  # Close the browser session


