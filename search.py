import os

def check_mp3_names():
    for folder in os.listdir('character_unique'):
        folder_path = os.path.join('character_unique', folder)
        if os.path.isdir(folder_path):
            mp3_file = folder + '.mp3'
            mp3_path = os.path.join(folder_path, mp3_file)
            if not os.path.exists(mp3_path):
                print(f"Mismatch: {mp3_file} in {folder} folder is missing.")

if __name__ == "__main__":
    check_mp3_names()
