import json

# Load chars.json
with open('chars_formatted.json', 'r', encoding='utf-8') as chars_file:
    chars_data = json.load(chars_file)

# Load songs.json
with open('character_songs.json', 'r', encoding='utf-8') as songs_file:
    songs_data = json.load(songs_file)

# Loop through characters in chars.json
for character in chars_data['chars']:
    # Get the DevNicknames value
    dev_nickname = character.get('DevNicknames')
    
    # Check if the DevNicknames exists in songs.json
    if dev_nickname and dev_nickname in songs_data['characters']:
        # Get the songs for the character from songs.json
        character_songs = songs_data['characters'][dev_nickname]['songs']
        
        # Insert the songs into the character in chars.json
        character['songs'] = character_songs

# Write updated chars.json
with open('chars_updated.json', 'w') as chars_updated_file:
    json.dump(chars_data, chars_updated_file, indent=4)
