# TTS Logic, main file.

# TTS Window tools.
from tts_window import *

# Voice engine.
from pyttsx3 import init

# Threads.
from threading import Thread

# Time tools.
from time import strftime


# Default voice rate.
DEFAULT_VOICE_RATE = 105

# Main speak function.
def speak(save_res: bool) -> None:
    text = form.Text.text()

    chosen_voice = [form.MaleVoice.isChecked(), form.FemaleVoice.isChecked()]
    voice = None

    if chosen_voice[0]:
        voice = 0
    elif chosen_voice[1]:
        voice = 1

    voice_engine = init()
    voice_engine.setProperty('voice', voice_engine.getProperty('voices')[voice].id)
    voice_engine.setProperty('rate', DEFAULT_VOICE_RATE)

    if not save_res:
        def say():
            voice_engine.say(text)
            voice_engine.runAndWait()

        voiceline_thread = Thread(target=say, daemon=True)
        voiceline_thread.start()

    elif save_res:
        save_path = QFileDialog.getExistingDirectory(window, 'Select path where will be your voiceline.')

        if save_path != '':
            voice_engine.save_to_file(text, strftime(f'{save_path}/%Y-%m-%d-%H-%M-%S.mp3'))
            voice_engine.runAndWait()

# Connect function to button.
form.Speak.clicked.connect(lambda: speak(False))
form.SaveVoice.clicked.connect(lambda: speak(True))

# Run window.
window.show()
app.exec_()

