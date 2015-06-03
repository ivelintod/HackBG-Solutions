from music_library import Song, Playlist
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import os


class MusicCrawler:

    def __init__(self, path):
        self.path = path
        self.playlist = Playlist('Skillet', shuffle=True)

    def generate_playlist(self):
        for root, dirs, filenames in os.walk(self.path):
            for f in filenames:
                log = os.path.join(root, f)
                audio = MP3(log, ID3=EasyID3)
                if audio.get('title') != None:
                    self.playlist.add_song(
                    Song(audio.get('title')[0],
                    audio.get('artist')[0],
                    audio.get('album')[0],
                    str(audio.info.length) + 's'))



crawler = MusicCrawler('/home/ivelin/Downloads/Music/')
crawler.generate_playlist()
print(crawler.playlist.next_song())
print(crawler.playlist.next_song())
print(crawler.playlist.next_song())
print(crawler.playlist.next_song())
print(crawler.playlist.next_song())
print(crawler.playlist.next_song())
