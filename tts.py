# TTS Logic, main file.

# TTS Window tools.
from tts_window import *

# Voice engine.
from pyttsx3 import init

# Threads.
from threading import Thread

# Time tools.
from time import strftime


# Tools loading logs.
logger.info('Libraries loaded.')

# Message boxes.
msg_box = QMessageBox();

logger.info('Message boxes loaded!')

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

    logger.info('Engine settings loaded and engine initializing was successfully!')

    if not save_res:
        def say():
            voice_engine.say(text)
            voice_engine.runAndWait()

        voiceline_thread = Thread(target=say, daemon=True)
        voiceline_thread.start()

        logger.info(f'Speaking... (Text: "{text}")')
        logger.warning('The application could not say anything because the female voice does not support the CIS languages.')

    elif save_res:
        logger.info('Starting QFileDialog...')

        save_path = QFileDialog.getExistingDirectory(window, 'Select path where will be your voiceline.', getattr(__import__('os'), 'path').expanduser('~') + '\\')

        if save_path != '':
            voice_engine.save_to_file(text, strftime(f'{save_path}/%Y-%m-%d-%H-%M-%S.mp3'))
            voice_engine.runAndWait()

            logger.info(f'Voiceline saved to path {save_path}.')

            msg_box.information(window, 'Text To Speech.', 'Voiceline saved!')
        else:
            logger.info('User canceled voiceline saving.')

# Connect function to button.
form.Speak.clicked.connect(lambda: speak(False))
form.SaveVoice.clicked.connect(lambda: speak(True))

logger.info('All functions connected to UI.')

# Starting window log.
logger.info('Starting window...')

# Run window.
window.show()
app.exec_()

# Process terminated log.
logger.info('Process terminated.')

