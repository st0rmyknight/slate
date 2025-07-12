#!/usr/bin/env python3
import subprocess
import os
import whisper
import tempfile
import contextlib
import wave
import time
from tqdm import tqdm
import argparse
import sys
      
VERSION = "1.0.1"

def extract_audio(mkv_path, wav_path):
    print(f"Extracting audio from {mkv_path} ...")
    subprocess.run([
        "ffmpeg", "-y", "-i", mkv_path,
        "-vn", "-acodec", "pcm_s16le",
        "-ar", "16000", "-ac", "2",
        wav_path
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Audio saved to {wav_path}")

def normalize_audio(input_path, output_path):
    print("Normalizing audio volume...")
    subprocess.run([
        "ffmpeg", "-y", "-i", input_path,
        "-af", "loudnorm",
        output_path
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Normalized audio saved to {output_path}")

def get_audio_duration(wav_path):
    with contextlib.closing(wave.open(wav_path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        return frames / float(rate)

def transcribe_audio(wav_path, model_size="large", language=None):
    print(f"Loading Whisper model: {model_size} ...")
    model = whisper.load_model(model_size)

    duration = get_audio_duration(wav_path)
    pbar = tqdm(total=int(duration), unit="sec", desc="Transcribing")

    result = model.transcribe(wav_path, verbose=False, language=language)

    for _ in range(int(duration)):
        time.sleep(0.1)
        pbar.update(1)

    pbar.close()
    return result["segments"]

def format_transcript(segments):
    print("Formatting transcript...")
    output = []
    for segment in segments:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"].strip()
        output.append(f"[{start:.1f}–{end:.1f}]: {text}")
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description="Slate - Transcribe MKV audio to text")
    parser.add_argument("input", nargs="?", help="Input MKV file path")
    parser.add_argument("output", nargs="?", help="Output transcript text file path")
    parser.add_argument("--language", help="Force language (e.g., en, es, fr)")
    parser.add_argument("--model", default="large", help="Whisper model to use (tiny, base, small, medium, large)")
    parser.add_argument("--version", action="store_true", help="Show version and exit")
    args = parser.parse_args()

    if args.version:
        print(f"Slate version {VERSION}")
        return

    if not args.input or not args.output:
        print("Error: Missing input or output path.")
        parser.print_help()
        sys.exit(1)

    mkv_path = args.input
    out_path = args.output

    if not os.path.isfile(mkv_path):
        print(f"Error: Input file '{mkv_path}' does not exist.")
        sys.exit(1)

    wav_path = tempfile.mktemp(suffix=".wav")
    norm_path = tempfile.mktemp(suffix=".wav")

    try:
        extract_audio(mkv_path, wav_path)
        normalize_audio(wav_path, norm_path)

        whisper_segments = transcribe_audio(norm_path, model_size=args.model, language=args.language)
        full_text = format_transcript(whisper_segments)

        with open(out_path, "w") as f:
            f.write(full_text)

        print(f"Transcription saved to {out_path}")
        
        #  Summary
        print(" Summary:")
        print(f"   Segments: {len(whisper_segments)}")
        print(f"   Duration: {int(get_audio_duration(norm_path))} seconds")
        word_count = sum(len(segment['text'].split()) for segment in whisper_segments)
        print(f"   Estimated Words: {word_count}")
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        for path in [wav_path, norm_path]:
            if os.path.exists(path):
                os.remove(path)

if __name__ == "__main__":
    main()

