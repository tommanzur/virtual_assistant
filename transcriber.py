import openai

class Transcriber:
    """
    A class to transcribe audio to text using OpenAI's Whisper model.
    """
    
    def __init__(self):
        """
        Initializes the Transcriber class.
        """
        pass

    def transcribe(self, audio, file_name="audio.mp3"):
        """
        Transcribes the given audio file to text.

        Args:
            audio: The audio data to be transcribed.
            file_name (str, optional): The file name to save the audio. Defaults to 'audio.mp3'.

        Returns:
            str: The transcribed text from the audio.
        """
        try:
            with open(file_name, "wb") as audio_file:
                audio_file.write(audio.getbuffer())

            with open(file_name, "rb") as audio_file:
                transcript = openai.Audio.transcribe("whisper-1", audio_file)
                return transcript.text

        except Exception as e:
            # Handle exceptions such as file write/read errors or API errors
            print(f"An error occurred: {e}")
            return None
