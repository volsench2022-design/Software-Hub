from pathlib import Path

from flask import Flask, abort, render_template, send_from_directory, url_for

# Створюємо головний Flask-застосунок.
# name допомагає Flask зрозуміти, де шукати шаблони та статичні файли.
app = Flask(__name__)

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
        "title": "File Drop",
        "description": "An app that helps you to transfer data from pc to the phone files photos everything",
        "long_description": "In this app you scan an qar code and you will be abel to transfer data from pc to phone 'but you two devices need to be conected to the same wifi' and you can dounloud everything from the computer pictures files documentsd",
        "category": "tools",
        "version": "1",
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
        "author": STUDENT_NAME,
    },
    {
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
        "file_name": "downloads/systemmaneger.exe",
        "author": STUDENT_NAME,
    },
]
# Абсолютний шлях до папки, де лежать файли для завантаження (. ехе).
# app.static_folder -> зазвичай це папка static, а далі додаємо підпапку downloads.
DOWNLOADS_DIR = Path(app.static_folder) / "downloads"

def get_program_by_slug(slug: str):
    """Повертає словник програми за iї короткою адресою slug. """
    # next ( ... ) бере перший елемент, який підходить під умову.
    # Генератор (program for program in PROGRAMS ... ) перебирає список програм.
    # Якщо нічого не знайдено, повертаємо None (завдяки другому аргументу next).
    return next((program for program in PROGRAMS if program["slug"] == slug), None)

@app.context_processor
def inject_global_data():
    """Робить список програм доступним у всіх шаблонах. """
    # Усі пари ключ-значення з цього словника автоматично доступні
    # в Jinjа-шаблонах (base.html, index.html, programs.html тощо).
    # Наприклад, у шаблоні можна звертатися до змінної programs без
    # явної передачі її в кожному render_template( ... ).
    return {"programs": PROGRAMS}

@app.route("/")
def home():
    """Головна сторінка з кількома рекомендованими програмами. """
    # Беремо перші 3 елементи списку (зріз list slicing).
    # Це простий спосіб показати "рекомендовані" програми
    featured_programs = PROGRAMS [ : 3]
    # render_template рендерить HTML-файл з папки templates
    # і підставляє передані змінні в шаблон.
    return render_template("index.html", featured_programs=featured_programs)

@app.route("/programs")
def programs_list():
    """Сторінка з усім каталогом програм. """
    # Передаємо в шаблон повний список програм.
    return render_template("programs.html", programs=PROGRAMS)

@app.route("/programs/<slug>")
def program_detail(slug):
    """Детальна сторінка конкретної програми."""
    # <slug> у маршруті означає: Flask дістане частину URL
    # і передасть її у параметр функції slug.
    program = get_program_by_slug(slug)
    # Якщо програма не знайдена, повертаємо стандартну НТТР-помилку 404.
    # Далі цю помилку перехоплює наш обробник @app.errorhandler(404).
    if not program:
        abort(404)
    # Якщо все добре, рендеримо детальну сторінку конкретної програми.
    return render_template("program_detail.html", program=program)

@app.route("/about")
def about():
    """Сторінка з інформацією про автора сайту."""
    return render_template("about.html")

@app.route("/download/<slug>")
def download_program(slug):
    """Віддає .ехе файл з папки static/downloads. """
    # Крок 1. Шукаємо програму за slug, щоб зрозуміти, який файл видавати.
    program = get_program_by_slug(slug)
    if not program:
        # Якщо такого slug немає, повертаємо 404.
        abort(404)
    
    # Крок 2. Формуємо повний шлях до файлу.
    # Наприклад: static/downloads/pixel-painter.exe
    file_path = DOWNLOADS_DIR / program["file_name"]
    if not file_path.exists():
        # Якщо запис у каталозі є, а файлу на диску немає,
        # повідомляємо про це через 404 з поясненням.
        abort(404, description="Файл для завантаження поки що не доданий до проєкту.")
    
    # Крок 3. Відправляємо файл користувачу.
    # as_attachment=True -> браузер пропонує завантажити файл.
    # download_name -> iм'я, з яким файл буде збережено у користувача.
    return send_from_directory(
        DOWNLOADS_DIR,
        program["file_name"],
        as_attachment=True,
        download_name=program["file_name"],
    )

@app.errorhandler(404)
def page_not_found(error):
    """Користувацька сторінка помилки 404. """
    # Flask викличе цю функцію для всіх 404 помилок у застосунку.
    # Повертаємо власний HTML-шаблон і явний статус-код 404.
    return render_template("404.html", error=error), 404

if __name__ == "__main__":
    # Цей блок виконується лише при прямому запуску файлу:
    # python app.py
    # debug=True вмикає авто-перезапуск при змінах і детальні помилки.
    # У production-запуску debug зазвичай вимикають.
    app.run(debug=True)
