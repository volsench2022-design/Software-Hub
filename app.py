from pathlib import Path

from flask import Flask, abort, render_template, send_from_directory, url_for

# Створюємо головний Flask-застосунок.
# name допомагає Flask зрозуміти, де шукати шаблони та статичні файли.
app = Flask(_name_)

# Ім'я учня використовується як автор для всіх демонстраційних програм.
# Достатньо змінити це значення в одному місці, і воно оновиться всюди.
STUDENT_NAME = "Illia Senchyshyn"

PROGRAMS = [
    {
        "id": 1,
        "slug": "auto-cliker",
        "title": "Auto Cliker",
        "description": "An auto cliker that you can use for any of your tasks.",
        "long_description": "An simple auto cliker were you can edit how it will work and adapt it for your tasks",
        "category": "tools",
        "version": "1.4",
        "icon": "",
        "screenshots": "images/screenshots/autocliker.png",
        "file_name": "downloads/autocliker.exe",
        "author": STUDENT_NAME,
    },
]
[
    {
        "id": 2,
        "slug": "empty-folder-hunter",
        "title": "Empty folder hunter",
        "description": "An app that finds and empty folders in your computer and it helps you to delite them",
        "long_description": "An app that serches for empty folders and finds how many are in your conputer adn asks you if you wana to delite them ",
        "category": "tools",
        "version":"1",
        "icon": "",
        "screenshots": "images/screenshots/emptyfolderhunter.png",
        "file_name": "downloads/emptyfilehunter.py.exe"
        "author": STUDENT_NAME,
    }
]
[
    {
        "id": 3,
        "slug": "file-drop",
        "title": "File Drop"
        "description": "An app that helps you to transfer data from pc to the phone files photos everything",
        "long_description": "In this app you scan an qar code and you will be abel to transfer data from pc to phone 'but you two devices need to be conected to the same wifi' and you can dounloud everything from the computer pictures files documentsd",
        "category": "tools",
        "version" "1",
        "icon": ""
        "screenshots": "images/screenshots/filedrop.png",
        "file_name": "downloads/filedrop.png",
        "author": STUDENT_NAME,
    }
]