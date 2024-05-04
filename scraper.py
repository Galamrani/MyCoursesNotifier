from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from info import setup


# Function to scrape course IDs and study group elements from the website
def scrape_course_ids():
    
    COURSE_ID, YEAR, SEMESTER = setup()

    try:
        courses_ids = []
        website = f"https://sheilta.apps.openu.ac.il/CoursesRegistration/Pages/GroupSearchResults.aspx?Semester={YEAR}%u{SEMESTER}&CourseIDs=,{COURSE_ID},&Degree=0&GeographicalArea=,01,02,03,04,05,06,07,09,&InstructionHours=00:01&Days=111111&Page=1"

        service = Service(executable_path="./drivers/chromedriver")
        driver = webdriver.Chrome(service=service)
        driver.get(website)

        # Find elements containing course codes and study group information using the main_table ID
        course_code_elements = driver.find_elements(By.XPATH, "//table[@id='main_table']//tr/td[5]")
        study_group_elements = driver.find_elements(By.XPATH, "//table[@id='main_table']//tr/td[7]")

        course_code_elements.pop(-1)

        # Collect course IDs and study group elements into a list
        for i in range(len(course_code_elements)):
            course_id = (course_code_elements[i].text, study_group_elements[i].text)
            courses_ids.append(tuple(map(str, course_id)))

        return courses_ids
    
    except Exception as e:
        print(f"Error occurred during web scraping: {str(e)}")
        return []

    finally:
        if 'driver' in locals():
            driver.quit()


