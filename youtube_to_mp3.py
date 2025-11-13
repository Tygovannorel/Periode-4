#!/usr/bin/env python3
"""
YouTube to MP3 Converter
Ondersteunt zowel losse video's als hele playlists
"""

import os
import sys
from pathlib import Path
import yt_dlp
from tkinter import Tk, filedialog


def select_download_folder():
    """
    Open een GUI dialoog om een download folder te selecteren
    """
    root = Tk()
    root.withdraw()  # Verberg het hoofdvenster
    root.attributes('-topmost', True)  # Zet venster voorop

    folder_path = filedialog.askdirectory(
        title='Selecteer Download Folder',
        initialdir=str(Path.home() / 'Downloads')
    )

    root.destroy()

    if not folder_path:
        print("Geen folder geselecteerd. Programma wordt afgesloten.")
        sys.exit(1)

    return folder_path


def download_youtube_to_mp3(url, output_folder):
    """
    Download YouTube video(s) of playlist en converteer naar MP3

    Args:
        url: YouTube URL (kan een enkele video of playlist zijn)
        output_folder: Pad waar de MP3 bestanden opgeslagen worden
    """
    # Configuratie voor yt-dlp - ALLEEN MP3, GEEN extra bestanden
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'noplaylist': False,  # Playlists zijn toegestaan
        'quiet': False,
        'no_warnings': False,
        'extract_flat': False,
        # ALLEEN MP3 - geen extra bestanden
        'keepvideo': False,  # Verwijder origineel audio bestand na conversie
        'writethumbnail': False,  # Geen thumbnails
        'writeinfojson': False,  # Geen JSON metadata
        'writedescription': False,  # Geen beschrijvingen
        'writesubtitles': False,  # Geen ondertitels
        'writeautomaticsub': False,  # Geen automatische ondertitels
        'writeannotations': False,  # Geen annotaties
        'postprocessor_args': ['-ar', '44100'],  # Standaard sample rate
    }

    try:
        print(f"\n{'='*60}")
        print(f"Download folder: {output_folder}")
        print(f"URL: {url}")
        print(f"{'='*60}\n")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Haal eerst informatie op
            print("Video/Playlist informatie ophalen...")
            info = ydl.extract_info(url, download=False)

            # Check of het een playlist is
            if 'entries' in info:
                print(f"\nPlaylist gedetecteerd: {info.get('title', 'Onbekende playlist')}")
                print(f"Aantal video's: {len(info['entries'])}")
                print("\nStart met downloaden...\n")
            else:
                print(f"\nEnkele video gedetecteerd: {info.get('title', 'Onbekende video')}")
                print("\nStart met downloaden...\n")

            # Download en converteer
            ydl.download([url])

        print(f"\n{'='*60}")
        print("Download en conversie succesvol voltooid!")
        print(f"Bestanden opgeslagen in: {output_folder}")
        print(f"{'='*60}\n")

    except Exception as e:
        print(f"\nERROR: Er is een fout opgetreden tijdens het downloaden:")
        print(f"{str(e)}\n")
        sys.exit(1)


def main():
    """
    Hoofdfunctie van het programma
    """
    print("\n" + "="*60)
    print("YouTube to MP3 Converter")
    print("="*60 + "\n")

    # Vraag om YouTube URL
    url = input("Voer de YouTube URL in (video of playlist): ").strip()

    if not url:
        print("Geen URL ingevoerd. Programma wordt afgesloten.")
        sys.exit(1)

    # Selecteer download folder
    print("\nSelecteer een folder om de MP3 bestanden op te slaan...")
    output_folder = select_download_folder()

    # Start download proces
    download_youtube_to_mp3(url, output_folder)


if __name__ == "__main__":
    main()
