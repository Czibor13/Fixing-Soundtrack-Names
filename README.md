# Fixing Soundtrack Names


## Purpose

I downloaded an album, and the tracks were improperly named.
Testing a few, it appeared track n contained the sound that n+1 should, and that the last track contained the sound for track "01.".

The way that I wanted to solve this was simple.
Just rename track "01." to track "02." until I get to track "119." which would be track "01.".
However, the operating system would definitely not going to like the two files having the exact same name.
The way I decided to get around that was to temporarily rename the files before going back and assigning them the proper names.

I decided to use tuples to faciliate ordering and pairing the files names and numbers

## Author
* Ryne Czibor
