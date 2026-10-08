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

    # def get_segments(self):


            
        

        


def main():
    workout = Workout("session1", "2024-0-10")
    song = Song("hello", "Katy Perry", 120, "pop")
    song1 = Song("drop", "Tape B", 180, "dubstep")
    song3 = Song("Where are you now", "Justin Bieber", 100, "edm")
    song4 = Song("Space Jam", "SOSA", 102, "edm")


    vital = Vitals(67, (91, 70), 95.2, "2024-03-10 09:30")
    vital2 = Vitals(50, (91, 70), 95.2, "2024-03-10 09:30")
    vital3 = Vitals(74, (91, 70), 95.2, "2024-03-10 09:30")

    workout.add_song(song)
    workout.add_song(song1)
    workout.add_song(song3)

    workout.add_vital(vital)
    workout.add_vital(vital2)
    workout.add_vital(vital3)



    print("Abnormal readings: ", workout.get_abnormal_readings())


if __name__ == "__main__":
    main()


