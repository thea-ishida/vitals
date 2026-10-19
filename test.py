from song import Song
from vitals import Vitals
from workout import Workout

w = Workout("session_001", "2023-03-10")
w.add_song(Song("Eye of the Tiger", "Survivor", 109, "rock"))
w.add_song(Song("Don't Stop the Music", "Rihanna", 171, "pop"))
w.add_song(Song("Scenario", "A tribe called quest", 93, "hip-hop"))

w.add_vital(Vitals(80, (116, 75), 98.2, "2024-03-10 09:00"))
#w.add_vital(Vitals(90, (122, 78), 97.8, "2024-03-10 09:15"))
w.add_vital(Vitals(97, (128, 82), 97.3, "2024-03-10 09:15"))
w.add_vital(Vitals(84, (117, 76), 98.1, "2024-03-10 09:30"))

print("Even split (3 songs, 3 readings):")

for song, readings in w.get_segments():
    print("  " + song.get_title() + ": " + str(len(readings)) + "readings")
    for v in readings:
        print("   " + str(v))
