# slate
simple MKV-to-transcript converter using Whisper.  Transcribes MKV files and outputs clean, timestamped text.

Features
Extracts audio from MKV files using FFmpeg

Normalizes audio volume for better transcription accuracy

Uses OpenAI Whisper for state-of-the-art speech-to-text transcription

Provides clean, timestamped transcripts

Lightweight and easy to use from the terminal

Supports multiple Whisper model sizes (tiny, base, small, medium, large)

Optional Bash autocomplete for smoother command-line experience

Installation
You can install Slate via a Debian package:

bash
Copy
Edit
sudo dpkg -i slate_1.0.0_all.deb
sudo apt-get install -f  # to fix dependencies if needed
Slate requires:

Python 3.8+

FFmpeg installed system-wide

Python packages: whisper, tqdm

These dependencies are bundled or installed automatically during package setup.

Usage
Basic command format:

bash
Copy
Edit
slate [--model MODEL] input.mkv output.txt
Example:

bash
Copy
Edit
slate --model small "/path/to/video file.mkv" transcript.txt
Options:

--model : Select Whisper model size (tiny, base, small, medium, large). Default is large.

Autocomplete Setup
To enable Bash autocomplete for slate, source the completion script:

bash
Copy
Edit
source /etc/bash_completion.d/slate
Or add it to your .bashrc:

bash
Copy
Edit
echo "source /etc/bash_completion.d/slate" >> ~/.bashrc
Development
Clone the repo:

bash
Copy
Edit
git clone https://github.com/yourusername/slate.git
cd slate
Build the Debian package:

bash
Copy
Edit
dpkg-deb --build slate-deb
License
This project is licensed under the MIT License — see the LICENSE file for details.

Acknowledgments
Uses OpenAI Whisper for transcription

Audio processing powered by FFmpeg

