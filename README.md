# Email Integrated Keylogger

> **WARNING — Legal & Ethical:** This tool logs keystrokes and emails them. **Use only on devices you own or where you have explicit, written permission to monitor.** Unauthorized use is illegal and unethical. The author is not responsible for misuse.

---

## Overview

An educational/administrative tool that records keystrokes with timestamps and, on command (pressing `ESC`), emails the log and deletes the local file. **Designed for lawful use only** (device owner testing, lab research, or explicit monitoring consent).

## Features

* Logs every keystroke with a timestamp.
* Human-readable special key names: `[SPACE]`, `[ENTER]`, `[TAB]`, `[BACKSPACE]`, `[ESC]`, etc.
* Press `ESC` to: send the current log as an email, securely delete the local log file, and stop the program.
* No hardcoded passwords — supports secure credentials via environment variables or a `.gitignored` config file.

## Requirements

* Python 3.8+.
* Internet connection (to send email).
* SMTP-capable email account (Gmail with App Password recommended).

## Installation

```bash
# clone the repo
git clone https://github.com/yourusername/keylogger-project.git
cd keylogger-project

# create and activate a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
# venv\Scripts\activate   # Windows (PowerShell)

# install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python3 keylogger.py
```

🧩 Compatibility

This project was originally tested using Python 3.11 in a controlled lab environment.
The pynput package (used for keyboard event capture in the original research) is known to be incompatible with Python 3.12+ — as of mid-2024 to 2025, it may throw a _ThreadHandle TypeError.

If you’re exploring this repository for educational or defensive purposes only:

Use Python 3.11 to ensure compatibility when examining the pseudocode or safe demo components.

The sanitized public version does not include any active key-capture code.

To recreate the analysis environment safely:

python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Run only the safe demo or analysis scripts (not any redacted modules)
python demo_sanitised.py

⚠️ Note: Do not attempt to re-enable or execute any redacted capture functionality.
This repository is provided for educational and defensive research only.



