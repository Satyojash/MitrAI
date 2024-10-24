import pyttsx3

def speak(audio):
    try:
        engine = pyttsx3.init()  # Initialize the TTS engine
        print("Engine initialized successfully.")
        
        voices = engine.getProperty('voices')  # Get available voices
        print(f"Available voices: {len(voices)}")
        
        # Set the voice to a specific option (0: male, 1: female)
        engine.setProperty('voice', voices[0].id)  # Change to male voice
        print("Voice set to male.")
        
        engine.say(audio)  # Speak the text
        engine.runAndWait()  # Wait for the speech to complete
        print("Speech completed.")
    
    except Exception as e:
        print(f"Error occurred: {e}")

# Call the function to say "Hello sir"
speak("Hello sir")
