from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Initialize the Chrome driver
# driver = webdriver.Chrome(options="./chromedriver.exe")
driver = webdriver.Firefox()


# Function to parse information from URL
def parse_url_info(url):
    parts = url.split('/')
    album_and_song = parts[-1].split('-')
    album_id = album_and_song[0]
    song = '-'.join(album_and_song[1:]).replace('.mp3', '')
    album = parts[-2]

    return {
        'album_id': album_id,
        'album': album.replace('_', ' '),
        'song_id': album_and_song[0],
        'song': song
    }


# Function to get all song links
def get_song_links(url):
    driver.get(url)
    links = []

    # Find all <li> elements inside the specified <div>
    playlist_items = driver.find_elements(By.CSS_SELECTOR, '.jp-playlist ul li')

    for item in playlist_items:
        # Click on the second <a> tag inside each <li>
        clickable_element = item.find_element(By.CSS_SELECTOR, 'div a.jp-playlist-item')
        clickable_element.click()

        # Wait until the 'jp-seeking-bg' class is removed
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".jp-seek-bar.jp-seeking-bg"))
        )

        # Extract the song link
        audio_src = driver.find_element(By.CSS_SELECTOR, '#jp_audio_0').get_attribute('src')
        links.append(audio_src)

        # Check if we have reached the end of the playlist
        if len(links) >= len(playlist_items):
            break

    return links


# Extract song links
song_links = get_song_links('http://www.universidadedocoracao.org/joomla/templates/butterflyway_a/html/player.php')
# Parse all URLs
parsed_data = [parse_url_info(url) for url in song_links]
# Save to JSON file
with open('song_data.json', 'w') as json_file:
    json.dump(parsed_data, json_file, indent=4)
# Save song links to a file
with open('song_links.txt', 'w') as file:
    for link in song_links:
        file.write(link + '\n')

# Close the driver
driver.quit()
