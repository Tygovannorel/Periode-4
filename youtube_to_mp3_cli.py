#!/usr/bin/env python3
"""
YouTube to MP3 Converter (Command Line versie)
Ondersteunt zowel losse video's als hele playlists
Gebruik: python youtube_to_mp3_cli.py <URL> <output_folder>
"""

import os
import sys
import argparse
from pathlib import Path
import yt_dlp


def download_youtube_to_mp3(url, output_folder, quality='192'):
    """
    Download YouTube video(s) of playlist en converteer naar MP3

    Args:
        url: YouTube URL (kan een enkele video of playlist zijn)
        output_folder: Pad waar de MP3 bestanden opgeslagen worden
        quality: Audio kwaliteit in kbps (default: 192)
    """
    # Maak output folder aan als deze niet bestaat
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Configuratie voor yt-dlp - ALLEEN MP3, GEEN extra bestanden
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': quality,
        }],
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'noplaylist': False,  # Playlists zijn toegestaan
        'quiet': False,
        'no_warnings': False,
        'extract_flat': False,
        'ignoreerrors': True,  # Ga door bij fouten in playlist items
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
        print(f"Audio kwaliteit: {quality} kbps")
        print(f"{'='*60}\n")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Haal eerst informatie op
            print("Video/Playlist informatie ophalen...")
            info = ydl.extract_info(url, download=False)

            # Check of het een playlist is
            if 'entries' in info:
                print(f"\nPlaylist gedetecteerd: {info.get('title', 'Onbekende playlist')}")
                valid_entries = [e for e in info['entries'] if e is not None]
                print(f"Aantal video's: {len(valid_entries)}")
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
    parser = argparse.ArgumentParser(
        description='YouTube to MP3 Converter - Download video\'s of playlists als MP3',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Voorbeelden:
  # Enkele video downloaden
  python youtube_to_mp3_cli.py "https://www.youtube.com/watch?v=VIDEO_ID" ./downloads

  # Playlist downloaden
  python youtube_to_mp3_cli.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" ./music

  # Met aangepaste kwaliteit (320 kbps)
  python youtube_to_mp3_cli.py "VIDEO_URL" ./downloads --quality 320
        """
    )

    parser.add_argument('url', help='YouTube URL (video of playlist)')
    parser.add_argument('output_folder', help='Folder waar MP3 bestanden worden opgeslagen')
    parser.add_argument(
        '-q', '--quality',
        default='192',
        choices=['128', '192', '256', '320'],
        help='Audio kwaliteit in kbps (default: 192)'
    )

    args = parser.parse_args()

    # Start download proces
    download_youtube_to_mp3(args.url, args.output_folder, args.quality)


if __name__ == "__main__":
    main()
