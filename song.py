class Song:
    def __init__(self, title, artist, bpm, genre):
        self._title = title
        self._artist = artist
        self._bpm = bpm
        self._genre = genre


        #self refers to the current instance of the class and is used to access attributes
        #and methods.
    def get_title(self):
        return self._title

    def get_artist(self):
        return self._artist

    def get_bpm(self):
        return self._bpm

    def get_genre(self):
        return self._genre

    def __str__(self):
        return f"\"{self._title}\" by {self._artist} ({self._bpm} bpm, {self._genre})"

    def __repr__(self):
        return f"Song('{self._title}', '{self._artist}', '{self._bpm}', '{self._genre}')"

    def __eq__(self, other):
        return True if (self._title and self._artist) == (other._title and other._artist) else False

def main():
    s = Song("hello", "Katy Perry", 120, "pop")
    # print(s.get_genre(), " !")
    print("repr", repr(s))
    print("str ", str(s))
    arr = [s, s, s]
    print("without:", arr)

# __name__ is a string python sets for each module,
# when you run a file directly its value is "__main__"
if __name__ == "__main__":
    main()



    