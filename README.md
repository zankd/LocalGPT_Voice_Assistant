# Using llamafile as a Server

## Overview
This Python script serves as a local server for the llamafile project, enabling local processing of user queries using the OpenAI API. It listens for user commands via voice input, processes them using the llamafile model, and responds accordingly. The assistant is capable of providing helpful responses to user queries, making it suitable for a variety of tasks.

## Dependencies
- Python 3.x
- OpenAI Python library (`openai`)
- Pyttsx3 for text-to-speech conversion (`pyttsx3`)
- SpeechRecognition for speech recognition (`speech_recognition`)
- Pynput for keyboard monitoring (`pynput`)

## Configuration
- Configure OpenAI API to use a local server by setting the `base_url` parameter to the desired URL.
- Ensure that the `api_key` parameter is set accordingly.

## Usage
1. Install dependencies using `pip install -r requirements.txt`.
2. Run the script using `python llamafile_server.py`.
3. Choose between starting a new session or continuing an existing one.
4. Speak your query when prompted.
5. The assistant will process your query and respond accordingly.

## Features
- Provides a simple interface for interacting with the llamafile model.
- Supports voice input for user queries.
- Processes user commands using the llamafile model to generate responses.
- Implements error handling and retries for robustness.

## Additional Notes
- Existing session management is not implemented in this version of the script.
- Users can exit the script by saying "exit" or "exit." during the conversation.

## License
This project is licensed under the [MIT License](LICENSE).

