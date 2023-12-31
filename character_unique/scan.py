import json
import os

def create_character_json():
    """Loops through the current directory, creates a JSON structure with folder names and MP3 files."""

    character_data = {"characters": {}}

    for root, _, files in os.walk('.'):
        folder_name = os.path.basename(root)
        mp3_files = [file for file in files if file.endswith('.mp3')]

        if mp3_files:
            character_data["characters"][folder_name] = {"songs": mp3_files}

    with open('character_songs.json', 'w') as f:
        json.dump(character_data, f, indent=4)

if __name__ == '__main__':
    create_character_json()
