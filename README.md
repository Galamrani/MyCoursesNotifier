# MyCoursesNotifier

This handy script keeps you informed about the latest course offerings at the Open University of Israel. Through web scraping, it monitors the course registration page for a particular course that you chose and alerts you as soon as new study groups become available.


# Steps to use the **MyCoursesNotifier** script:

1. Clone the Repository:
   - Go to the GitHub repository page (e.g., https://github.com/username/MyCoursesNotifier).
   - Click on the "Code" button and copy the repository URL (e.g., https://github.com/username/MyCoursesNotifier.git).
   - Open a terminal or command prompt on your computer.
   - Navigate to the directory where you want to clone the repository.
   - Run the following command to clone the repository:

     ```
     git clone https://github.com/username/MyCoursesNotifier.git
     ```

2. Install Dependencies:
   - Make sure you have Python 3.x installed on your computer.
   - Install the required dependencies using pip:

     ```
     pip install selenium winotify
     ```

3. Update Course Details:
   - Open the `my_courses_notifier.py` file in a text editor.
   - Replace the values of `COURSE_ID`, `YEAR`, `SEMESTER`, and `DRIVER_PATH` with your desired course details and WebDriver path.

   ```python
   COURSE_ID = "20554"     // Replace with your desired course ID
   YEAR = "2024"           // Replace with the desired year (e.g., 2024)
   SEMESTER = "A"          // Replace with the desired semester (A, B, or C)
   DRIVER_PATH = "C:\Program Files\chromedriver.exe"   // Replace with the path to your Chrome WebDriver
   ```

5. Test the Script:
   - Run the script manually to ensure it's working as expected:

     ```
     python my_courses_notifier.py
     ```

6. Automate with Windows Task Scheduler:
   - Follow the instructions provided in the README to set up automation using Windows Task Scheduler.

7. Customize and Use:
   - The script will automatically notify you of new courses, and you can customize it further as per your requirements.


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


## Contributing

I welcome contributions to **MyCoursesNotifier**! If you have ideas, bug fixes, or improvements, feel free to contribute. You can:

- Report issues: Provide feedback or report any problems you encounter while using the script.
- Submit pull requests: If you've made enhancements or bug fixes, i will be happy to review and merge them.
- Improve documentation: Help make the README more informative and user-friendly.
- Provide feedback: input is valuable, even if you don't have code contributions.

Your contributions are appreciated and will help improve **MyCoursesNotifier** for the Open University community. Thank you for considering contributing!
