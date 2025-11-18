---
title: "🏥 Hospital Information System"
description: "Manage hospitals & doctors with Python 🐍, modular architecture 🏗️, and a sleek Qt GUI 🎨."
tags: ["Python", "PyQt5", "Hospital", "MVC", "Desktop App"]
---

# 🏥 Hospital Information System

```yaml
overview: >
  This project is a desktop application built in Python following a 
  Three-Layer (MVC) architecture. It allows managing hospitals and doctors 
  in a modular and organized way.

---

# 📁 Project Structure

Hospital:
  Model:
    - __init__.py
    - doctor.py
    - crud_doctor.py
    - hospital.py
    - crud_hospital.py
  Controller:
    - __init__.py
    - search_controller.py
    - doctor_controller.py
    - hospital_controller.py
  ui_Qt:
    - form_doctor.ui
    - form_hospital.ui
    - main_window.ui
  ui_to_py:
    - __init__.py
    - form_doctor.py
    - form_hospital.py
    - main_window.py
  - __init__.py
  - .gitignore
  - README.md

---

# 🛠️ Technologies Used

technologies:
  - Python 3.x 🐍
  - PyQt5 / PySide6 🎨
  - Three-Layer Architecture 🏗️
  - Modular Programming & Namespaces 📦


---

#🎯 Functionalities

functionalities:
  - Create and store hospitals with their doctors 🏨
  - Manage doctors information (CRUD) 👨‍⚕️
  - Search doctor and hospital info by DNI 🔍
  - Display results in a table/grid in the GUI 📊


---

#🏛️ System Architecture

architecture:
  Model:
    description: "Handles Hospital and Doctor entities and CRUD operations"
  Controller:
    description: "Manages business logic and communication between Model and View"
  View:
    description: "Qt GUI interfaces, converted from .ui files to Python code"


---

# ⚡ Requirements

requirements:
  - Python 3.x
  - PyQt5 or PySide6
  - Recommended editors: VS Code or PyCharm


---

# 🚀 How to Run

steps:
  - Clone the repository: git clone <repository-url>
  - Create virtual environment: python -m venv venv
  - Activate virtual environment:
      windows: venv\Scripts\activate
      linux/mac: source venv/bin/activate
  - Install dependencies: pip install -r requirements.txt
  - Run application: python ui_to_py/main_window.py

---

# 📌 Notes

notes:
  - This is an academic project focused on layered architecture and modularity
  - Currently handles Hospital and Doctor entities only, but can be extended

---

# 💡 Author

author:
  name: "Santiago Osorio Jiménez"

message: "Thanks for using the Hospital Information System! 🏥💙"

---
