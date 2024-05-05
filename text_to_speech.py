import pyttsx3


def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()


# Input text
text = input("Enter the text you want to convert to speech: ")

# Convert text to speech using default properties
text_to_speech(text)
