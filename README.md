# Course Notifier

## Overview
The **Course Notifier** project aims to provide a convenient solution for students or individuals interested in specific study group of a courses in the open university of israel. Course Notifier make sure you stay updated on new course offerings. By leveraging web scraping techniques, the script automates the process of monitoring course listings on a open university website, detecting any additions or changes, and promptly notifying the user by a message.

## Purpose
1. **Automation of Course Monitoring**: Manually checking for new study group of courses or updates on a website can be time-consuming and inefficient. The Course Notifier automates this process, saving users valuable time and effort.
  
2. **Timely Notifications**: By scheduling periodic checks for new courses, the script ensures that users receive timely notifications as soon as new offerings become available, allowing them to take prompt action, such as registering for courses of interest.

3. **Customization and Flexibility**: The script provides flexibility by allowing users to specify the course ID, academic year, and semester of interest. This customization ensures that users receive notifications tailored to their specific preferences.

## Key Components

### Web Scraping (`scraper.py`)
- Utilizes the Selenium library to scrape course IDs and study group elements from the target website.
- Parses the webpage content to extract relevant information, such as course codes and study group details.
- Handles exceptions and errors gracefully to maintain script robustness.

### Notification System (`notifier.py`)
- Implements a notification system using the Pushover API to send notifications to users' devices.
- Constructs informative messages detailing the newly available courses for user convenience.
- Validates Pushover API tokens and user keys to ensure successful notification delivery.

### Scheduled Execution (`schdualer.py`)
- Orchestrates the entire process by scheduling tasks using the `schedule` library.
- Defines a job function to execute the scraping, checking, and notification processes.
- Allows users to customize the scheduling interval and end date based on their preferences and requirements.

### Data Management (`course_identifiers.csv`)
- Stores course IDs in a CSV file for comparison with newly scraped data.
- Enables efficient detection of new courses by maintaining a record of previously identified course IDs.

### User Interaction (`info.file`)
- Providing interactions with the user to receive the necessary information.

## Usage
1. **Installation**: Users need to install Python 3.x and the required dependencies listed in `Requirements`.
   
2. **Configuration**: 
    - Before running this script, make sure to set up the PUSHOVER_TOKEN and PUSHOVER_USER_KEY environment variables.
        ```bash
        export PUSHOVER_TOKEN="your_pushover_token"
        export PUSHOVER_USER_KEY="your_pushover_user_key"
        ```
        Verify if they are set up correctly using the following commands:
        ```bash
        echo $PUSHOVER_TOKEN
        echo $PUSHOVER_USER_KEY
        ```
    - Additionally, ensure that the Chrome WebDriver is installed and accessible.

3. **Execution**: Run the script (`schdualer.py`) to initiate the monitoring process.
   
4. **Customization**: Adjust scheduling parameters and input course-specific details as needed.

5. **Notification**: Receive timely notifications about new courses via the configured notification service.

## Requirements
- Python 3.x
- Selenium
- schedule
- Chrome WebDriver
- Pushover API tokens and user keys


## Author
Gal amrani


