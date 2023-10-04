import webbrowser
import pywhatkit
from mouth.Speak import Speak
from mouth.Listen import onlisten
import json
import wikipedia
import random


def open_website(site):
    Speak(f"Opening {site['name']} for you.")
    webbrowser.open(site["url"])

    # Select and speak a random opening message
    opening_messages = site.get("opening_messages", [])
    if opening_messages:
        random_message = random.choice(opening_messages)
        Speak(random_message)


def search_wikipedia(query):
    try:
        search_result = wikipedia.summary(query, sentences=3)
        Speak(f"Here's a summary from Wikipedia: {search_result}")
    except wikipedia.exceptions.DisambiguationError:
        Speak("It seems there's a disambiguation issue. Please provide more details.")


def process_command(command, custom_json_file_path):
    with open(custom_json_file_path) as file:
        site_data = json.load(file)

    if 'play' in command:
        video = command.replace('play', '').strip()
        Speak('Here is a video for you: ' + video)
        pywhatkit.playonyt(video)

    found_in_json = False

    for site in site_data:
        if site["name"].lower() in command.lower():
            open_website(site)  # Pass the site dictionary to the function
            found_in_json = True
            break

    if not found_in_json:
        query = command.strip()
        search_wikipedia(query)  # Search Wikipedia if not found in JSON data


custom_json_file_path = 'D:\\Projects\\Big projects\\Ai\\Vaijal\\Data\\web.json'

command = onlisten()
process_command(command, custom_json_file_path)
