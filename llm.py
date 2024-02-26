import openai
import json
from mac_command import MacCommand

class LLM:
    """
    Class to utilize any Large Language Model (LLM) to process text
    and return a callable function with its parameters. 
    The default model used is "gpt-3.5-turbo-0613", but this can be adjusted with 
    prompt engineering for other models.
    """

    def __init__(self):
        """
        Initializes the LLM instance.
        """
        pass
    
    def process_functions(self, text):
        """
        Processes the input text to determine the appropriate function to call.
        Utilizes OpenAI's ChatCompletion to interact with the LLM.

        Args:
            text (str): The user's input text to be processed.

        Returns:
            tuple: A tuple containing the function name, arguments, and message, 
                   if a function call is identified. Otherwise, returns None.
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                {"role": "system", "content": "Eres un asistente argentino muy gracioso"},  # Adjusted assistant's description
                {"role": "user", "content": text},
            ],
            functions=[
                # Define the functions that the LLM can call
                {"name": "get_weather", "description": "Get the current weather", "parameters": {...}},
                {"name": "send_email", "description": "Send an email", "parameters": {...}},
                {"name": "open_safari", "description": "Open the Safari browser to a specific site", "parameters": {...}},  # Changed to open_safari
            ],
            function_call="auto",
        )
        
        message = response["choices"][0]["message"]
        
        if message.get("function_call"):
            # If GPT has identified a function to call
            function_name = message["function_call"]["name"]
            args = json.loads(message["function_call"]["arguments"])
            print("Function to call: " + function_name)
            return function_name, args, message
        
        return None, None, message
    
    def process_response(self, text, message, function_name, function_response):
        """
        Processes the function's response to generate a natural language response.

        Args:
            text (str): The original user input text.
            message (dict): The original message from the LLM.
            function_name (str): The name of the function that was called.
            function_response (str): The response from the called function.

        Returns:
            str: A natural language response based on the function's response.
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                {"role": "system", "content": "You are a witty assistant"},  # Adjusted assistant's description
                {"role": "user", "content": text},
                message,
                {"role": "function", "name": function_name, "content": function_response},
            ],
        )
        return response["choices"][0]["message"]["content"]
