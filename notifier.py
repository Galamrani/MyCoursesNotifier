import csv, os
import http.client, urllib


# Constants
CSV_FILE = "course_identifiers.csv"


# Constants
CSV_FILE = "course_identifiers.csv"

# Function to check for new courses and notify the user if found
def check_and_notify(existing_course_ids):
    try:
        if os.path.exists(CSV_FILE):
            new_course_ids = []
            with open(CSV_FILE, "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)  # Skip header row

                # Read course IDs from the CSV file
                csv_course_ids = {row[0] for row in csv_reader}

                # Compare existing course IDs with those in the CSV file
                for course_id in existing_course_ids:
                    if str(course_id) not in csv_course_ids:
                        new_course_ids.append(str(course_id))

                # Notify the user about new courses
                if new_course_ids:
                    notify_new_courses(new_course_ids)
                else:
                    print("No new courses found.")

    except (FileNotFoundError, PermissionError, csv.Error) as e:
        print(f"Error occurred while checking for new courses: {e}")


# Function to save course IDs to a CSV file
def save_courses(ids_list):
    try:
        with open(CSV_FILE, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Course ID"])  # Header row
            csv_writer.writerows([[course_id] for course_id in ids_list])
    except (PermissionError, csv.Error) as e:
        print(f"Error occurred while saving course IDs to CSV: {e}")



# Function to display a notification about new courses
def notify_new_courses(courses_ids):
    
    # before running this script, make sure to set up the PUSHOVER_TOKEN and PUSHOVER_USER_KEY
    # You can set them using the following commands:
    # export PUSHOVER_TOKEN="your_pushover_token"
    # export PUSHOVER_USER_KEY="your_pushover_user_key"
    # use echo command to see if you set them up: echo $PUSHOVER_TOKEN, echo $PUSHOVER_USER_KEY

    PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN")
    PUSHOVER_USER_KEY = os.getenv("PUSHOVER_USER_KEY")

    if not PUSHOVER_TOKEN or not PUSHOVER_USER_KEY:
        print("Error: PUSHOVER_TOKEN or PUSHOVER_USER_KEY not set.")
        return

    message = "New courses are now available:\n"
    for course in courses_ids:
        message += course
    
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": PUSHOVER_TOKEN,
        "user": PUSHOVER_USER_KEY,
        "title": "Course Notifier",
        "message": message,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()









