# Instagram Comment Bot

This is a Python script that uses Selenium to automate commenting on Instagram posts of specified actors and actresses. The bot logs into your Instagram account, navigates to the profiles of popular Indian celebrities, and posts thoughtful, positive comments on their recent posts.

## Features
- Logs into Instagram with support for 2FA (manual OTP entry).
- Comments on a configurable number of posts per profile.
- Uses a mix of male and female Indian actors/actresses.
- Includes randomized delays and thoughtful comments to mimic human behavior.
- Credentials are securely stored in environment variables.
- Robust error handling and graceful browser shutdown.

## Prerequisites
- **Python 3.x**: Ensure Python is installed on your system.
- **Chrome Browser**: The script uses Chrome WebDriver.
- **Chromedriver**: Must match your Chrome version and be added to your system PATH.

## Installation
1. **Clone the Repository** (or download the script):
   ```bash
   git clone <repository-url>
   cd instagram-comment-bot
