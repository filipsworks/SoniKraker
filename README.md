# SoniKraker
Sonicare brush head nfc pwd cracker and # sessions left nfc cmd generator

Basically a python reimplementation of https://gist.github.com/atc1441/41af75048e4c22af1f5f0d4c1d94bb56 with some extra meat

## Usage
**Beware - You have only 3 tries until the NFC chip in the brush head will lock itself for writing even when using the correct password on subsequent tries. So be extra cautious while entering the UID and MFG**

Just run the python script

1. Input the NFC tag serial number (You can ommit : separation)
2. Input MFG code printed on the bottom of the brushing head (including space and letter)
3. Input the number of sessions You want to have left on the brush head
4. Copy SoniKraker CMD value and run it as advanced NFC command

## Known issues
1. NFC rejects the connection -> either UID/MFG were provided incorrectly or You've exceeded the number of tries providing the bad password and now even the correct one won't work.
2. Sonicare app is showing old number of tries / it rewrites the memory with the old adddres -> Click show my brush heads link on the top of the screen where unfinished sessions counter is displayed, remove the brush head from the brush base and click on the brush info in app, then delete the brush head from app, close the app, reexecute the SoniKraker CMD, connect the brush head and run the app.
