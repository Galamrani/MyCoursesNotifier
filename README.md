# MyCoursesNotifier

This script helps you stay updated on the availability of new courses for enrollment at the Open University of Israel. It uses web scraping to monitor the course registration page for a specific course and notifies you when new study groups are available.

## Requirements

- Python 3.x
- Selenium: `pip install selenium`
- winotify: `pip install winotify`
- Chrome WebDriver: Download and install ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure to place the `chromedriver.exe` file in the path specified in the `DRIVER_PATH` constant.

## How to Use

1. Make sure you have all the requirements installed.

2. Update the script with your course details:

   ```python
   COURSE_ID = "20554"     // Replace with your desired course ID
   YEAR = "2024"           // Replace with the desired year (e.g., 2024)
   SEMESTER = "A"          // Replace with the desired semester (A, B, or C)
   DRIVER_PATH = "C:\Program Files\chromedriver.exe"   // Replace with the path to your Chrome WebDriver
   ```

3. Run the script manually to ensure it's working as expected:

   ```
   python my_courses_notifier.py
   ```

## Automation with Windows Task Scheduler

You can set up automation using Windows Task Scheduler to run the script at regular intervals. Here's how to do it:

1. Open "Task Scheduler" on your Windows machine.

2. Click on "Create Basic Task" on the right-hand side.

3. Give your task a name and description, then click "Next."

4. Choose "Daily" if you want the script to run daily or choose "Weekly" for a specific day of the week. Click "Next."

5. Set the start date and time for your task, and click "Next."

6. Choose "Start a Program" and click "Next."

7. Browse and select the Python executable (e.g., C:\Python39\python.exe) in the "Program/script" field.

8. In the "Add arguments" field, enter the full path to the my_courses_notifier.py file (e.g., "C:\path\to\your\script\my_courses_notifier.py").

9. In the "Start in" field, enter the directory path where the my_courses_notifier.py file is located (e.g., "C:\path\to\your\script").

10. Click "Next" to review your settings.

11. Click "Finish" to create the task.

Now, the script will run automatically at the specified intervals, checking for new course offerings and notifying you when available.

## Functionality

1. **Scrape Course IDs**: The script will open the Open University's course registration page for the specified semester and course. It will retrieve the course IDs and study group IDs available for enrollment.

2. **Check and Notify New Courses**: The script will compare the newly scraped course IDs with the ones stored in the `course_identifiers.csv` file. If it finds any new course IDs, it will notify you about them using the Windows Notification Center. The script will also save the latest course IDs to the CSV file for future comparisons.

## Notifications

- When new courses are available, you will receive a Windows notification with the list of new course IDs.
- The notification will display the course ID, the study group ID, and additional information about the available courses.

## Note

- Make sure to run the script manually at least once to ensure it works as expected before scheduling it with Windows Task Scheduler.
