# Password Generator

This repository contains two versions of a password generator written in Python: a command-line version and a GUI version. Both versions allow users to generate random passwords based on user-defined criteria, such as length and character types (letters, numbers, symbols).

## Command-Line Password Generator

### Features
- Generates random passwords based on user-defined criteria
- Allows users to specify password length and character set preferences (letters, numbers, symbols)
- Simple and easy-to-use command-line interface

### Usage
1. Navigate to the `command-line` directory:

```bash
cd command-line
```
2.Run the password generator script:
```bash
python password_generator.py
```
+ Follow the prompts to enter the desired password length and character set preferences.

**Example**

```bash

Welcome to the Command-Line Password Generator!
Enter the desired password length: 12
Include letters? (yes/no): yes
Include numbers? (yes/no): yes
Include symbols? (yes/no): yes
Generated password: a1b2c3d4!@#$
```

# GUI Password Generator

## Features

   - Generates random passwords based on user-defined criteria
   - Allows users to specify password length and character set preferences (letters, numbers, symbols)
   - Provides a graphical user interface (GUI) for ease of use
   - Includes clipboard integration for easy copying of generated passwords

## Usage

**  Navigate to the gui directory:**

```bash
cd gui
```
**Run the password generator script:
**
```bash
python password_generator_gui.py
```
## GUI Interface

  -Enter the desired password length.
  + Select the character types to include (letters, numbers, symbols).
  + Click the "Generate Password" button to create a password.
  + Click the "Copy to Clipboard" button to copy the generated password to the clipboard.

![Screenshot 2024-08-07 at 10 28 59 PM](https://github.com/user-attachments/assets/c3b0a609-0aee-43e5-a5cd-48efb53470c2)

# Requirements

  + Python 3.x
  + Tkinter (for GUI version)
  + pyperclip (for clipboard integration)

# Installation

## Install the required packages using pip:

```bash
pip install tk pyperclip
```
# Code Overview
## Command-Line Version (command-line/password_generator.py)

  + generate_password(length, use_letters, use_numbers, use_symbols): Generates a random password based on the specified criteria.
  + get_user_preferences(): Prompts the user for password preferences (length, character types).
  + main(): Main function to run the command-line password generator.

## GUI Version (gui/password_generator_gui.py)
  + generate_password(length, use_letters, use_numbers, use_symbols): Generates a random password based on the specified criteria.
  + PasswordGeneratorApp: A class that creates the GUI application using Tkinter.
  +  __init__(self, root): Initializes the GUI components.
  +  generate_password(self): Generates and displays the password based on user input.
  +  copy_to_clipboard(self): Copies the generated password to the clipboard.

# Contributing

- Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any bugs or feature requests.

# License

- This project is licensed under the MIT License - see the LICENSE file for details.

# Contact

For any questions or feedback, please contact [Reegan Aakish C](reeganaakish@gmail.com).
