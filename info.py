import datetime
    

# Function to get user input for course ID
def get_course_id():
    return input("Enter the course ID: ")

# Function to get user input for year
def get_year():
    while True:
        year = input("Enter the year: ")
        try:
            year = int(year)
            current_year = datetime.datetime.now().year
            if year >= current_year:
                return str(year)
                break
            else:
                print("Invalid year. Please enter the current year or a future year.")
        except ValueError:
            print("Invalid input. Please enter a valid year.")

# Function to get user input for semester
def get_semester():
    SEMESTER_DICT = {
        "A" : "05D0",
        "B" : "05D1",
        "C" : "05D2",
    }
    while True:
        semester = input("Enter the desired semester (A, B, or C): ").upper()
        if semester in SEMESTER_DICT:
            return SEMESTER_DICT[semester]
            break
        else:
            print("Invalid semester. Please enter A, B, or C.")


# setup function to interact with the user and generate the website URL and driver path
def setup():
    print("Please provide the following information:")
    course_id = get_course_id()
    year = get_year()
    semester = get_semester()
    return course_id, year, semester

