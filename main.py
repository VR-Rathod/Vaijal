import time
from mouth.Listen import onlisten
from body.flwork.flwork import process_query
from body.nlwork.opening import process_command


def main_loop():
    stop_keywords = ["stop", "ruk", "wait", "off"]

    while True:
        command = onlisten()  # Allow manual input
        if not command:
            command = onlisten()  # If no manual input, use voice recognition
            print("Recognized:", command)

        if command:  # Check if a command was recognized or manually entered
            if any(keyword in command.lower() for keyword in stop_keywords):
                print("Goodbye, sir...")
                break
            else:
                if any(keyword in command.lower() for keyword in ["play", "search", "find", "wiki"]):
                    process_command(command)  # Call the appropriate function in opening.py
                else:
                    result = process_query(command=command)  # Call process_query with the recognized or entered command
                    if result:
                        print(result)
                    else:
                        print("I am Ruto")
        else:
            print("Listening...")

        time.sleep(3)


if __name__ == "__main__":
    main_loop()
