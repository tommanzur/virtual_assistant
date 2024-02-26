import os
import requests
from dotenv import load_dotenv

class TTS:
    """
    A class for Text-To-Speech (TTS) conversion using ElevenLabs API.

    Attributes:
        key (str): API key for ElevenLabs.
    """

    def __init__(self):
        """
        Initializes the TTS instance by loading the API key from environment variables.
        """
        load_dotenv()
        self.key = os.getenv('ELEVENLABS_API_KEY')
        if not self.key:
            raise ValueError("API key for ElevenLabs is not set in environment variables.")

    def process(self, text):
        """
        Converts the given text to speech.

        Args:
            text (str): The text to be converted to speech.

        Returns:
            str: The file name where the speech is saved.

        Raises:
            ValueError: If the response from the API is not successful.
        """
        CHUNK_SIZE = 1024
        url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"

        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.key
        }

        data = {
            "text": text,
            "model_id": "eleven_multilingual_v1",
            "voice_settings": {
                "stability": 0.55,
                "similarity_boost": 0.55
            }
        }

        response = requests.post(url, json=data, headers=headers)
        if response.status_code != 200:
            raise ValueError("Failed to get response from ElevenLabs API.")

        file_name = "static/response.mp3"
        with open(file_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
                    
        return file_name
