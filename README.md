# Slate

**Slate** is a command-line tool to transcribe audio from video/audio files using OpenAI's Whisper model.  
It extracts and normalizes audio, then produces a timestamped text transcript.

---

## Features

- Extracts audio from video files using FFmpeg  
- Normalizes audio volume for better transcription accuracy  
- Uses OpenAI Whisper for state-of-the-art speech-to-text transcription  
- Provides clean, timestamped transcripts  
- Lightweight and easy to use from the terminal  
- Supports multiple Whisper model sizes (`tiny`, `base`, `small`, `medium`, `large`)  
- Optional Bash autocomplete for smoother command-line experience  

---

## Formats
Video:
MP4 (.mp4) 
AVI (.avi)
MOV (.mov) 
WMV (.wmv)
FLV (.flv)
WEBM (.webm)
MPEG (.mpg, .mpeg)
MTS/M2TS (.mts, .m2ts) 
MXF (.mxf)

Audio:
WAV (.wav)
MP3 (.mp3)
AAC (.aac)
OGG (.ogg)
FLAC (.flac)
M4A (.m4a)

## Installation

You can install Slate via a Debian package:

```bash
sudo dpkg -i slate_1.0.1_all.deb
sudo apt-get install -f  # to fix dependencies if needed
```
slate [--model MODEL] [--language LANG] <input.mkv> <output.txt>

example:

slate --model small --language en /home/user/Downloads/movie.mkv /home/user/Documents/transcript.txt
This command:

- Uses the **small** Whisper model for faster transcription
- Forces transcription in **English** (`--language en`)
- Processes `movie.mkv` from the Downloads folder
- Saves the transcript to the Documents folder
