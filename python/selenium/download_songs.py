import requests
import os

# Read URLs from file
with open('song_links.txt', 'r') as file:
    urls = file.readlines()

# Create a directory for the songs
os.makedirs('songs', exist_ok=True)

# Download each song
for url in urls:
    url = url.strip()
    file_name = url.split('/')[-1]

    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join('songs', file_name), 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {file_name}")
    else:
        print(f"Failed to download: {file_name}")

print("All downloads complete.")
