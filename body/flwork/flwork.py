import json
import random
import time
import pyautogui
from mouth.Speak import Speak


def open_application_by_search(application_name):
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write(application_name)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)


def run_application_search(command):
    app_data_file = 'D:\\Projects\\Big projects\\Ai\\Vaijal\\Data\\appdata.json'

    with open(app_data_file) as file:
        app_data = json.load(file)

    for app_name, app_info in app_data.items():
        if any(keyword in command for keyword in app_info["keywords"]):
            open_application_by_search(app_name)
            app_messages_list = app_info.get("messages", [])

            if app_messages_list:
                random_message = random.choice(app_messages_list)
                Speak(random_message)

            break
    else:
        Speak("Sorry, I couldn't understand or open the requested application.")


def process_query(command):
    run_application_search(command)
