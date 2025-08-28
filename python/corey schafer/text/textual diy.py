# Idea in mind:
# Count the amount of letters in certain albums.

myName = "Kelvin"

# example with music
album = "Fuzao"
artist = "Faye Wong"

print(album.find('Search'))

# example with movies
movie = "Shaolin Soccer"
director = "Stephen Chow"

movieMessage = '"' + movie + '"' + ' by ' + director + ' is definitely on my watchlist this year!'
print(movieMessage)
print(movieMessage.replace('watchlist', 'to-do for'))


message1 = f"I haven't really listened to any of {artist}'s albums yet. I would love to listen to {album} by the end of this year."
print(message1)

message2 = f"I love {director} a lot. He's really funny. I've always heard of {movie}, but I haven't gotten to watching it, except for a few clips. I hope I can meet {director} one day though. It would be nice."
print(message2)

delusional = "Imagine if " + myName + " was able to meet " + director + "."
print(delusional)