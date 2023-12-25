#!/bin/bash

# Create a directory for the songs
mkdir -p songs

# Read each line in the file and download
while IFS= read -r url; do
    wget -P songs "$url"
done < song_links.txt

echo "All downloads complete."
