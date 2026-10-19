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


    def get_segments(self):
        segments = []

        vital_list = self.get_log()
        song_list = self.get_playlist()

        if len(vital_list) == 0 or len(song_list) == 0:
            return None

        min_vitals = len(vital_list) // len(song_list)
        tuple_list = []

        '''
            Create a list of tuples
            each tuple would have 2 params  ((song index) , val (min vital needed for the song))
            (0,2) = 0 is song index, 2 is the number of vitals 
            (1,2) = 1 is song index, 2 is number of vitals
            (2,2) = 2 is song index, 2 is number of vitals
    
            [(0,2), (1,2), (2,2)] 
            *** take the tot # of vitals - (2 (min_vital size) * 3 ( number of songs)) = 2 
            --> first 2 songs in the tuple get 1 extra vital 
    
            when we run through the for loop on the list of tuples, # of times the for loop runs is based off ***
    
            [(0,2), (1,2), (2,2)] --> [(0,3), (1, 3), (2,2)]
        '''
        for i,s in enumerate(song_list):
            vital_tuple = (i, min_vitals)
            tuple_list.append(vital_tuple)

        extra = len(vital_list) - (min_vitals * len(song_list))

        for i in range(extra):
            song_index, number_of_vitals = tuple_list[i]
            tuple_list[i] = (song_index, number_of_vitals + 1)

  

        start = 0
        for song_index, vitals in enumerate(tuple_list):
            end = vitals[-1]
            segment = (song_list[song_index], vital_list[start:end+start])
            start = start + end

            segments.append(segment)



        return segments


    def __str__(self):
        return self.get_session_id(), "on", self.get_date(),":", len(self.get_playlist()),",", len(self.get_log()), "readings"
        

    def get_peak_heart_rate_song(self):
        segments = self.get_segments()

        max_hr = 0
        for song, vitals in segments:

           

            for i in range(len(vitals)):
                # current_max = max(current_max, vitals.get_average_heart_rate())
                # current_max = self.get_average_heart_rate()
                # print("current maxxxxxxx", current_max)

                # print(vitals[i], " !!!!!!!!!!@ ", song)

                print(vitals[i], i, "song ", song)
            # print("current")
            

        
            
        

        


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

    # how about 3 songs, 8 vitals
    # s1: v1, v2, v3
    # s2: v4, v5, v6
    # s3: v7, v8

    # 3 songs 4 vitals
    # s1: v1, v2
    # s2: v3, 
    # s3: v4

  
    workout.add_vital(vital)
    workout.add_vital(vital2)
    workout.add_vital(vital3)
    workout.add_vital(vital4)
    workout.add_vital(vital5)
    # workout.add_vital(vital6)
    # workout.add_vital(vital7)
    # workout.add_vital(vital8)
    # workout.add_vital(vital9)

    # print(workout.get_log())

    print("-------------------")

    # for song, v in workout.get_segments():
    #     print("**", song, v)

    workout.get_peak_heart_rate_song()

if __name__ == "__main__":
    main()


