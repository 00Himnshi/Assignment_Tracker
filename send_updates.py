
import time
from main import check_updates
from send import send_message

def main():
    while True:
        # Calling check_updates function
        update = check_updates()
        
        # sending notification if there is an update
        if update != "NONE":
            send_message(update)
        
        # Wait for 2 hours (2 hours * 60 minutes * 60 seconds)
        time.sleep(2 * 60 * 60)

if __name__ == "__main__":
    main()