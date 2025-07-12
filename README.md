# Slate

**Slate** is a command-line tool to transcribe audio from MKV video files using OpenAI's Whisper model.  
It extracts and normalizes audio, then produces a timestamped text transcript.

---

## Features

- Extracts audio from MKV files using FFmpeg  
- Normalizes audio volume for better transcription accuracy  
- Uses OpenAI Whisper for state-of-the-art speech-to-text transcription  
- Provides clean, timestamped transcripts  
- Lightweight and easy to use from the terminal  
- Supports multiple Whisper model sizes (`tiny`, `base`, `small`, `medium`, `large`)  
- Optional Bash autocomplete for smoother command-line experience  

---

## Installation

You can install Slate via a Debian package:

```bash
sudo dpkg -i slate_1.0.1_all.deb
sudo apt-get install -f  # to fix dependencies if needed
