import requests
from bs4 import BeautifulSoup
import os

# Output file to store all assignments posted till now
all_assignments = 'assignments.txt'

# Predefining all the URLs/Paths needed to reach the assignment section
login_url = 'http://e-exam.igdtuw.ac.in/exam/login/index.php'
course_url = 'http://e-exam.igdtuw.ac.in/exam/course/view.php?id=129'

# login credentials:
login_details = {
    'username': 'STUDENT_USERNAME',
    'password': 'STUDENT_PASSWORD'
}

# Start a session and login
session = requests.Session()
response = session.post(login_url, data=login_details)
def check_updates():
    global response
    if  response.ok:
        print("Login successful!")

        # Access the course page to navigate to the assignment section
        response = session.get(course_url)

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find and print information about new assignments
        page_content = soup.find('div', id='page-content')

        # Extract course sections
        sections = page_content.find_all('li', class_='section main clearfix')

        current_assignments = []

        for section in sections:
            # Extract section title
            section_title = section.find('h3', class_='sectionname')
            if section_title:
                print(f"Section Title: {section_title.get_text(strip=True)}")

            # Extract activities within this section
            activities = section.find_all('li', class_='activity')
            for activity in activities:
                activity_link = activity.find('a')
                if activity_link:
                    activity_name = activity_link.get_text(strip=True)
                    activity_url = activity_link.get('href')
                    if "Lab Exercise" in activity_name or 'Assignment' in activity_name:
                        current_assignments.append(f"{activity_name}: {activity_url}")
                        print(f"  Activity Name: {activity_name}")
                        print(f"  Activity URL: {activity_url}")

        # Load previous assignments
        previous_assignments = []
        if os.path.exists(all_assignments):
            with open(all_assignments, 'r') as file:
                previous_assignments = file.read().splitlines()

        # Compare and notify of changes
        new_assignments = set(current_assignments) - set(previous_assignments)
        if new_assignments:
            print("\nNew assignments detected:")
            text = ""
            for assignment in new_assignments:
                text += assignment+'\n'
                print(assignment)

            # Save current assignments to file
            with open(all_assignments, 'w') as file:
                file.write('\n'.join(current_assignments))
        else:
            print("\nNo new assignments.")
    else:
        print("Login failed!")
        exit()
import requests
from bs4 import BeautifulSoup


def extract_assignment_details(url):
    global response
    # Check if the request was successful
    if response.ok :
        # Parse the HTML content of the page
        response = session.get(url)
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Initialize a dictionary to store the extracted details
        details = {
            'submissionStatus': '',
            'gradingStatus': '',
            'dueDate': '',
            'timeRemaining': '',
            'lastModified': '',
        }
        rawdata=soup.find('tbody')
        rows = rawdata.find_all('tr')
            
        for row in rows:
                # Find the two columns in the row
            cols = row.find_all('td')
            if len(cols) == 2:
                    # Extract text from the second column
                key = cols[0].get_text(strip=True)
                value = cols[1].get_text(strip=True)
                    
                    # Map the key to the dictionary
                if key == 'Submission status':
                    details['submissionStatus'] = value
                elif key == 'Grading status':
                    details['gradingStatus'] = value
                elif key == 'Due date':
                    details['dueDate'] = value
                elif key == 'Time remaining':
                    details['timeRemaining'] = value
                elif key == 'Last modified':
                    details['lastModified'] = value
        for key,value in details.items():
            print(key ," : ",value)

def get_submit_url(url):
    return url+"&action=editsubmission"




def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Check for new assignments")
        print("2. Extract assignment details")
        print("3. Get submit URL")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            check_updates()
        elif choice == '2':
            url = input("Enter the assignment URL: ")
            extract_assignment_details(url)
        elif choice == '3':
            url = input("Enter the assignment URL: ")
            submit_url = get_submit_url(url)
            print(f"Submit URL: {submit_url}")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    menu()