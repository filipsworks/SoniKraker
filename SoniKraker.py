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


def int_to_colon_hex(integer):
    hex_string = hex(integer)[2:]
    hex_string = ":".join(hex_string[i:i+2] for i in range(0, len(hex_string), 2))
    return hex_string


nfctag_uid = bytearray.fromhex(input("Input UID: ").replace(":", ""))
nfc_mfg = bytearray(input("Input MFG: ").encode('ascii'))
seconds_used = "00:00:02:00" # 0 sec

pwd = CRC16(0x49A3, nfctag_uid.copy())
pwd = pwd | (CRC16(pwd, list(nfc_mfg)) << 16)
pwd = (pwd >> 8) & 0x00FF00FF | (pwd << 8) & 0xFF00FF00
print(f"SoniKraker CMD: 1B:{int_to_colon_hex(pwd).upper()},A2:24:{seconds_used}")
