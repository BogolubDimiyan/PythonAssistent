# импорт всех необходимых библиотек
import pyttsx3
engine = pyttsx3.init()
import speech_recognition as sr
import pyautogui as pg
import os

# начало работы программы
engine.say("Здравствуйте! Меня зовут АйкА")
engine.runAndWait()


# Запись речи
def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        audio = r.listen(source)
    try:
        our_speech = r.recognize_google(audio, language="ru-RU")
        print("Вы сказали:" + our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ОШИБКА"
    except sr.RequestError:
        return "ОШИБКА"
    # return input("Команда")


# Блок со всеми возможностями Айки
def TurnOffComputer():
    if "Выключи компьютер" in message:
        engine.say("Выключаю")
        engine.runAndWait()
        os.system('shutdown -s')
    else:
        engine.say("Чееее?")
        engine.runAndWait()

def open_Browser():
    engine.say("Открываю!")




# Индекс записывающего устройства
mic = sr.Microphone(device_index=5)


# Запись речи
def say_message(message):
    print("система:" + message)


if __name__ == "__main__":
    while True:
        command = listen_command()
      