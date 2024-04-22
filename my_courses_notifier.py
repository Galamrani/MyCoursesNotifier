import time, csv, os, selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from winotify import Notification, audio


# Constants
COURSE_ID = "20554"     # Replace with your desired course ID
YEAR = "2024"           # Replace with the desired year
SEMESTER  = "A"         # Replace with the desired semester (A OR B OR C)
DRIVER_PATH  = "C:\Program Files\chromedriver.exe"   # Replace with the path to your Chrome WebDriver 
CSV_FILE = "course_identifiers.csv"
SEMESTER_DICT = {
    "A" : "05D0",
    "B" : "05D1",
    "C" : "05D2",
}
WEBSITE = "https://sheilta.apps.openu.ac.il/CoursesRegistration/Pages/GroupSearchResults.aspx?Semester=" + YEAR + "%u" + SEMESTER_DICT[SEMESTER]+ "&CourseIDs=," + COURSE_ID  + ",&Degree=0&GeographicalArea=,01,02,03,04,05,06,07,09,&InstructionHours=00:01&Days=111111&Page=1"


# Function to scrape course IDs and study group elements from the website
def scrape_course_ids():
    try:
        courses_ids = []
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(WEBSITE)

        # Find elements containing course codes and study group information
        main_table = driver.find_element_by_id("main_table")
        course_code_elements = main_table.find_elements_by_xpath("//tr/td[5]")
        study_group_elements = main_table.find_elements_by_xpath("//tr/td[7]")
        course_code_elements.pop(-1)

        # Collect course IDs and study group elements into a list
        for i in range(len(course_code_elements )):
            course_id = (course_code_elements[i].text, study_group_elements[i].text)
            courses_ids.append(course_id)
        
        time.sleep(1)
        driver.quit()
        return courses_ids
    
    except Exception as e:
        print(f"Error occurred during web scraping: {str(e)}")
        return []


# Function to check for new courses and notify the user if found
def check_and_notify_new_courses(existing_ids):

    if os.path.exists(CSV_FILE):
        courses_ids = []
        with open(CSV_FILE, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            try:
                csv_data = next(csv_reader)
            except StopIteration:
                csv_data = []  
            
            # Compare existing course IDs with those in the CSV file          
            for course_id  in existing_ids:
                course_id_str = str(course_id)
                if course_id_str not in csv_data:
                    courses_ids.append(course_id_str)
            
            # Notify the user about new courses
            if len(courses_ids) > 0:
                notify_new_course(courses_ids)


# Function to save course IDs to a CSV file
def save_course_ids_to_csv(ids_list):
    with open(CSV_FILE, "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(ids_list)


# Function to display a notification about new courses
def notify_new_course(courses_ids):
    separator = ','
    result_string = separator.join(courses_ids)
    toast = Notification(app_id = "MyCoursesNotifier",
                         title = "New courses are now available for enrollment in Course ID " + COURSE_ID,
                         msg = result_string,
                         duration = "long", 
                         icon=os.path.join(os.path.dirname(__file__), "icon.jpg"))
    
    toast.set_audio(audio.Default, loop=False)
    toast.show()

def justtest():
    pass

if __name__ == "__main__":
    courses_ids = scrape_course_ids()   # Scrape course IDs from the website
    check_and_notify_new_courses(courses_ids)   # Check for new courses and notify if found
    save_course_ids_to_csv(courses_ids) # Save the current course IDs to a CSV file for future comparison






