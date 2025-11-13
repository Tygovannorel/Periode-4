# YouTube to MP3 Converter

Een Python tool om YouTube video's en complete playlists te downloaden en om te zetten naar MP3 bestanden.

## Features

- ✅ Download losse YouTube video's
- ✅ Download complete playlists
- ✅ Converteer automatisch naar MP3
- ✅ Kies zelf de download folder (GUI)
- ✅ Goede audio kwaliteit (192 kbps standaard, tot 320 kbps)
- ✅ Progress indicatie tijdens download
- ✅ Command line versie voor gevorderde gebruikers

## Vereisten

- Python 3.7 of hoger
- ffmpeg (voor audio conversie)

### FFmpeg installeren

**Windows:**
```bash
# Via chocolatey
choco install ffmpeg

# Of download van: https://ffmpeg.org/download.html
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

## Installatie

1. Clone of download dit project
2. Installeer de vereiste Python packages:

```bash
pip install -r requirements.txt
```

## Gebruik

### Versie 1: GUI versie (Makkelijk)

Run het script en volg de instructies:

```bash
python youtube_to_mp3.py
```

Het programma vraagt om:
1. Een YouTube URL (video of playlist)
2. Een download folder (via een GUI dialoog)

### Versie 2: Command Line versie (Gevorderd)

Voor meer controle en automatisering:

```bash
# Basis gebruik
python youtube_to_mp3_cli.py "YOUTUBE_URL" "OUTPUT_FOLDER"

# Enkele video downloaden
python youtube_to_mp3_cli.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" ./downloads

# Playlist downloaden
python youtube_to_mp3_cli.py "https://www.youtube.com/playlist?list=PLxxxxxx" ./music

# Met hogere kwaliteit (320 kbps)
python youtube_to_mp3_cli.py "VIDEO_URL" ./downloads --quality 320
```

### Beschikbare kwaliteitsopties

- `128` - 128 kbps (klein bestand)
- `192` - 192 kbps (standaard, goede balans)
- `256` - 256 kbps (hoge kwaliteit)
- `320` - 320 kbps (maximale kwaliteit)

## Voorbeelden

### Enkele video downloaden
```bash
python youtube_to_mp3.py
# Voer in: https://www.youtube.com/watch?v=dQw4w9WgXcQ
# Selecteer folder via GUI
```

### Complete playlist downloaden
```bash
python youtube_to_mp3_cli.py "https://www.youtube.com/playlist?list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf" ./my_music
```

## Bestandsnamen

De MP3 bestanden krijgen automatisch de titel van de video als bestandsnaam. Bijvoorbeeld:
- Video titel: "Amazing Song - Artist Name"
- Bestand: "Amazing Song - Artist Name.mp3"

## Troubleshooting

### "ffmpeg not found"
- Zorg dat ffmpeg geïnstalleerd is (zie hierboven)
- Herstart je terminal/command prompt na installatie

### "ERROR: Unable to download"
- Controleer of de URL correct is
- Sommige video's zijn mogelijk niet beschikbaar in jouw regio
- Sommige video's hebben download restricties

### Download is erg traag
- Dit is normaal en hangt af van je internetsnelheid
- YouTube limiteert soms de downloadsnelheid

### Playlist download stopt bij een fout
- De CLI versie gaat automatisch door naar de volgende video
- Check of alle videos in de playlist beschikbaar zijn

## Tips

1. **Grote playlists**: Voor playlists met veel video's, gebruik de CLI versie zodat je de terminal open kunt laten draaien
2. **Organisatie**: Maak aparte folders voor verschillende playlists
3. **Kwaliteit vs Bestandsgrootte**: 192 kbps is meestal voldoende, gebruik alleen 320 kbps als je echt het beste wilt

## Licentie

Dit project is bedoeld voor persoonlijk gebruik. Respecteer auteursrechten en gebruik deze tool alleen voor content waar je toestemming voor hebt.

## Technische Details

- Gebruikt `yt-dlp` voor het downloaden (moderne fork van youtube-dl)
- Gebruikt `ffmpeg` voor audio extractie en conversie
- Ondersteunt alle websites die yt-dlp ondersteunt (niet alleen YouTube)
