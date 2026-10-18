from song import Song
from vitals import Vitals

class Workout:
    def __init__(self, session_id, date):
        self._session_id = session_id
        self._date = date
        self._playlist = [] # a list of Song objects 
        self._log = [] #log is a list of Vitals objects

    def get_session_id(self):
        return self._session_id

    def get_date(self):
        return self._date

    def get_playlist(self):
        # list_copy = self._playlist
        return self._playlist.copy()

    def get_log(self):
        return self._log.copy()

    def add_song(self, song):
        self._playlist.append(song)

    def add_vital(self, vital):
        self._log.append(vital)

    '''
    float or
    None
    Returns the average heart rate across all
    readings. Returns None if the log is empty.
    '''
    def get_average_heart_rate(self):
        heart_rates = []
        logs = self.get_log()

        for log in logs:
            heart_rates.append(log.get_heart_rate())

        return sum(heart_rates) / len(heart_rates) if logs != [] else None

    '''
    Returns a set of unique genre strings from all
    songs in the playlist.
    '''
    def get_unique_genres(self):
        unique_genres = set()
        playlist = self.get_playlist()

        for p in playlist:
            genre = p.get_genre()
            if genre in unique_genres:
                continue
            unique_genres.add(genre)

        return unique_genres

    '''
    Returns a list of all Vitals objects for which
    is_abnormal() returns True.
    '''
    def get_abnormal_readings(self):
        abnormal = []
        logs = self.get_log()
        for log in logs:
            if log.is_abnormal():
                abnormal.append(log)

        return abnormal

    '''
    Divide Vitals logs into equal segments 
    Return list of Song(, [Vitals]) tuples 
    Return None if the playlist or log is empty

    Divude the vitals_log into equal degments, one segment per song in the plalist

    zip() --> runs until the shortest list runs out

    3 songs, 9 readings
    song 0 gets 0-2

    if 
    '''

    def get_segments(self):
        '''
        1) find min num of vitals every soong is required to get len(vital_list) // len(song_list)
        2) determine leftover for what could not be divided evenly 
        3) use a counter to track where we are in vitals list, and a list called segments to store he list of vitals for each song
        4) loop through the song list
        5) assume each song gets the min num of vitals, if there is a remainder > 0, add a vital to the song and subtract the remainder
        6) update the new counter index to move forward in the vitals list
        '''


        segments = []

        vital_list = self.get_log()
        song_list = self.get_playlist()

        if len(vital_list) == 0 or len(song_list) == 0:
            return None

        min_vitals = len(vital_list) // len(song_list)
        remainder = len(vital_list) % len(song_list)
        vital_index = 0

        for song in song_list:
            vital_segment = []

            if remainder > 0:
                vital_segment.append(vital_list[vital_index:vital_index+1])
                remainder -= 1
                

            # print("vital segment", vital_segment)

            vital_index += 1

            segments.append((song, vital_segment))

        # print(segments)

        return segments


        


        
            
        

        


def main():
    workout = Workout("session1", "2024-0-10")
    song = Song("hello", "Katy Perry", 120, "pop")
    song1 = Song("drop", "Tape B", 180, "dubstep")
    song3 = Song("Where are you now", "Justin Bieber", 100, "edm")
    song4 = Song("Space Jam", "SOSA", 102, "edm")
    song5 = Song("Shiver", "John summit", 90, "edm")
    song6 = Song("W", "Subtronics", 190, "RAP")


    vital = Vitals(60, (91, 70), 95.2, "2024-03-10 09:30")
    vital2 = Vitals(50, (91, 70), 95.2, "2024-03-10 09:30")
    vital3 = Vitals(74, (91, 70), 95.2, "2024-03-10 09:30")
    vital4 = Vitals(73, (90, 69), 95.2, "2024-03-10 09:30")
    vital5 = Vitals(71, (90, 69), 95.2, "2024-03-10 09:30")
    vital6 = Vitals(72, (90, 69), 95.2, "2024-03-10 09:30")
    vital7 = Vitals(70, (90, 69), 95.2, "2024-03-10 09:30")
    vital8 = Vitals(78, (90, 69), 96.2, "2024-03-10 09:30")
    vital9 = Vitals(79, (90, 69), 95.2, "2024-03-10 09:30")


    workout.add_song(song)
    workout.add_song(song1)
    workout.add_song(song3)
    # workout.add_song(song4)
    # workout.add_song(song5)
    # workout.add_song(song6)

    # how about 3 songs, 8 vitals59555
    # s1: v1, v2, v3
    # s2: v4, v5, v6
    # s3: v7, v8


  
    workout.add_vital(vital)
    workout.add_vital(vital2)
    workout.add_vital(vital3)
    workout.add_vital(vital4)
    workout.add_vital(vital5)
    workout.add_vital(vital6)
    workout.add_vital(vital7)
    workout.add_vital(vital8)
    # workout.add_vital(vital9)

    print(workout.get_log())

    print("-------------------")

    for song, v in workout.get_segments():
        print(song, v)


if __name__ == "__main__":
    main()


