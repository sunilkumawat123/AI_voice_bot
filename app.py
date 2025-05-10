import os
import time
import speech_recognition as sr
from gtts import gTTS
import playsound
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

class AI_Assistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.full_transcript = [
            {"role": "system", "content": "You are a receptionist at a dental clinic. Be helpful, friendly, and efficient."},
        ]

    def start_transcription(self):
        print("Please start speaking...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            transcript = self.recognizer.recognize_google(audio)
            print(f"Transcript: {transcript}")
            self.generate_ai_response(transcript)
        except Exception as e:
            print(f"Error: {e}")

    def generate_ai_response(self, transcript):
        self.full_transcript.append({"role": "user", "content": transcript})
        print(f"\nPatient: {transcript}")

        conversation = self.get_full_conversation()
        response = model.generate_content(conversation)
        ai_response = response.text.strip()

        self.generate_audio(ai_response)
        self.full_transcript.append({"role": "assistant", "content": ai_response})

    def get_full_conversation(self):
        return "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in self.full_transcript])

    def generate_audio(self, text):
        print(f"\nAI Receptionist: {text}")
        tts = gTTS(text=text, lang='en')
        filename = "response.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

# Run
if __name__ == "__main__":
    greeting = "Thank you for calling Vancouver dental clinic. My name is Sandy, how may I assist you?"
    ai_assistant = AI_Assistant()
    ai_assistant.generate_audio(greeting)
    while True:
        ai_assistant.start_transcription()
