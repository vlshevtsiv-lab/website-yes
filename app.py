from pathlib import Path

from flask import Flask, abort, render_template, send_from_dictionary, url_for

app = Flask(__name__)

STUDENT_NAME = "2AM_VL4D"

PROGRAMS = [
    {
        "id": 1,
        "slug": "first-gui",
        "title": "First Gui",
        "description": "this program shows what you write.",
        "long_description": "This is a simple Python Tkinter GUI application that lets the user enter text and update a label with it. The label’s text and color change when the button is clicked, demonstrating basic widgets, event handling, and interactive interfaces.",
        "category": "GUI",
        "version": "1.0.0",
        "icon": "images/icons/first-gui.svg",
        "screenshot": "images/screenshots/Screenshot first gui.png",
        "file_name": "downloads/firstGUI.exe",
        "author": STUDENT_NAME,
    },
 {
        "id": 2,
        "slug": "auto-clicker",
        "title": "Auto Clicker",
        "description": "Automatically clicks for you.",
        "long_description": "This Python Tkinter application is an Auto Clicker that simulates mouse clicks at a user-defined speed. Users can enter clicks per second, start the auto-clicking process, and stop it with the ESC key. The app demonstrates GUI design, event handling, and integration with mouse and keyboard libraries.",
        "category": "Utility",
        "version": "1.0.0",
        "icon": "images/icons/auto-clicker.svg",
        "screenshot": "images/screenshots/Screenshot auto clicker.png",
        "file_name": "downloads/autoclicker1.exe",
        "author": STUDENT_NAME,
    },
 {
        "id": 3,
        "slug": "calculator",
        "title": "Calculator",
        "description": "A simple calculator application.",
        "long_description": "This is a basic Python Tkinter calculator that performs addition, subtraction, multiplication, and division operations. It demonstrates the use of buttons, entry fields, and label widgets to create a functional user interface.",
        "category": "GUI",
        "version": "1.0.0",
        "icon": "images/icons/calculator.svg",
        "screenshot": "images/screenshots/Screenshot calculator.png",
        "file_name": "downloads/calculator.exe",
        "author": STUDENT_NAME,
    },
 {
        "id": 4,
        "slug": "first-gui",
        "title": "First Gui",
        "description": "this program shows what you write.",
        "long_description": "This is a simple Python Tkinter GUI application that lets the user enter text and update a label with it. The label’s text and color change when the button is clicked, demonstrating basic widgets, event handling, and interactive interfaces.",
        "category": "GUI",
        "version": "1.0.0",
        "icon": "images/icons/first-gui.svg",
        "screenshot": "images/screenshots/Screenshot first gui.png",
        "file_name": "downloads/first-gui.exe",
        "author": STUDENT_NAME,
    },
     {
        "id": 4,
        "slug": "first-gui",
        "title": "First Gui",
        "description": "this program shows what you write.",
        "long_description": "This is a simple Python Tkinter GUI application that lets the user enter text and update a label with it. The label’s text and color change when the button is clicked, demonstrating basic widgets, event handling, and interactive interfaces.",
        "category": "GUI",
        "version": "1.0.0",
        "icon": "images/icons/first-gui.svg",
        "screenshot": "images/screenshots/Screenshot first gui.png",
        "file_name": "downloads/first-gui.exe",
        "author": STUDENT_NAME,
    },
]
