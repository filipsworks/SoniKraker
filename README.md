# SoniKraker
![SoniKraker](https://github.com/filipsworks/SoniKraker/assets/47939098/4e77b4be-fa3b-431e-9bb0-801b8e9ca279)

Sonicare brush head nfc pwd cracker and # sessions left nfc cmd generator

Basically a python reimplementation of https://gist.github.com/atc1441/41af75048e4c22af1f5f0d4c1d94bb56 with some extra meat

## Usage
**Beware - You have only 3 tries until the NFC chip in the brush head will lock itself for writing even when using the correct password on subsequent tries. So be extra cautious while entering the UID and MFG**

Just run the python script

1. Input the NFC tag serial number (You can ommit : separation)
2. Input MFG code printed on the bottom of the brushing head (including space and letter)
3. Input the number of sessions You want to have left on the brush head (or set it to 180 by pressing enter)
4. Copy SoniKraker CMD value and run it as advanced NFC command

![4](https://github.com/filipsworks/SoniKraker/assets/47939098/35d49395-d859-49b5-b38b-bb0d8801c92e)


## Known issues
1. NFC rejects the connection -> either UID/MFG were provided incorrectly or You've exceeded the number of tries providing the bad password and now even the correct one won't work.
2. Sonicare app is showing old number of sessions / it rewrites the memory with the old data -> Click show my brush heads link on the top of the screen where unfinished sessions counter is displayed, remove the brush head from the brush base and click on the brush info in app, then delete the brush head from app, close the app, reexecute the SoniKraker CMD, connect the brush head and run the app.
