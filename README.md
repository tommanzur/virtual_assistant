# Virtual Assistant
This GitHub repository hosts an innovative project: a virtual assistant powered by OpenAI's GPT-3.5-Turbo-0613 language model. The assistant is designed for speech-to-speech interaction, seamlessly working in Spanish, which makes it highly accessible and user-friendly for Spanish-speaking users. The core functionality revolves around understanding spoken Spanish queries and responding verbally, offering a hands-free, conversational experience. Additionally, this virtual assistant is capable of performing a wide range of tasks thanks to its integration with the OpenAI API.

## Configuration

To run this project, you need to:

1. Clone or download this repository.
2. Optionally, create a virtual environment for better dependency management.
3. Install the necessary dependencies by running the command:
```Bash
pip install -r requirements.txt
```
4. Create a .env file in the project root.
5. In the ```.env``` file, add the following keys as per the requirements of the project demonstrated in the video (and this repository):
```Bash
OPENAI_API_KEY=XXXXXX
ELEVENLABS_API_KEY=XXXXXX
WEATHER_API_KEY=XXXXXX
```

## Customizations

There are several aspects of the project you might want to customize, such as:

- In the LLM class, there is an option to modify the assistant's speech to avoid inappropriate language. This is used in two places in the file.
- In the PcCommand class, Chrome is opened by searching for its executable in a fixed path for Windows. You can modify this to locate the executable on Mac/Linux systems.

## Execution

This project uses Flask as its web framework. You can start the server in debug mode on the default port (5000) using the command:

```Bash
flask --app app run --debug
```

To interact with the assistant:

1. Open your browser and navigate to http://localhost:5000.
2. Click to start recording (it will ask for permission). Click again to stop recording.
