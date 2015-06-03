#import datetime
import random
import json
from prettytable import PrettyTable
from inflection import dasherize


class Song:
    def __init__(self, title="", artist="", album="", length=""):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        message = "'{}' - '{}' from '{}' - '{}'"
        return message.format(self.title, self.artist, self.album, self.length)

    def __eq__(self, other):
        equal_titles = self.title == other.title
        equal_artists = self.artist == other.artist
        equal_albums = self.album == other.album
        equal_lengths = self.length == other.length
        return equal_titles and equal_artists and equal_albums and equal_lengths

    def __hash__(self):
        return hash(self.title + self.artist + self.album + self.length)

    def length_of_song(self, seconds=False, minutes=False, hours=False):
        length_splitted = self.length.split(':')
        if seconds is False and minutes is False and hours is False:
            return self.length
        elif seconds is True:
            if len(length_splitted) > 2:
                len_seconds = int(length_splitted[2]) + 60 * int(length_splitted[1]) + 3600 * int(length_splitted[0])
            else:
                len_seconds = int(length_splitted[1]) + 60 * int(length_splitted[0])
            return len_seconds
        elif minutes is True:
            if len(length_splitted) > 2:
                len_minutes = int(length_splitted[1]) + 60 * int(length_splitted[0])
            else:
                len_minutes = int(length_splitted[0])
            return len_minutes
        elif hours is True:
            if len(length_splitted) > 2:
                len_hours = int(length_splitted[0])
            else:
                len_hours = 0
            return len_hours


class Playlist:

    def __init__(self, name="Code", repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs = []
        self.list_of_songs = []
        self.index = 0
        self.next_song_shuffle = []

    def add_song(self, song):
        self.songs.append(song)

    def add_songs(self, songs):
        self.list_of_songs.append(songs)

    def remove_song(self, song):
        self.songs.remove(song)

    def total_length(self):
        total_seconds = 0
        total_minutes = 0
        total_hours = 0
        for song in self.songs:
            total_seconds += song.length_of_song(seconds=True)
            while total_seconds >= 60:
                total_seconds -= 60
                total_minutes += 1
            while total_minutes >= 60:
                total_minutes -= 60
                total_hours += 1
        if len(str(total_hours)) > 1 and len(str(total_minutes)) > 1 and len(str(total_seconds)) > 1:
            message = "{}:{}:{}"
        elif len(str(total_hours)) == 1 and len(str(total_minutes)) == 1:
            message = "0{}:0{}:{}"
        elif len(str(total_minutes)) == 1 and len(str(total_seconds)) == 1:
            message = "{}:0{}:0{}"
        elif len(str(total_hours)) == 1 and len(str(total_seconds)) == 1:
            message = "0{}:{}:0{}"
        elif len(str(total_hours)) == 1:
            message = "0{}:{}:{}"
        elif len(str(total_minutes)) == 1:
            message = "{}:0{}:{}"
        elif len(str(total_seconds)) == 1:
            message = "{}:{}:0{}"
        return message.format(total_hours, total_minutes, total_seconds)

    def artists(self):
        artists = []
        for song in self.songs:
            artists.append(song.artist)
        count_artist_songs = 0
        histogram_artists = {}
        for artist in artists:
            for song in self.songs:
                if artist is song.artist:
                    count_artist_songs += 1
            histogram_artists[artist] = count_artist_songs
            count_artist_songs = 0
        return histogram_artists

    def repeat_song(self):
        current_song = self.songs[self.index]
        if self.index < len(self.songs) - 1:
            self.index += 1
        else:
            self.index = 0
        return current_song

    def shuffle_song(self):
        song = random.choice(self.songs)
        if song not in self.next_song_shuffle:
            self.next_song_shuffle.append(song)
            return song
        else:
            if len(self.songs) == len(self.next_song_shuffle):
                self.next_song_shuffle = []
                return self.shuffle_song()
            else:
                return self.shuffle_song()

    def next_song(self):
        if self.repeat:
            return self.repeat_song()
        if self.shuffle:
            return self.shuffle_song()
        else:
            if self.index < len(self.songs):
                song = self.songs[self.index]
                self.index += 1
                return song

    def pprint_playlist(self):
        x = PrettyTable(["Artist", "Song", "Length"])
        for s in self.songs:
            x.add_row([s.artist, s.title, s.length])
        return x

    def save(self):
        dasherized_name = self.name.replace(' ', '-')
        with open('playlist-data/' + dasherized_name + '.json', 'w') as f:
            save_list = []
            for song in self.songs:
                save_list.append((song.title, song.artist, song.album, song.length))
            json.dump(save_list, f)

    @staticmethod
    def load(playlist):
        undasherized_name = playlist.replace('-', ' ').strip('.json')
        p = Playlist(undasherized_name)
        with open('playlist-data/' + playlist, 'r') as f:
            for s in json.load(f):
                loaded_song = Song(s[0], s[1], s[2], s[3])
                p.add_song(loaded_song)
        return p













if __name__ == '__main__':

    skillet = Song("Rise", "John Cooper", "Rise", "1:03:05")
    rise = Song("Monster", "John", "Comatose", "5:43")
    rebirthing = Song("Falling inside the black", "John Cooper", "Rise", "4:35")
    #print(str(skillet))
    #print(skillet.length_of_song(minutes=True))
    monster = Song("Whispers in the dark", "George Graham", "Silence", "5:37")

    s = Playlist("For Code", shuffle=True)
    s.add_song(skillet)
    s.add_song(rise)
    s.add_song(rebirthing)
    print(s.total_length())
    print(s.artists())
    print(s.next_song())
    print(s.next_song())
    print(s.next_song())
    print(s.next_song())
    print(s.next_song())
    print(s.next_song())
    print(s.pprint_playlist())
    '''s.save()'''
    code = Playlist.load('For-Code.json')
    print(code.name == 'For Code')
    print(code.total_length())
    print(code.artists())
    print(code.pprint_playlist())
    #code.name == 'For Code'
    #s.save()
    #p = Playlist.load("For-Code.json")
    #p.add_song(monster)
    #print(p.next_song())
    #print(p.next_song())
    #print(p.next_song())
    #print(p.next_song())
