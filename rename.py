import os

def main():
    # Assumes there is nothing but the files to be renamed in the folder.
    # EX. 04. Metal.flac
    # EX. 106. Sunrise.flac
    # Right now, track 1 holds the sound for the name of track 2, track 2 holds the sound for the name of track 3, etc.
    # So if you play 04. Metal.flac, you get the sound of track 05. If you wanted to play Metal, it is actually track 03.
    
    # Where the songs are
    directory = "M:/Music/Original Soundtrack for something/"
    # Create a list of the files there
    lis = os.listdir(directory)
    # The track number is the first 2 or three characters.
    # Luckily, there is a period after the track number.
    # "ddd" and "dd." can be converted to a float, which can in turn be converted to an int.
    # Creates a list of track numbers as ints
    num = [int(float(x[:3])) for  x in lis]
    # Package the track number as an int with the track file name
    # Then, sort the enumeration. This sorts it by numerical order instead of alphanumerical order
    original_enum = sorted(zip(num, lis))
    # Now that we have the current/improper track number and filename combinations,
    # we will pair the current/improper track numbers with the proper track names.
    # Right now, track 1 holds the sound for the name of track 2, track 2 holds the sound for the name of track 3, etc.
    fixed_enum = [(n, original_enum[n][1]) for n,f in original_enum[0:len(original_enum)-1]]
    # Track 119 holds the sound for the name of track 1
    fixed_enum.append((len(original_enum), original_enum[0][1]))
    # Temporarily rename the files to just the number portion of the current/improper file name
    for n, f in original_enum:
        os.rename(directory + f, directory + str(n))
    # Rename the temporary file names with the proper names
    for n,f in fixed_enum:
        os.rename(directory + str(n), directory + f)
    # Finished

if __name__ == '__main__':
    main()