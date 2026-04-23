# Software-Hub

A modern web application showcasing a collection of utility programs built by Illia Senchyshyn. Browse, learn about, and download various tools designed to enhance productivity and system management.

## Features

- **Browse Programs**: Explore a curated collection of utility applications with detailed descriptions
- **Program Details**: View comprehensive information about each program including version, category, and screenshots
- **Easy Downloads**: Download executable files (.exe) directly from the website
- **Responsive Design**: Clean, user-friendly interface that works across devices
- **Program Categories**: Organized tools for system management, file handling, and productivity
- **About Page**: Learn more about the creator and the project

## Available Programs

1. **Auto Cliker** - Automate repetitive clicking tasks with customizable settings
2. **Empty Folder Hunter** - Find and delete empty folders from your computer
3. **File Drop** - Transfer files between PC and mobile devices via QR code (same WiFi required)
4. **Image Convertor** - Convert images to different formats with quality control
5. **Privacy Shield** - Blur your screen with a hotkey when away from your computer
6. **System Manager** - Monitor running processes and system resource usage

## Project Structure

```
Software-Hub/
├── app.py                 # Main Flask application
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Homepage with featured programs
│   ├── programs.html    # All programs listing
│   ├── program_detail.html # Individual program details
│   ├── about.html       # About page
│   └── 404.html         # Error page
└── static/              # Static files
    ├── css/
    │   └── style.css    # Stylesheet
    ├── js/
    │   └── main.js      # JavaScript functionality
    ├── images/
    │   ├── icons/       # Program logos
    │   └── screenshots/ # Program screenshots
    └── downloads/       # Executable files (.exe)
```

## Installation

### Requirements
- Python 3.7 or higher
- Flask

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Software-Hub.git
cd Software-Hub
```

2. Install required dependencies:
```bash
pip install flask
```

3. Ensure the following directories exist:
   - `static/downloads/` - Place your .exe files here
   - `static/images/icons/` - Place program logos here
   - `static/images/screenshots/` - Place program screenshots here

## Usage

### Running the Application

Start the Flask development server:
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`

### Development Features
- **Debug Mode**: Enabled by default for development with auto-reload on code changes
- **Template Rendering**: Dynamic page generation with program data
- **File Downloads**: Direct .exe file downloads from the website

## Adding New Programs

To add a new program, edit the `PROGRAMS` list in `app.py`:

```python
{
    "id": 7,
    "slug": "program-name",
    "title": "Program Title",
    "description": "Short description",
    "long_description": "Detailed description",
    "category": "tools",
    "version": "1.0",
    "icon": "images/icons/program-icon.jpg",
    "screenshot": "images/screenshots/screenshot.png",
    "file_name": "program.exe",
    "author": STUDENT_NAME,
}
```

Then add the corresponding files to the appropriate directories.

## Technologies Used

- **Backend**: Python with Flask web framework
- **Frontend**: HTML5, CSS3, JavaScript
- **Architecture**: Model-View-Template (MVT) pattern
- **File Serving**: Flask static file serving with custom download handling

## Features Explained

### Context Processor
The `inject_global_data()` function makes the programs list available to all templates, reducing code duplication.

### Dynamic Routing
Programs are accessed via URL slugs (e.g., `/programs/auto-cliker`) making URLs user-friendly and memorable.

### Error Handling
Custom 404 error page when programs are not found or download files are missing.

## Author

**Illia Senchyshyn**

## License

This project is open source. Feel free to use and modify for your needs.

## Support

If you encounter any issues or have suggestions for improvement, please create an issue in the repository.

---

**Note**: This is a demonstration project showcasing various utility applications. Download and use at your own discretion. 
