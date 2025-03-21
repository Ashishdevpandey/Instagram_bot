from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

# List of actresses' Instagram handles
actresses = [
    "shraddhakapoor",
    "amarpalidubey",
    "kanganaranaut",  # Corrected typo
    "kajol",
    "Akshay_Kumar",
    "Shahrukh_khan"
]

# List of random comments to choose from
comments = [
    "Wow, this is amazing! 😍",
    "Great work! Keep it up! 👏",
    "Love this vibe! ✨",
    "So cool! 🖤",
    "Incredible shot! 📸"
]

# Initialize the Chrome WebDriver with options to reduce bot detection
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")  # Hide automation flags
driver = webdriver.Chrome(options=options)  # Ensure chromedriver is in PATH

def login_instagram(username, password):
    print("Logging in...")
    driver.get("https://www.instagram.com/")
    sleep(8)  # Increased wait time for page load to handle network delays

    # Enter username
    try:
        username_field = driver.find_element(By.NAME, "username")
        username_field.send_keys(username)
        sleep(1)
    except Exception as e:
        print(f"Error entering username: {e}")
        return False

    # Enter password
    try:
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(password)
        sleep(1)
    except Exception as e:
        print(f"Error entering password: {e}")
        return False

    # Click login button
    try:
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        sleep(5)
    except Exception as e:
        print(f"Error clicking login button: {e}")
        return False

    # Pause for 1 minute to allow you to enter the 2FA OTP
    print("Pausing for 1 minute to allow you to enter the 2FA OTP...")
    sleep(60)  # 60 seconds pause for OTP entry

    # Skip "Save Login Info" prompt
    try:
        not_now_button = driver.find_element(By.XPATH, "//button[text()='Not Now']")
        not_now_button.click()
        sleep(2)
    except:
        print("No 'Save Login Info' prompt found.")

    # Skip notifications prompt
    try:
        not_now_button = driver.find_element(By.XPATH, "//button[text()='Not Now']")
        not_now_button.click()
        sleep(2)
    except:
        print("No notifications prompt found.")

    return True

def comment_on_profile_posts(username, num_posts):
    print(f"Visiting profile of @{username}...")
    driver.get(f"https://www.instagram.com/{username}/")
    sleep(5)  # Wait for profile page to load

    # Find and click on the first post
    try:
        first_post = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//article//a[contains(@href, '/p/')]"))
        )
        first_post.click()
        sleep(3)
    except Exception as e:
        print(f"Could not find posts for @{username}: {e}")
        return

    # Comment on the specified number of posts
    for i in range(num_posts):
        try:
            # Randomly select a comment
            comment_text = random.choice(comments)
            print(f"Commenting on post {i+1}/{num_posts}: {comment_text}")

            # Find the comment box and ensure it's interactable
            comment_box = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Add a comment…']"))
            )
            comment_box.click()
            sleep(1)

            # Re-find the comment box after clicking
            comment_box = driver.find_element(By.XPATH, "//textarea[@placeholder='Add a comment…']")
            comment_box.send_keys(comment_text)
            sleep(1)

            # Try submitting the comment with Enter key
            comment_box.send_keys(Keys.ENTER)
            sleep(1)

            # If Enter doesn't work, try clicking the "Post" button
            try:
                post_button = driver.find_element(By.XPATH, "//button[text()='Post']")
                post_button.click()
                sleep(1)
            except:
                print("No 'Post' button found; assuming Enter key worked.")

            print(f"Commented on post {i+1}/{num_posts} for @{username}")

            # Random delay between 3 to 10 seconds
            delay = random.uniform(3, 10)
            print(f"Waiting for {delay:.2f} seconds...")
            sleep(delay)

            # Move to the next post
            try:
                next_button = driver.find_element(By.XPATH, "//button[contains(@class, '_abl-')]")
                next_button.click()
                sleep(3)
            except:
                print("No more posts to comment on.")
                break

        except Exception as e:
            print(f"Error on post {i+1} for @{username}: {e}")
            break

def main():
    # Replace with your Instagram credentials
    username = "Username"
    password = "Userpswd"

    # Log in to Instagram with a pause for OTP
    if not login_instagram(username, password):
        print("Login failed. Exiting...")
        driver.quit()
        return

    # Comment on 2 posts for each actress
    num_posts_per_actress = 2
    for actress in actresses:
        comment_on_profile_posts(actress, num_posts_per_actress)

    # Close the browser
    print("Finished commenting. Closing browser...")
    driver.quit()

if __name__ == "__main__":
    main()
