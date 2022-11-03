import os
from num2words import num2words
import config
import stt
import tts
from fuzzywuzzy import fuzz
from datetime import datetime
import webbrowser
import random
import pyjokes
from vosk import Model, KaldiRecognizer
import pyaudio
print(f"{config.VA_NAME} начал свою работу ...")


def va_respond(voice: str):
    print(voice)
    if voice.startswith(config.VA_ALIAS):

        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            tts.va_speak("Что?")
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc
def num2text(cmd: str):
    time = datetime.now()
    str(time)
def execute_cmd(cmd: str):
    if cmd == 'help':
        # help
        text = "Я умею:"
        text += "произносить время "
        text += "рассказывать анекдоты "
        text += "открывать браузер"
        text += 'выключать компьтер'
        tts.va_speak(text)
        pass
    elif cmd == 'ctime':
        text = num2text('Сейчас' + {time})
        tts.va_speak(text)
    elif cmd == 'hello':
        tts.va_speak('приветсвую')
    elif cmd == 'joke':
        jokes = ['у меня нету чувства юмора']

        tts.va_speak(random.choice(jokes))

    elif cmd == 'open_browser':
        webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))
        webbrowser.get('Chrome').open_new_tab('youtube.com')
        webbrowser.get('Chrome').open_new_tab('python.org')
    elif cmd == 'name':
        tts.va_speak(f'Меня зовут {config.VA_NAME}')
    elif cmd == 'shutdown':
        os.system('shutdown -s')
        tts.va_speak('хорошо, слушаюсь')
    elif cmd == 'bye':
        tts.va_speak('досвидания,хорошего дня')
    elif cmd == 'mood':
        tts.va_speak('хорошо, а у тебя')


stt.va_listen(va_respond)
#MADE BY BOGDAN KOVALSKY  telegram https://t.me/Magicxxxxxxx
#MADE BY BOGDAN KOVALSKY, telegram https://t.me/Magicxxxxxxx
