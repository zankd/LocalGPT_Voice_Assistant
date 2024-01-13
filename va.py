# Using llamafile as server

import openai
import json
import pyttsx3
import speech_recognition as sr
import os
import subprocess
import time
from pynput import keyboard

# Configure OpenAI API to use local server
client = openai.OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="sk-no-key-required"
)

model_name = "LLaMA_CPP"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=0.3)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query

def send_message(thread_id, task):
    return client.beta.threads.messages.create(thread_id, role="user", content=task)

def run_assistant(prompt, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content  # Changed line
        except openai.InternalServerError as e:
            print(f"An internal server error occurred: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break
    return "I'm sorry, I'm having trouble processing your request right now."

def main_loop():
    user_choice = input("Type 'n' for a new session or 'Enter' for an existing session: ")
    if user_choice == 'n':
        user_name_input = input("Enter a name for this session: ")
        print(f"Session started with the name: {user_name_input}")
    else:
        print("Existing sessions not implemented in this script.")
        return

    while True:
        print("Speak now:")
        user_message = take_command()
        if user_message.lower() in {'exit', 'exit.'}:
            print("Exiting.")
            break
        assistant_message = run_assistant(user_message)
        print(f"{user_name_input}: {assistant_message}")
        speak(assistant_message)

if __name__ == "__main__":
    main_loop()
