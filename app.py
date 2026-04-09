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
        "file_name": "downloads/emptyfilehunter.exe",
        "author": STUDENT_NAME,
    },
    {
        "id": 3,
        "slug": "file-drop",
        "title": "File Drop"
        "description": "An app that helps you to transfer data from pc to the phone files photos everything",
        "long_description": "In this app you scan an qar code and you will be abel to transfer data from pc to phone 'but you two devices need to be conected to the same wifi' and you can dounloud everything from the computer pictures files documentsd",
        "category": "tools",
        "version" "1",
        "icon": "",
        "screenshots": "images/screenshots/filedrop.png",
        "file_name": "downloads/filedrop.exe",
        "author": STUDENT_NAME,
    },
    {
        "id": 4,
        "slug": "image-convertor",
        "title": "Image Convertor",
        "description": "An app that help you conwert image to specific format you need",
        "long_description": "An app where you can chouse an picture you need adn convert in to the other format adn edit its sithe quoliti",
        "category": "tools",
        "version": "1",
        "icon": "",
        "screenshots": "images/screenshots/imageconvertor.png",
        "file_name": "downloads/image-converter.exe",
        "author": STUDENT_NAME
    {,
        "id": 5,
        "slug": "privacy-shield",
        "title": "Privacy Shild",
        "description": "With this app you can blur your screend wille you are awy from you computer so no one will see whats there",
        "long_description": "An app where you can chouse you hot key to blur of unblur your screen so no one will see what you have in your computer",
        "category": "tools",
        "version": "1",
        "icon": "",
        "screenshots": "iamges/screenshots/privacyshield.png",
        "file_name": "downloads/Privacyshield.exe",
        "author": STUDENT_NAME,
    },
    {
        "id": 6,
        "slug": "system-meneger",
        "title": "System Meneger",
        "description": "An app that help you to monitor the system ",
        "long_description": "An that help you to monitor every proces that is running on you computer and see how hard your system works",
        "version": "1",
        "icon": "",
        "screenshots": "images/screenshots/systemmaneger.png",
        "file_name": "downloads/systemmaneger.exe"
        "author" STUDENT_NAME,
    },
]
