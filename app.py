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
        "icon": "mageis/icons/pixel-painter.svg",
        "screenshot": "images/screenshots/autocliker.png",
        "file_name": "downloads/autocliker.exe",
        "author": STUDENT_NAME,
    },
]