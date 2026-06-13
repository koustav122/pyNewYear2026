import random

def playlist_randomizer(songs, count):
    if count > len(songs):
        count = len(songs)
    return random.sample(songs, count)

if __name__ == "__main__":
    songs = [
        "Shape of You - Ed Sheeran",
        "Believer - Imagine Dragons",
        "Kesariya - Arijit Singh",
        "Tum Hi Ho - Arijit Singh",
        "Blinding Lights - The Weeknd",
        "Senorita - Shawn Mendes & Camila Cabello",
        "Perfect - Ed Sheeran",
        "Naatu Naatu - RRR"
    ]
    
    print("🎧 Welcome to Playlist Randomizer!")
    num = int(input("How many songs do you want in your playlist? "))
    playlist = playlist_randomizer(songs, num)
    
    print("\n🔥 Your Random Playlist:")
    for track in playlist:
        print("•", track)
