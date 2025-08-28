album = 'Treasure'
artist = 'Cocteau Twins'

message = album + " by " + artist + " is a great album I've been listening to."
# plus sign adds strings

message = '{} by {}. I like this!'.format(album, artist)
# {} is like a template, use .format to fill in

# formatted strings
message = f'{album} by {artist}. Nice choice!'

print(message)