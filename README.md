# Айка/Aika
 <u>Проект-основа голосового ассистента для ***дальнейших доработок***

The project is the basis of a voice assistant for further improvements</u>



![Логотип](https://sun9-77.userapi.com/impf/c847122/v847122018/1432e6/Mx3-hGNmY7M.jpg?size=755x755&quality=96&sign=75b9d3125d956c1176a726ea49c138bf&c_uniq_tag=JIO50u3KCug_MDNKU3TdYLVRaCSINBV7w3BCIkfE1bs&type=album "Логотип Айки")

------------------------------------------------------------------------
## Для чего был создан данный проект?
Айка представляет собой ***основу*** для разработки голосового ассистента  под самые разные задачи, ведь проще взять готовую основу и на ее базе создать тот продукт, который вам нужен 

## Условия для работы
Для работы дальнейшей работы установить следующие элементы:
1. [Python](https://www.python.org/downloads/)
2. Любую среду разработки для работы над проектом (Например [PyCharm](https://www.jetbrains.com/pycharm/))
3. Скачать сам [файл](https://github.com/BogolubDimiyan/PythonAssistent/tree/main/src) и заупустить в среде разработки

## Шаги установки
Для установки программы достаточно:
1. скачать [файл](https://github.com/BogolubDimiyan/PythonAssistent/tree/main/src)
2. Заупстить 

## Порядок использования
### Использование
После запуска программы, "Айка" приветствует вас и готова к выполнению команд. Вы можете давать команды, произнося их в микрофон.
***
### Примеры команд
#### Выключение компьютера:

***Команда: "Выключи компьютер"***

Действие: Компьютер будет выключен через 1 секунду.

Примечание: Команда чувствительна к регистру, но в коде она приведена к нижнему регистру для удобства.

***

### Дополнительные опции и флаги
В **текущей версии** "Айка" ***не*** поддерживает дополнительные опции или флаги. Однако, вы можете легко расширить функциональность, добавив новые команды в функцию ```execute_command```.

## Подробная документация
Для более подробной информации о библиотеках и командах, используемых в проекте, вы можете обратиться к следующим ресурсам:

[pyttsx3 Documentation](https://pyttsx3.readthedocs.io/_/downloads/en/latest/pdf/)

[SpeechRecognition Documentation](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition)

[pyautogui Documentation](https://pyautogui.readthedocs.io/en/latest/)

### Примечания
***Индекс микрофона:*** В коде используется _индекс микрофона 5_. Если у вас несколько микрофонов, вы можете изменить этот индекс в строке:\
```mic = sr.Microphone(device_index=5).```

Если "Айка" **не** может распознать вашу речь, <u>она сообщит об этом</u>.
***

В случае необходимости более детального разбора кода можете посмотреть видео [тут](https://www.youtube.com/watch?v=iIOKHKwi2TE)
