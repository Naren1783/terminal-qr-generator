# QR Code Generator (Python)

A simple command-line QR Code Generator built with Python. This application allows users to enter a website URL and generates a QR code that is saved as a PNG image.

---

## Features

- Generate QR codes from website URLs
- Command-line interface
- Automatically creates a `QR_Codes` folder
- Saves QR codes as PNG images
- User-friendly menu system
- Input validation

---

## Technologies Used

- Python 3
- qrcode
- Pillow (PIL)

---

## Project Structure

```
QR-Code-Generator-Python/
│
├── main.py
├── QR_Codes/
│   └── my_website_qr.png
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/qr-code-generator-python.git
```

Move into the project directory:

```bash
cd qr-code-generator-python
```

Install the required package:

```bash
pip install -r requirements.txt
```

---

## Requirements

Create a `requirements.txt` file containing:

```
qrcode[pil]
```

---

## Usage

Run the program:

```bash
python main.py
```

Example:

```
Welcome to QR Code Generator

1. Generate QR Code
2. Exit

Enter your choice: 1

Enter website URL:
https://github.com

Generating QR Code...

QR Code created successfully!
Saved at:
QR_Codes/my_website_qr.png
```

---

## Future Improvements

- Support text, email, phone numbers, and Wi-Fi QR codes
- Allow custom file names
- Custom QR colors
- Custom background colors
- Different QR sizes
- Download location selection
- GUI version using Tkinter
- Web version using HTML, CSS, and JavaScript

---

## Learning Outcomes

This project helped practice:

- Functions
- Loops
- Conditional statements
- Input validation
- Python modules
- File and directory management
- Working with third-party libraries
- Writing modular and reusable code

---

## Author

**Naren**

B.Tech Computer Science (Cyber Security)

