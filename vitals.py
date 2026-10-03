from song import Song

s1 = Song("Scenario", "A Tribe Called Quest", 93, "hip-hop")
s2 = Song("Scenario", "A Tribe Called Quest", 99, "hip-hop")
s3 = Song("Sabotage", "The Beastie Boys", 93, "hip-hop")

print(s1)
print(repr(s1))
print(s1.get_title())
print(s1.get_artist())
print(s1.get_bpm())
print(s1.get_genre())
print(s1 == s2) # shouldn't this be false?
print(s1 == s3)