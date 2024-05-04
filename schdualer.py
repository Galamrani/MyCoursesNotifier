import schedule
import time
from datetime import datetime, timedelta
from notifier import check_and_notify, save_courses
from scraper import scrape_course_ids

def job():
    # Scrape course IDs from the website
    courses_ids = scrape_course_ids()
    
    # Check for new courses and notify if found
    check_and_notify(courses_ids)
    
    # Save the current course IDs to a CSV file for future comparison
    save_courses(courses_ids)


if __name__ == "__main__":
    # Run the job once immediately
    job()
    
    # Calculate end date (today's date + 14 days)
    end_date = datetime.now() + timedelta(days=14)

    # Schedule the job to run every day at 10:00 AM until the end date
    schedule.every().day.at("10:00").do(job).until(end_date)

    # Loop to run scheduled jobs
    while True:
        schedule.run_pending()
        time.sleep(60)
