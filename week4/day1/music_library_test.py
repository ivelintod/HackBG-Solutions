import unittest
from music_library import Song


class MusicLibraryTest(unittest.TestCase):

    def setUp(self):
        self.my_song = Song("Whispers in the dark", "John Cooper", "Comatose", "3:13")

    def test_is_instance(self):
        self.assertTrue(isinstance(self.my_song, Song))

    def test_valid_init(self):
        self.assertEqual(self.my_song.artist, "John Cooper")
        self.assertEqual(self.my_song.title, "Whispers in the dark")
        self.assertEqual(self.my_song.album, "Comatose")
        self.assertEqual(self.my_song.length, "3:13")

    def test_valid_str(self):
        self.assertEqual(str(self.my_song), "'Whispers in the dark' - 'John Cooper' from 'Comatose' - '3:13'")

    def test_eq(self):
        test_song = Song("Whispers in the dark", "John Cooper", "Comatose", "3:13")
        self.assertEqual(self.my_song, test_song)

    def test_hash(self):
        result = self.my_song.__hash__()
        self.assertTrue(isinstance(result, int))

    def test_length_of_song(self):







if __name__ == '__main__':
    unittest.main()
