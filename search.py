import os
import json

def check_mp3_names():
    for folder in os.listdir('character_unique'):
        folder_path = os.path.join('character_unique', folder)
        if os.path.isdir(folder_path):
            mp3_file = folder + '.mp3'
            mp3_path = os.path.join(folder_path, mp3_file)
            if not os.path.exists(mp3_path):
                folder_contents = os.listdir(folder_path)
                if folder_contents:
                    folder_contents_str = ', '.join(folder_contents)
                    print(f"Mismatch: {mp3_file} in {folder} folder is missing. Contents: [{folder_contents_str}]")
                else:
                    print(f"Mismatch: {mp3_file} in {folder} folder is missing. \nContents: []")

def scan_json_for_songs():
    with open('chars.json') as file:
        data = json.load(file)
        chars = data['chars']
        missing_songs = []
        for char in chars:
            if 'songs' not in char:
                missing_songs.append(str(char['DevNicknames']))
        
        with open('missing_songs.txt', 'w') as output_file:
            output_file.write('\n'.join(missing_songs))

#scan_json_for_songs()

if __name__ == "__main__":
    scan_json_for_songs()