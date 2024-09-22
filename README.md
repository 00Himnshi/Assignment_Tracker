# Assignment Tracker

## Technologies Used
- Python
- BeautifulSoup
- Requests library
- Twilio API to send assignment updates on whatsapp

## Motivation
The motivation behind building this project came from realizing the need for it during the third semester of my engineering studies. We receive assignment details for our course on the ELMS portal of IGDTUW. However, every time we want to access it, we have to log in again and navigate through numerous webpages to finally find the relevant assignment updates. To solve this problem, I started working on this project. I explored various documentations about web scraping and eventually developed a solution using BeautifulSoup and the Requests library in Python.It also have functionality for automatically sending whatsapp updates when there is an update on the portal.


## Project Overview
### main.py
This is a menu-driven program that performs the following tasks:
- **Login Credentials:** The user provides login credentials to the program.
- **Session Management:** A common session is started to maintain the login session throughout subsequent requests.
- **Check Updates:** The `check_updates` function extracts assignments and checks if any new assignments have been posted by comparing them with previously posted assignments stored in a text file.
- **Extract Assignment Details:** The `extract_assignment_details` function scrapes necessary information such as submission status, grading status, due date, time remaining, and last modified date for an assignment based on the user's choice and displays it to the user.
- **Submit URL:** The `get_submit_url` function provides a direct link to the submission page of a particular assignment.

### send.py and send_updates
send.py contains python code for sending WhatsApp update using Twilio's API when there’s an update on the ERP portal.
send_updates useds the checkupdates function imported from main.py and triggers send.py to notify about any new assignments.

## Demo Video link:
https://drive.google.com/drive/folders/1VSAFCdkwYqYqGXZmB64IBTLzzibHrFAj?usp=sharing
