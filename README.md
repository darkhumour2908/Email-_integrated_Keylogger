# Email Integrated Keylogger

> **WARNING — Legal & Ethical:** This tool logs keystrokes and emails them. **Use only on devices you own or where you have explicit, written permission to monitor.** Unauthorized use is illegal and unethical. The author is not responsible for misuse.

---

## Overview

An educational/administrative tool that records keystrokes with timestamps and, on command (pressing `ESC`), emails the log and deletes the local file. **Designed for lawful use only** (device owner testing, lab research, or explicit monitoring consent).

---

## Features

- Logs every keystroke with a timestamp.
- Human-readable special key names: `[SPACE]`, `[ENTER]`, `[TAB]`, `[BACKSPACE]`, `[ESC]`, etc.
- Press `ESC` to: send the current log as an email, securely delete the local log file, and stop the program.
- No hardcoded passwords — supports secure credentials via environment variables or a `.gitignored` config file.

---

## Requirements

- Python 3.11 (recommended via [pyenv](https://github.com/pyenv/pyenv))
- Internet connection (to send email)
- SMTP-capable email account (Gmail with App Password recommended)

---

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/keylogger-project.git
cd keylogger-project

# (Optional) Fix ownership if files were created as root
sudo chown -R $USER:$USER .

# Install pyenv if you don’t have Python 3.11
curl https://pyenv.run | bash

# Add pyenv to your shell (bash example)
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
exec $SHELL

# Install Python 3.11
MAKEFLAGS="-j2" pyenv install 3.11.12
pyenv local 3.11.12

# Create and activate virtual environment
python -m venv venv3.11
source venv3.11/bin/activate  # Linux / macOS
# venv3.11\Scripts\activate    # Windows (PowerShell)

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# (Optional) pin pynput to avoid issues
pip install pynput==1.7.6

## Run
bash
python3 keylogger.py
