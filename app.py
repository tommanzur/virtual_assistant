import os
import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request
import json
from transcriber import Transcriber
from llm import LLM
from weather import Weather
from tts import TTS
from mac_command import MacCommand

# Load environment variables and validate their presence
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
elevenlabs_key = os.getenv('ELEVENLABS_API_KEY')
if not all([openai_api_key, elevenlabs_key]):
    raise EnvironmentError("Missing required environment variables")

openai.api_key = openai_api_key

app = Flask(__name__)
llm = LLM()
transcriber = Transcriber()

@app.route("/")
def index():
    """
    Render the main page of the application.
    """
    return render_template("recorder.html")

@app.route("/audio", methods=["POST"])
def audio():
    """
    Handle the audio input, transcribe it, process the command and execute the relevant function.
    """
    audio_file = request.files.get("audio.mp3")
    if not audio_file:
        return {"result": "error", "message": "No audio file provided"}

    try:
        text = transcriber.transcribe(audio_file)
        function_name, args, message = llm.process_functions(text)

        if function_name:
            return handle_function(function_name, args, text, message)
        else:
            return respond_with_default_message(text)
    except Exception as e:
        return {"result": "error", "message": str(e)}

def handle_function(function_name, args, text, message):
    """
    Handle the execution of a specific function based on the function_name.
    """
    if function_name == "get_weather":
        return execute_weather_function(args, text, message)
    elif function_name == "send_email":
        # Placeholder for send email functionality
        return respond("Email sending not implemented yet")
    elif function_name == "open_safari":
        return execute_open_safari_function(args, text)
    else:
        return respond("Function not recognized")

def execute_weather_function(args, text, message):
    """
    Execute the weather function and return the response.
    """
    weather_response = Weather().get(args["location"])
    weather_response = json.dumps(weather_response)
    return process_response(text, message, "get_weather", weather_response)

def execute_open_safari_function(args, text):
    """
    Execute the open Safari function and return the response.
    """
    MacCommand().open_safari(args["website"])
    return respond(f"Safari opened at {args['website']}")

def respond_with_default_message(text):
    """
    Return a default response when no function is recognized.
    """
    return respond("I'm not sure what you're talking about")

def respond(message):
    """
    Process the given message through TTS and return the response.
    """
    tts_file = TTS().process(message)
    return {"result": "ok", "text": message, "file": tts_file}

def process_response(text, message, function_name, function_response):
    """
    Process the response from a function execution.
    """
    final_response = llm.process_response(text, message, function_name, function_response)
    return respond(final_response)

if __name__ == "__main__":
    app.run(debug=True)
