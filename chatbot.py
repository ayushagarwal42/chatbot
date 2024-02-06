import speech_recognition as sr #Library for performing speech recognition.
import pyttsx3 #Library for text-to-speech conversion
from datetime import datetime #Library for working with dates and times.
from googletrans import Translator #A translator from the Google Translate API.
    
#Function to capture audio from the microphone and perform speech recognition using Google's Speech Recognition service.
def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        
        print("Say something...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio) #audio to text
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Function to convert text to speech using the pyttsx3 library.
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

#Function to translate English text to Hindi using the Google Translate API.
def translate_english_to_hindi(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='hi')
    return translation.text

# Function to process the user's input and generate an appropriate response.
def process_user_input(text):
    # Adding my logic here to perform actions based on my input
    lower_text = text.lower()
    if "what is the day today" in lower_text:
        # Get the current day and format it
        current_day = datetime.now().strftime("%A")
        return f"Today is {current_day}."
    elif "what is the time" in lower_text:
        # Get the current time and format it
        # current_time = datetime.now().strftime("%H:%M")
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."
    elif "is the company open today" in lower_text:
        # Check if the current day is Monday to Friday
        current_day = datetime.now().strftime("%A")
        if current_day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            return f"like i am seeing today is {current_day} so the company is open."
        else:
            return f"The company is closed on {current_day}."
    elif "translate text to hindi" in lower_text:
        # Extract the text to be translated
        text_to_translate = lower_text.split("translate text to hindi")[1].strip()
        if text_to_translate:
            # Translate the text to Hindi
            translation = translate_english_to_hindi(text_to_translate)
            return f"Translation to Hindi: {translation}"
        else:
            return "Please provide the text to translate."
    elif "stop" in lower_text:
        return "Goodbye! Exiting..."
    else:
        # For any other input, simply echo back the user's input
        return f"{text}"

if __name__ == "__main__":
    while True:
        
        user_input = speech_to_text()

        if user_input:
            response = process_user_input(user_input)
            print(response)
            text_to_speech(response)
            if "stop" in user_input.lower():
                break
