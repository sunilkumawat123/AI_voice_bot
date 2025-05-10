📞 AI Receptionist Voice Assistant
This Python-based AI Voice Assistant simulates a dental clinic receptionist. It listens to speech input from a user, processes it with Google's Gemini (Generative AI), and responds using text-to-speech (TTS). The app uses only free tools (no OpenAI or paid APIs).

🚀 Features
🎙️ Speech-to-Text using Google Speech Recognition.

🧠 AI Response Generation using Google Gemini (gemini-1.5-flash).

🔊 Text-to-Speech using Google's gTTS (Google Text-to-Speech).

🗣️ Natural Conversation: Maintains full dialogue history for contextual understanding.

🧪 Self-contained: Works locally without needing any frontend or web interface.

📁 Project Structure
bash
Copy
Edit
AI-Voice-Assistant/
│
├── .env                   # Stores your GOOGLE_API_KEY
├── app.py                 # Main application script
├── requirements.txt       # Dependencies for the project
└── README.md              # This file
🛠️ Technologies Used
Library	Purpose
speech_recognition	Converts microphone input to text (STT)
google.generativeai	Accesses Google's Gemini AI model
gTTS	Converts text responses into speech (TTS)
playsound	Plays the generated audio files
python-dotenv	Loads environment variables (like API keys)

🔐 Environment Variables
Create a .env file in the root directory:

ini
Copy
Edit
GOOGLE_API_KEY=your_google_api_key_here
📦 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-repo/ai-voice-assistant.git
cd ai-voice-assistant
Create a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create the .env file (as described above).

🧠 How It Works
Step 1: Start Listening
The assistant uses SpeechRecognition to capture and transcribe voice input.

python
Copy
Edit
audio = self.recognizer.listen(source)
transcript = self.recognizer.recognize_google(audio)
Step 2: AI Response with Google Gemini
The transcribed text is passed to Gemini via generate_content() using gemini-1.5-flash.

python
Copy
Edit
response = model.generate_content(conversation)
Step 3: Speak the Response
The assistant responds using gTTS, saves the output as an MP3, plays it, and deletes the file.

python
Copy
Edit
tts = gTTS(text=text, lang='en')
tts.save(filename)
playsound.playsound(filename)
os.remove(filename)
🧪 Example Output
vbnet
Copy
Edit
Patient: What are your clinic hours?
AI Receptionist: Our clinic is open from 9 AM to 6 PM, Monday through Saturday.
