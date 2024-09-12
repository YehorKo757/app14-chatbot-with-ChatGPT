from openai import OpenAI
import os

API_KEY = os.getenv("CHATBOT")


class Chatbot:
    def __init__(self):
        self.client = OpenAI(api_key=API_KEY)

    def get_response(self, user_input):
        response_inner = self.client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5 # How accurate and diverse answers
        ).choice[0].text
        return response_inner


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)
