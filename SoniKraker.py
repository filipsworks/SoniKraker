def CRC16(crc, buffer):
    for i in range(len(buffer)):
        crc ^= buffer[i] << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ 0x1021
            else:
                crc <<= 1
        crc &= 0xFFFF
    return crc


def int_to_colon_hex(integer, bytes_reversed=None):
    hex_string = hex(integer)[2:].zfill(4)
    hex_string = ":".join(hex_string[i:i+2] for i in range(0, len(hex_string), 2))
    if bytes_reversed:
        hex_values = hex_string.split(":")
        reversed_hex_values = hex_values[::-1]
        hex_string = ":".join(reversed_hex_values)
    return hex_string.upper()

def tries_left_to_seconds_used(tries):
    initial_tries = 180
    maximum_seconds_used = 21600 # 60 sec * 2 minutes brushing * 2 times a day * 30 days in month * 3 months recommended lifetime
    return 0 if tries == "" else 120*(180-int(tries))


nfctag_uid = bytearray.fromhex(input("Input UID: ").replace(":", ""))
nfc_mfg = bytearray(input("Input MFG: ").encode('ascii'))
time_left = int_to_colon_hex(tries_left_to_seconds_used(input("Leave # sessions (or leave empty for 180): ")), True)
seconds_used = f"{time_left}:02:00" # 0 sec

pwd = CRC16(0x49A3, nfctag_uid.copy())
pwd = pwd | (CRC16(pwd, list(nfc_mfg)) << 16)
pwd = (pwd >> 8) & 0x00FF00FF | (pwd << 8) & 0xFF00FF00
print(f"SoniKraker CMD: 1B:{int_to_colon_hex(pwd)},A2:24:{seconds_used}")
